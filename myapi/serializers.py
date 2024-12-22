from rest_framework import serializers
from users.models import (
    Utilisateur,
    Medecin,
    Infirmier,
    Patient,
    Radiologue,
    Laboratoire,
    Hospital
)


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'nom', 'prenom', 'username', 'email',
            'date_creation', 'derniere_connexion', 'telephone',
            'user_type', 'is_active', 'is_staff'
        ]
        read_only_fields = ['date_creation', 'derniere_connexion']


class MedecinSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = Medecin
        fields = ['utilisateur', 'numero_ordre', 'specialite']

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Medecin.objects.create(utilisateur=utilisateur, **validated_data)


class InfirmierSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = Infirmier
        fields = ['utilisateur', 'service', 'hospital_name']

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Infirmier.objects.create(utilisateur=utilisateur, **validated_data)


class PatientSerializer(serializers.ModelSerializer):
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = Patient
        fields = [
            'NSS', 'utilisateur', 'date_naissance', 'adresse',
            'mutuelle', 'medecin_traitant', 'personne_contact_nom',
            'personne_contact_telephone', 'hopital_residence'
        ]

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Patient.objects.create(utilisateur=utilisateur, **validated_data)


class RadiologueSerializer(serializers.ModelSerializer):
    id_utilisateur = UtilisateurSerializer()

    class Meta:
        model = Radiologue
        fields = ['id_utilisateur', 'etablissement', 'qualification']

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('id_utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Radiologue.objects.create(id_utilisateur=utilisateur, **validated_data)


class LaboratoireSerializer(serializers.ModelSerializer):
    id_utilisateur = UtilisateurSerializer()

    class Meta:
        model = Laboratoire
        fields = ['id_utilisateur', 'nom_etablissement', 'specialisation']

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('id_utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Laboratoire.objects.create(id_utilisateur=utilisateur, **validated_data)


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'contact_number', 'email', 'website']
