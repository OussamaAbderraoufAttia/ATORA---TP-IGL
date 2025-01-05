from rest_framework import serializers
from users.models import Utilisateur,Medecin,Infirmier,Radiologue,Laborantin,Hospital
from django.contrib.auth import authenticate, login
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.utils import timezone
from rest_framework import serializers
from django.core.validators import MinLengthValidator
import re


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = [
            'id', 'nom', 'prenom', 'username', 'email',
            'date_creation', 'derniere_connexion', 'telephone',
            'user_type', 'is_active', 'is_staff'
        ]
        read_only_fields = ['date_creation', 'derniere_connexion']

    
class AuthenticationSerializer(serializers.ModelSerializer):
    credentials = serializers.EmailField(max_length=155, source='email')
    auth_key = serializers.CharField(max_length=68, write_only=True, source='password')
    session_token = serializers.CharField(max_length=255, read_only=True, source='access_token')
    renewal_token = serializers.CharField(max_length=255, read_only=True, source='refresh_token')
    permissions = serializers.CharField(max_length=20, read_only=True, source='role')
    display_name = serializers.CharField(source='__str__', read_only=True)
    user_id = serializers.IntegerField(read_only=True, source='id')

    class Meta:
        model = Utilisateur
        fields = [
            'credentials',
            'auth_key',
            'display_name',
            'session_token',
            'renewal_token',
            'permissions',
            'user_id'
        ]

    def validate(self, data):
        try:
            request = self.context.get('request')
            print(data)
            user = authenticate(
                request,
                email=data.get('email'),
                password=data.get('password')
            )
           

            if not user:
                raise serializers.ValidationError({
                    'auth_error': 'Authentication failed. Please verify your credentials.'
                })

            if not user.is_active:
                raise serializers.ValidationError({
                    'status_error': 'Account is currently inactive.'
                })

            user.derniere_connexion = timezone.now()
            user.save(update_fields=['derniere_connexion'])

            auth_tokens = user.tokens
            auth_tokens = user.tokens
            
            return {
                'id': user.id,
                'email': user.email,
                'full_name': str(user),
                'role': user.role,
                'access_token': str(auth_tokens['access']),
                'refresh_token': str(auth_tokens['refresh']),
            }

        except Exception as e:
            raise serializers.ValidationError({
                'system_error': 'Authentication service unavailable.'
            })

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            k: v for k, v in data.items()
            if v is not None and v != ''
        }


class AccountRegistrationSerializer(serializers.ModelSerializer):
    auth_key = serializers.CharField(
        min_length=6, 
        max_length=68, 
        write_only=True,
        source='password',
        validators=[MinLengthValidator(6)]
    )
    auth_key_confirmation = serializers.CharField(
        min_length=6,
        max_length=68,
        write_only=True,
        source='password2'
    )
    account_type = serializers.ChoiceField(
        choices=Utilisateur.USER_TYPE_CHOICES,
        source='role'
    )
    expertise = serializers.CharField(
        max_length=100, 
        required=False, 
        write_only=True,
        source='specialite'
    )
    prenom = serializers.CharField()
    nom = serializers.CharField()
    telephone = serializers.CharField(
        max_length=10,
        required=True,
        validators=[MinLengthValidator(9)]
    )
    

    class Meta:
        model = Utilisateur
        fields = [
            'email',
            'prenom',
            'nom',
            'auth_key',
            'telephone',
            'auth_key_confirmation',
            'account_type',
            'expertise',
            'telephone'
        ]

    def validate_auth_key(self, value):
        if not re.match(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$', value):
            raise serializers.ValidationError(
                "Password must contain at least one letter and one number"
            )
        return value

    def validate_email(self, value):
        if Utilisateur.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email is already registered")
        return value.lower()

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({
                "auth_error": "Password confirmation does not match"
            })

        account_type = data.get('role')
        if account_type not in dict(Utilisateur.USER_TYPE_CHOICES):
            raise serializers.ValidationError({
                "type_error": "Invalid account type specified"
            })

        if account_type == 'medecin' and not data.get('specialite'):
            raise serializers.ValidationError({
                "expertise_error": "Expertise field is required for medical professionals"
            })

        return data

    def _create_professional_profile(self, user, role, expertise=None):
        profile_mappings = {
            'medecin': lambda: Medecin.objects.create(
                utilisateur=user, 
                specialite=expertise
            ),
            'infirmier': lambda: Infirmier.objects.create(utilisateur=user),
            'laborantin': lambda: Laborantin.objects.create(utilisateur=user),
            'radiologue': lambda: Radiologue.objects.create(utilisateur=user)
        }
        
        create_profile = profile_mappings.get(role)
        if create_profile:
            create_profile()

    def create(self, validated_data):
        try:
            account_type = validated_data.pop('role')
            expertise = validated_data.pop('specialite', None)
            validated_data.pop('password2', None)

            user = Utilisateur.objects.create_user(
                email=validated_data['email'],
                prenom=validated_data.get('prenom'),
                nom=validated_data.get('nom'),
                password=validated_data.get('password')
            )
            user.role = account_type
            user.save(update_fields=['role'])
            self._create_professional_profile(user, account_type, expertise)
            
            return user

        except Exception as e:
            raise serializers.ValidationError({
                "registration_error": "Account creation failed. Please try again."
            })

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'email': instance.email,
            'account_type': instance.role
        }


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
        model = Laborantin
        fields = ['id_utilisateur', 'nom_etablissement', 'specialisation']

    def create(self, validated_data):
        utilisateur_data = validated_data.pop('id_utilisateur')
        utilisateur = Utilisateur.objects.create_user(**utilisateur_data)
        return Laborantin.objects.create(id_utilisateur=utilisateur, **validated_data)


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'contact_number', 'email', 'website']
