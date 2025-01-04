from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import RegexValidator

class UtilisateurManager(UserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractUser,PermissionsMixin):
    ADMIN = 'admin'
    PATIENT = 'patient'
    MEDECIN = 'medecin'
    INFIRMIER = 'infirmier'
    LABORANTIN = 'laborantin'
    RADIOLOGUE = 'radiologue'
    PHARMACIEN = 'pharmacien'
    USER_TYPE_CHOICES = [
        (ADMIN, 'Admin'),
        (MEDECIN, 'Medecin'),
        (PATIENT, 'Patient'),
        (INFIRMIER, 'Infirmier'),
        (PHARMACIEN, 'Pharmacien'),
        (LABORANTIN, 'Laborantin'),
        ( RADIOLOGUE, 'Radiologue'),
        ]
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True,null=True, blank=True)
    email = models.EmailField(unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    derniere_connexion = models.DateTimeField(auto_now=True,null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    activation_token = models.CharField(max_length=6, blank=True, null=True)
    reset_token =models.CharField(max_length=6, blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }
    def __str__(self):
        return f"{self.prenom} {self.nom} "



class Medecin(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    specialite = models.CharField(max_length=20)
    hospital_name = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='medecins')


class Infirmier(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    service = models.CharField(max_length=100,default="general")
    hospital_name = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='infirmiers')

class Patient(models.Model):
    NSS = models.CharField(max_length=11,unique=True,db_index=True,validators=[RegexValidator(regex=r'^\d{11}$',message="NSS must be exactly 11 digits long.")])
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    mutuelle = models.CharField(max_length=100, null=True, blank=True)
    medecin_traitant = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')
    personne_contact_nom = models.CharField(max_length=100)
    personne_contact_telephone = models.CharField(max_length=20)
    hopital_residence = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')

class Radiologue(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    etablissement = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

class Laborantin(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    nom_etablissement = models.CharField(max_length=100,default="general")
    specialisation = models.CharField(max_length=100,default="general")
    
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


