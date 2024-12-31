from django.db import models

# Create your models here.
from django.db import models

from users.models import Medecin, Patient



# Consultation model links Patient and Medecin
class Consultation(models.Model):
    """Represents a medical consultation."""
    date_consultation = models.DateTimeField()
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Consultation for {self.patient} on {self.date_consultation}"

# Diagnostic model      return f"Diagnostic for {self.patient} by Dr. {self.medecin}"

# Ordonnance model (prescription)
class Ordonnance(models.Model):
    """Represents a prescription."""
    date_creation = models.DateField()
    validated = models.CharField(max_length=20)
    # medicament = models.ForeignKey('examinations.Medicament', on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"Ordonnance for {self.patient}"


class Resume(models.Model):
    """Represents the summary of a medical consultation."""
    text = models.TextField()
    antecedents = models.JSONField()  # Medical history or past records in JSON format
    consultation_date = models.DateTimeField()
    # medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Resume for {self.patient.nom} {self.patient.prenom} - Consultation with Dr. {self.medecin.nom} {self.medecin.prenom} on {self.consultation_date}"



class Diagnostic(models.Model):
    id_diagnostic = models.AutoField(primary_key=True)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)
    consultations = models.ManyToManyField(Consultation)
    ordonnance = models.ForeignKey('Ordonnance', on_delete=models.SET_NULL, null=True)
    # examen_complementaire = models.ForeignKey('examinations.ExamenComplementaire', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Diagnostic for {self.patient} by Dr. {self.medecin}"

class Compte_Rendu(models.Model):
    id_compte_rendu = models.AutoField(primary_key=True)
    content = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

class CertificatMedical(models.Model):
    id_certificat = models.AutoField(primary_key=True)
    description = models.TextField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)


    
class Hospital(models.Model):
    id_hospital = models.AutoField(primary_key=True)  # Auto-incremented primary key
    name = models.CharField(max_length=20)  # Name of the hospital, max length of 20 characters

    def __str__(self):
        return self.name    

class Soin(models.Model):
    id_soin = models.AutoField(primary_key=True)
    date_soin = models.DateTimeField()
    infirmier = models.ForeignKey('users.Infirmier', on_delete=models.CASCADE)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    description_soin = models.TextField()
    observation_patient = models.TextField()
    status = models.CharField(max_length=20)

class DPI(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    commentaire_administratif = models.TextField()
    chemin_QR_code = models.CharField(max_length=255)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.SET_NULL, null=True)
    compte_Rendu = models.ForeignKey(Compte_Rendu, on_delete=models.SET_NULL, null=True)
    certificatMedical = models.ForeignKey(CertificatMedical, on_delete=models.SET_NULL, null=True)
    hospitalisation = models.ForeignKey(Hospital, on_delete=models.SET_NULL, null=True)
    soin = models.ForeignKey(Soin, on_delete=models.SET_NULL, null=True)
    
    
    