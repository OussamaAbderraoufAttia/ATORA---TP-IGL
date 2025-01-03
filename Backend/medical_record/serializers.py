from .models import  DPI
from users.models import Utilisateur,Patient,Medecin
from myapi.serializers import AccountRegistrationSerializer
import logging
from rest_framework import serializers
from django.db import transaction
from django.db.models import Q

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
                "password2": f"{validated_attrs['nss']}#2024"
            }
            
            user_serializer = AccountRegistrationSerializer(data=user_data)
            user_serializer.is_valid(raise_exception=True)
            patient_user = user_serializer.save()

            patient_record = Patient.objects.create(
                utilisateur=patient_user,
                NSS=validated_attrs["nss"],
                date_naissance=validated_attrs["birth_date"],
                adresse=validated_attrs["location"],
                telephone=validated_attrs.get("contact_number", ""),
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


class DPIListSerializer(serializers.ModelSerializer):
    id_dpi = serializers.IntegerField(source="id_dpi")
    nom_complet_patient = serializers.CharField(source="patient.utilisateur.__str__")

    class Meta:
        model = DPI
        fields = ["nom_patient", "prenom_patient", "link"]



