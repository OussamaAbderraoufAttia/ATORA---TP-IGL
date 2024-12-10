# models.py

from django.db import models

# Table des Patients
class Patient(models.Model):
    nss = models.CharField(max_length=15, unique=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_de_naissance = models.DateField()
    adresse = models.TextField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    mutuelle = models.CharField(max_length=100, blank=True, null=True)
    contact_durgence = models.CharField(max_length=15, blank=True, null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Table des Utilisateurs
class Utilisateur(models.Model):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('medecin', 'Médecin'),
        ('infirmier', 'Infirmier'),
        ('laborantin', 'Laborantin'),
        ('radiologue', 'Radiologue'),
        ('administrateur', 'Administrateur')
    ]
    
    nom_utilisateur = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    id_patient = models.OneToOneField(Patient, on_delete=models.CASCADE, blank=True, null=True)
    cree_le = models.DateTimeField(auto_now_add=True)
    mis_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_utilisateur

# Table des Dossiers Médicaux (DPI)
class DossierMedical(models.Model):
    id_patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    resume_consultation = models.TextField(blank=True, null=True)
    diagnostic = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    mis_a_jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dossier pour {self.id_patient}"

# Table des Médicaments
class Medicament(models.Model):
    nom = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    duree_traitement = models.CharField(max_length=50)
    cree_le = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

# Table des Ordonnances
class Ordonnance(models.Model):
    id_dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)
    id_medicament = models.ForeignKey(Medicament, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

# Table des Examens Médicaux
class Examen(models.Model):
    id_dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)  # biologique ou radiologique
    resultat = models.TextField(blank=True, null=True)
    url_image = models.URLField(blank=True, null=True)
    url_graphique_tendance = models.URLField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

# Table des Interactions Médicales
class Interaction(models.Model):
    id_dossier_medical = models.ForeignKey(DossierMedical, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

# Tables des Rôles Spécifiques aux Médecins
class Laborantin(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

class Radiologue(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

class Medecin(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

class Infirmier(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)

class Administrateur(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True)
