from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.validators import RegexValidator

class UtilisateurManager(BaseUserManager):
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

        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Utilisateur(AbstractBaseUser,PermissionsMixin):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True,null=True, blank=True)
    email = models.EmailField(unique=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    derniere_connexion = models.DateTimeField(null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    activation_token = models.CharField(max_length=6, blank=True, null=True)
    reset_token =models.CharField(max_length=6, blank=True, null=True)

    USER_TYPE_CHOICES = [
        ('admin', 'Admin'),
        ('medecin', 'Medecin'),
        ('infirmier', 'Infirmier'),
        ('patient', 'Patient'),
        ('radiologue', 'Radiologue'),
        ('laboratoire', 'Laboratoire'),

    ]
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UtilisateurManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom']

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"


# Models for Medecin, Infirmier, and Patient

class Medecin(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    numero_ordre = models.CharField(max_length=50, unique=True)
    specialite = models.CharField(max_length=20)

class Infirmier(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    service = models.CharField(max_length=100)
    hospital_name = models.ForeignKey('Hospital', on_delete=models.SET_NULL, null=True, blank=True, related_name='infirmiers')

class Patient(models.Model):
    NSS = models.CharField(max_length=15, # Fixez la longueur maximale ici
        validators=[
            RegexValidator(
                regex=r'^\w{15}$',  # Exige exactement 10 caractères alphanumériques
                message="Ce champ doit contenir exactement 15 caractères."
            )
        ], primary_key=True,unique=True)  # National Social Security number
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

class Laboratoire(models.Model):
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, primary_key=True)
    nom_etablissement = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    
class Hospital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


