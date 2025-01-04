from django.db import models
from django.core.files.base import ContentFile
import uuid
from io import BytesIO
import qrcode
from users.models import Patient,Medecin,Utilisateur,Laborantin,Radiologue,Infirmier

class DPI(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, default=1)
    medecin = models.ForeignKey(Medecin, related_name="medcin", on_delete=models.CASCADE, default=1)
    antecedents = models.TextField(blank=True)
    qr_code = models.ImageField(upload_to='qrcodes/', unique=True ) 

    def generate_qr(self):
        if not self.patient or not self.patient.NSS:
            raise ValueError("Nss and patient required")

        user_str = str(self.patient.utilisateur)
        qr_data = self.patient.NSS
        qr = qrcode.QRCode(
            version=2,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        unique_filename = f"qrcodes/{uuid.uuid4().hex}_{user_str}.png"
        self.qr_code.save(unique_filename, ContentFile(buffer.getvalue()), save=False)
       
    def clean(self):
        super().clean()
        if not self.qr_code:
            self.generate_qr()

class Resume(models.Model):
    diagnostic = models.TextField(blank=True, null=True)
    symptomes = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"Résumé de la consultation {self.consultation.id_consultation}" if self.consultation else "Résumé sans consultation"

class Medicament(models.Model):
    id_medicament= models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField()
    quantite = models.PositiveIntegerField()
   
class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    date_prescription = models.DateField(auto_now=True)
    served_ordonnance = models.BooleanField(default=False)
    
class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(DPI, related_name="consultations", on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    resume = models.OneToOneField(Resume, related_name="consultation", on_delete=models.CASCADE)
    ordonnance = models.OneToOneField(Ordonnance, related_name="consultation", on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Consultation {self.id_consultation} pour DPI {self.dpi.patient.utilisateur.nom_complet}"

class Prescription(models.Model):
    id_prescription = models.AutoField(primary_key=True)
    ordonnance = models.ForeignKey(Ordonnance, related_name="prescriptions", on_delete=models.CASCADE)
    medicament = models.OneToOneField(Medicament, related_name="prescription", on_delete=models.CASCADE)    
    dose = models.CharField(max_length=20)
    duree = models.PositiveIntegerField()

class BilanBiologique(models.Model):
    REQUESTED = 'requested'
    DONE = 'done'
    VALIDATED = 'validated'
    STATUS_CHOICES = [
        (REQUESTED, 'Requested'),
        (DONE, 'Done'),
        (VALIDATED, 'Validated'),
        ]
    id_bilanbiologique = models.AutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='bilans_biologiques')
    description = models.TextField(default="")
    date = models.DateField(auto_now=True)
    laborantin = models.ForeignKey(Laborantin, related_name="bilanbiologiques", on_delete=models.CASCADE, null=True)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES,default=REQUESTED)

class Mesure(models.Model):
    id_mesure = models.AutoField(primary_key=True)
    bilan_biologique = models.ForeignKey('BilanBiologique', on_delete=models.CASCADE, related_name="mesures")
    param = models.CharField(max_length=100)
    valeur = models.CharField(max_length=100)

class BilanRadiologique(models.Model):
    id_bilanradiologique = models.AutoField(primary_key=True)
    consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE, related_name='bilans_radiologiques')
    date = models.DateField(auto_now=True)
    radiologue = models.ForeignKey(Radiologue, related_name="bilanradiologiques", on_delete=models.CASCADE,null=True,)
    description = models.TextField(default="",blank=True)
    compte_rendu = models.TextField(blank=True)
    type = models.TextField(default="")

class RadioImage(models.Model):
    id_image = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="radios/")
    bilan_radiologique = models.ForeignKey(BilanRadiologique, related_name="images", on_delete=models.CASCADE)

class Soin(models.Model):
    id_soin = models.AutoField(primary_key=True)
    dpi = models.ForeignKey(DPI, related_name="soins", on_delete=models.CASCADE)
    date_soin = models.DateField(auto_now=True)  
    infirmier = models.ForeignKey(Infirmier, related_name="soins", on_delete=models.CASCADE)
    description_medecin = models.CharField(max_length=200) 
    observation = models.TextField()