from django.db import models

from users.models import Laboratoire, Radiologue,Patient

class ImageMedicale(models.Model):
    """Represents a medical image."""
    id_image = models.AutoField(primary_key=True)
    chemin_fichier = models.CharField(max_length=255)

    def __str__(self):
        return f"Image {self.id_image} - {self.chemin_fichier}"

class ImageMedicale(models.Model):
    """Représente une image médicale obtenue lors d'un examen radiologique."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # L'image est liée à un patient
    chemin_fichier = models.CharField(max_length=255)  # Chemin du fichier image (peut être stocké dans un dossier spécifique)
    
    def __str__(self):
        return f"Image médicale: {self.chemin_fichier} - Patient: {self.patient.nom}"
      
      
class Examen_Consultation(models.Model):
    """Représente un examen effectué pendant une consultation médicale."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # L'examen est lié à un patient
    outils = models.CharField(max_length=100)  # Outils utilisés pour l'examen (par exemple, stéthoscope, thermomètre)
    description = models.TextField()  # Description de l'examen effectué
    
    def __str__(self):
        return f"Examen Consultation: {self.outils} - Patient: {self.patient.nom}"

class Examen_Radiologique(models.Model):
    """Représente un examen radiologique effectué par un radiologue."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # L'examen est lié à un patient
    resultat = models.ForeignKey(ImageMedicale, on_delete=models.CASCADE)  # Référence au résultat sous forme d'image
    date_examen = models.DateField()  # Date de l'examen
    radiologue = models.ForeignKey(Radiologue, on_delete=models.CASCADE)  # Radiologue qui a effectué l'examen
    type_radio = models.CharField(max_length=50)  # Type d'examen radiologique (par exemple, IRM, radiographie)
    
    def __str__(self):
        return f"Examen Radiologique du {self.date_examen} - {self.type_radio} - Patient: {self.patient.nom}"

class ResultatBiologique(models.Model):
    """Represents a biological result."""
    id_resultat = models.AutoField(primary_key=True)
    parametre = models.CharField(max_length=50)
    valeur = models.FloatField()
    unite = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.parametre}: {self.valeur} {self.unite}"

class BilanBiologique(models.Model):
    """Represents a biological report."""
    id_bilan_biologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField()
    laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    resultats = models.ManyToManyField(ResultatBiologique)

    def __str__(self):
        return f"Bilan Biologique #{self.id_bilan_biologique} - {self.date_bilan}"






class ExamenRadiologique(models.Model):
    """Represents a radiological exam."""
    id_examen = models.AutoField(primary_key=True)
    resultat = models.ForeignKey(ImageMedicale, on_delete=models.CASCADE)
    date_examen = models.DateField()
    radiologue = models.ForeignKey(Radiologue, on_delete=models.CASCADE)
    type_radio = models.CharField(max_length=20)

    def __str__(self):
        return f"Examen #{self.id_examen} - {self.type_radio}"


class BilanRadiologique(models.Model):
    """Represents a radiological report."""
    id_bilan_radiologique = models.AutoField(primary_key=True)
    date_bilan = models.DateTimeField()
    examens = models.ManyToManyField(ExamenRadiologique)

    def __str__(self):
        return f"Bilan Radiologique #{self.id_bilan_radiologique}"


        

class Examen_Complementaire(models.Model):
    """Représente un examen complémentaire qui inclut des examens biologiques et radiologiques."""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # L'examen est lié à un patient
    description = models.TextField()  # Description détaillée de l'examen complémentaire
    bilan_Biologique_id = models.ForeignKey(BilanBiologique, on_delete=models.CASCADE, null=True, blank=True)  # Référence à un bilan biologique si applicable
    bilan_Radiologique_id = models.ForeignKey(BilanRadiologique, on_delete=models.CASCADE, null=True, blank=True)  # Référence à un bilan radiologique si applicable
    
    def __str__(self):
        return f"Examen Complémentaire: {self.description[:30]}... - Patient: {self.patient.nom}"








