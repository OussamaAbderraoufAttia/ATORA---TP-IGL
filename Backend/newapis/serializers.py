from medical_record.models import DPI, BilanBiologique, BilanRadiologique, Consultation, Medicament, Mesure, Ordonnance, Prescription, Resume, Soin
from users.models import Utilisateur,Patient,Medecin
from myapi.serializers import AccountRegistrationSerializer
import logging
from rest_framework import serializers
from django.db import transaction
from django.db.models import Q



class SoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soin
        fields = ['id_soin', 'dpi', 'date_soin', 'infirmier',  'observation']
        read_only_fields = ['id_soin', 'date_soin']



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = ['email', 'telephone', 'date_creation']
        read_only_fields = ['date_creation']


class MedicamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicament
        fields = ['nom', 'description', 'prix', 'quantite']



class PrescriptionSerializer(serializers.ModelSerializer):
    medicament = MedicamentSerializer()

    class Meta : 
        model =Prescription
        fields = ['dose','duree','medicament']
class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['diagnostic', 'symptomes', 'antecedents', 'autres_informations']

class OrdonnanceSerializer(serializers.ModelSerializer):
    prescription = PrescriptionSerializer(many=True, required=False)

    class Meta:
        model = Ordonnance
        fields = ['date_prescription', 'etat_ordonnance', 'prescription']
class BilanRadiologiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BilanRadiologique
        fields = ['description', 'type']





    class Meta:
        model = DPI
        fields = [
            "nss",
            "nom_complet_patient",
            "date_de_naissance",
            "adresse",
            "telephone",
            "mutuelle",
            "personne_contact_nom",
            'person_contact_telephone',
            "nom_complet_medecin",
            'consultations',
            'soins',
        ]

class DPIListSerializer(serializers.ModelSerializer):
    id_dpi = serializers.IntegerField(source="id_dpi")
    nom_complet_patient = serializers.CharField(source="patient.utilisateur.__str__")

    class Meta:
        model = DPI
        fields = ["nom_complet_patient", "link"]


logger = logging.getLogger(__name__)

class DpiCreateSerializer(serializers.Serializer):
    nom = serializers.CharField(max_length=100)
    prenom = serializers.CharField(max_length=100)
    nss = serializers.CharField(max_length=20)
    birth_date = serializers.DateField()
    location = serializers.CharField()
    contact_number = serializers.CharField(max_length=15)
    insurance = serializers.CharField(max_length=100)
    emergency_contact = serializers.CharField(max_length=100)
    doctor_full_name = serializers.CharField(max_length=200)

    def _locate_doctor(self, full_name):
        names = [n.lower() for n in full_name.strip().split()][:2]
        doctor = Utilisateur.objects.filter(
            Q(prenom__iexact=names[0], nom__iexact=names[1]) |
            Q(nom__iexact=names[0], prenom__iexact=names[1]),
            role=Utilisateur.MEDECIN
        ).first()
        
        if not doctor:
            raise serializers.ValidationError({"doctor": "Provider not found in database."})
        return doctor

    def validate(self, attrs):
        if len(attrs["doctor_full_name"].split()) < 2:
            raise serializers.ValidationError(
                {"doctor": "Full name required for provider identification."}
            )
        attrs["provider"] = self._locate_doctor(attrs["doctor_full_name"])
        return attrs

    @transaction.atomic
    def create(self, validated_attrs):
        try:
            base_email = f"{validated_attrs['prenom'][:3]}{validated_attrs['nom'][:3]}{validated_attrs['nss'][-4:]}"
            email = f"{base_email.lower()}@medical.org"

            user_data = {
                "email": email,
                "prenom": validated_attrs["nom"],
                "nom": validated_attrs["nom"],
                "role": Utilisateur.PATIENT,
                "password": f"{validated_attrs['nss']}#2024",
                "password2": f"{validated_attrs['nss']}#2024",
                "telephone":f"{validated_attrs.get("contact_number","")}"
            }
            
            user_serializer = AccountRegistrationSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            patient_user = user_serializer.save()

            patient_record = Patient.objects.create(
                utilisateur=patient_user,
                NSS=validated_attrs["nss"],
                date_naissance=validated_attrs["birth_date"],
                adresse=validated_attrs["location"],
                mutuelle=validated_attrs["insurance"],
                personne_contact_nom=validated_attrs["emergency_contact"]
            )

            provider, _ = Medecin.objects.get_or_create(
                utilisateur=validated_attrs["provider"]
            )
            medical_record = DPI.objects.create(
                patient=patient_record, 
                medecin=provider
            )
            medical_record.generate_qr()
            
            medical_record.save()
            return medical_record
        

        except Exception as e:
            logger.error(f"Record creation failed: {str(e)}")
            raise serializers.ValidationError({"error": "Unable to process registration request."})
    def to_representation(self, instance):
    
        return {
            "message": "DPI created",
            "dpi_id": instance.id_dpi,
        }


class QRCodeSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.URLField(source='qr_code.url', read_only=True)

    class Meta:
        model = DPI
        fields = ["qr_code_url"]



##################################Consultation ++ Bilans############################################


class MesureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesure
        fields = ['id_mesure', 'param', 'valeur']


class BilanBiologiqueSerializer(serializers.ModelSerializer):
    mesures = MesureSerializer(many=True, required=False)

    class Meta:
        model = BilanBiologique
        fields = ['id_bilanbiologique', 'consultation', 'description', 'date', 'status', 'mesures']
        read_only_fields = ['id_bilanbiologique', 'consultation', 'date', 'status']

    def create(self, validated_data):
        mesures_data = validated_data.pop('mesures', [])
        bilan = BilanBiologique.objects.create(**validated_data)
        for mesure_data in mesures_data:
            Mesure.objects.create(bilan_biologique=bilan, **mesure_data)
        return bilan
    

class ConsultationSerializer(serializers.ModelSerializer):
    id_consultation = serializers.IntegerField(read_only=True)
    resume = ResumeSerializer(required=False)
    ordonnance = OrdonnanceSerializer(required=False)
    bilan_biologique = BilanBiologiqueSerializer(required=False)
    bilan_radiologue = BilanRadiologiqueSerializer(required=False)

    class Meta:
        model = Consultation
        fields = ['id_consultation', 'dpi', 'date', 'resume', 'ordonnance', 'bilan_radiologue', 'bilan_biologique']
        read_only_fields = ['id_consultation', 'date']


    def create(self, validated_data):
        # Extract nested data
        bilan_biologique_data = validated_data.pop('bilan_biologique', None)
        resume_data = validated_data.pop('resume', None)
        ordonnance_data = validated_data.pop('ordonnance', None)
        bilan_radiologue_data = validated_data.pop('bilan_radiologue', None)

        # Create the Consultation object
        consultation = Consultation.objects.create(**validated_data)

        # Creating nested  objects if data is provided
        if bilan_biologique_data:
            BilanBiologique.objects.create(consultation=consultation, **bilan_biologique_data)
        if resume_data:
            Resume.objects.create(consultation=consultation, **resume_data)
        if ordonnance_data:
            Ordonnance.objects.create(consultation=consultation, **ordonnance_data)
        if bilan_radiologue_data:
            BilanRadiologique.objects.create(consultation=consultation, **bilan_radiologue_data)

        return consultation
    



class DPIDetailSerializer(serializers.ModelSerializer):
    consultations = ConsultationSerializer(many=True, read_only=True)
    soins = SoinSerializer(many=True, read_only=True)
    nom_complet_patient = serializers.CharField(source="patient.utilisateur.__str__")
    nss = serializers.CharField(source="patient.NSS")
    date_de_naissance = serializers.DateField(source="patient.date_naissance")
    adresse = serializers.CharField(source="patient.adresse")
    telephone = serializers.CharField(source="patient.personne_contact_telephone")
    mutuelle = serializers.CharField(source="patient.mutuelle")
    person_contact_telephone = serializers.CharField(source="patient.personne_contact_telephone")
    personne_contact_nom=serializers.CharField(source="patient.personne_contact_nom")
    nom_complet_medecin = serializers.CharField(source="medecin.utilisateur.__str__")
    