from django.db import models

class TypeExamen(models.TextChoices):
    BIOLOGIQUE = 'BIOLOGIQUE'
    RADIOLOGIQUE = 'RADIOLOGIQUE'

class TypeImageMedicale(models.TextChoices):
    IRM = 'IRM'
    ECHOGRAPHIE = 'ECHOGRAPHIE'
    RADIOGRAPHIE = 'RADIOGRAPHIE'
    SCANNER = 'SCANNER'
    AUTRES = 'AUTRES'

class StatutValidationOrdonnance(models.TextChoices):
    EN_ATTENTE = 'EN_ATTENTE'
    VALIDEE = 'VALIDEE'
    REJETEE = 'REJETEE'

class TypeUtilisateur(models.TextChoices):
    ADMINISTRATIF = 'ADMINISTRATIF'
    MEDECIN = 'MEDECIN'
    INFIRMIER = 'INFIRMIER'
    PHARMACIEN = 'PHARMACIEN'
    LABORATOIRE = 'LABORATOIRE'
    RADIOLOGUE = 'RADIOLOGUE'
    PATIENT = 'PATIENT'
    ADMINISTRATEUR = 'ADMINISTRATEUR'

class SpecialiteMedicale(models.TextChoices):
    MEDECINE_GENERALE = 'MEDECINE_GENERALE'
    CARDIOLOGIE = 'CARDIOLOGIE'
    PNEUMOLOGIE = 'PNEUMOLOGIE'
    NEUROLOGIE = 'NEUROLOGIE'
    PEDIATRIE = 'PEDIATRIE'
    ONCOLOGIE = 'ONCOLOGIE'
    RADIOLOGIE = 'RADIOLOGIE'
    AUTRE = 'AUTRE'

class StatutDPI(models.TextChoices):
    OUVERT = 'OUVERT'
    EN_COURS = 'EN_COURS'
    CLOTURE = 'CLOTURE'
    ARCHIVE = 'ARCHIVE'
    SUSPENDU = 'SUSPENDU'

class TypeCertificat(models.TextChoices):
    ARRET_TRAVAIL = 'ARRET_TRAVAIL'
    APTITUDE = 'APTITUDE'
    INCAPACITE_TEMPORAIRE = 'INCAPACITE_TEMPORAIRE'
    INAPTITUDE = 'INAPTITUDE'
    SUIVI_MEDICAL = 'SUIVI_MEDICAL'
    AUTRE = 'AUTRE'

class StatutCertificat(models.TextChoices):
    ACTIF = 'ACTIF'
    EXPIRE = 'EXPIRE'
    ANNULE = 'ANNULE'
    BROUILLON = 'BROUILLON'
    VALIDE = 'VALIDE'
    SUSPENDU = 'SUSPENDU'

class Consultation(models.Model):
    id_consultation = models.AutoField(primary_key=True)
    numero_securite_sociale = models.CharField(max_length=15)
    date_consultation = models.DateTimeField()
    medecin = models.CharField(max_length=100)
    resume_consultation = models.TextField()
    antecedents = models.TextField()

class Ordonnance(models.Model):
    id_ordonnance = models.AutoField(primary_key=True)
    id_consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    date_prescription = models.DateField()

class Medicament(models.Model):
    id_medicament = models.AutoField(primary_key=True)
    id_ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    nom_medicament = models.CharField(max_length=100)
    dose = models.CharField(max_length=50)
    duree_traitement = models.CharField(max_length=50)

class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    id_consultation = models.ForeignKey(Consultation, on_delete=models.CASCADE)
    type_examen = models.CharField(max_length=20, choices=TypeExamen.choices)
    resultat = models.TextField()
    date_examen = models.DateField()

class ResultatBiologique(models.Model):
    id_resultat = models.AutoField(primary_key=True)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    parametre = models.CharField(max_length=50)
    valeur = models.FloatField()
    unite = models.CharField(max_length=20)

class ImageMedicale(models.Model):
    id_image = models.AutoField(primary_key=True)
    id_examen = models.ForeignKey(Examen, on_delete=models.CASCADE)
    chemin_fichier = models.CharField(max_length=255)
    type_image = models.CharField(max_length=20, choices=TypeImageMedicale.choices)

class Soin(models.Model):
    id_soin = models.AutoField(primary_key=True)
    numero_securite_sociale = models.CharField(max_length=15)
    date_soin = models.DateTimeField()
    infirmier = models.CharField(max_length=100)
    description_soin = models.TextField()
    observation_patient = models.TextField()

class DistributionMedicament(models.Model):
    id_distribution = models.AutoField(primary_key=True)
    id_ordonnance = models.ForeignKey(Ordonnance, on_delete=models.CASCADE)
    pharmacien = models.CharField(max_length=100)
    date_distribution = models.DateTimeField()
    statut_validation = models.CharField(max_length=20, choices=StatutValidationOrdonnance.choices)

class Utilisateur(models.Model):
    id_utilisateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=255)
    type_utilisateur = models.CharField(max_length=20, choices=TypeUtilisateur.choices)
    date_creation = models.DateTimeField()
    derniere_connexion = models.DateTimeField()
    actif = models.BooleanField()

class Medecin(models.Model):
    id_medecin = models.AutoField(primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    numero_ordre = models.CharField(max_length=50, unique=True)
    specialite = models.CharField(max_length=20, choices=SpecialiteMedicale.choices)
    etablissement = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

class Infirmier(models.Model):
    id_infirmier = models.AutoField(primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

class Pharmacien(models.Model):
    id_pharmacien = models.AutoField(primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    etablissement = models.CharField(max_length=100)
    service = models.CharField(max_length=100)

class Laboratoire(models.Model):
    id_laboratoire = models.AutoField(primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    nom_etablissement = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)

class Radiologue(models.Model):
    id_radiologue = models.AutoField(primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    etablissement = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)

class Patient(models.Model):
    numero_securite_sociale = models.CharField(max_length=15, primary_key=True)
    id_utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    mutuelle = models.CharField(max_length=100)
    medecin_traitant = models.CharField(max_length=100)
    personne_contact_nom = models.CharField(max_length=100)
    personne_contact_telephone = models.CharField(max_length=20)

class DossierPatientInformatise(models.Model):
    id_dpi = models.AutoField(primary_key=True)
    numero_securite_sociale = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_creation = models.DateTimeField()
    date_derniere_mise_a_jour = models.DateTimeField()
    statut = models.CharField(max_length=20, choices=StatutDPI.choices)
    medecin_referent_id = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    etablissement_hospitalier = models.CharField(max_length=100)
    numero_dossier_hospitalier = models.CharField(max_length=50, unique=True)
    commentaire_administratif = models.TextField()
    date_derniere_consultation = models.DateField()
    niveau_risque = models.CharField(max_length=20)
    consentement_partage = models.BooleanField()
    langue_communication = models.CharField(max_length=50)
    qr_code = models.CharField(max_length=255)
    chemin_qr_code = models.CharField(max_length=255)
    date_generation_qr_code = models.DateTimeField()

class HistoriqueModificationDPI(models.Model):
    id_historique = models.AutoField(primary_key=True)
    id_dpi = models.ForeignKey(DossierPatientInformatise, on_delete=models.CASCADE)
    id_utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_modification = models.DateTimeField()
    type_modification = models.CharField(max_length=50)
    details_modification = models.TextField()
    ip_modification = models.CharField(max_length=45)

class DocumentAdministratif(models.Model):
    id_document = models.AutoField(primary_key=True)
    id_dpi = models.ForeignKey(DossierPatientInformatise, on_delete=models.CASCADE)
    type_document = models.CharField(max_length=50)
    chemin_fichier = models.CharField(max_length=255)
    date_ajout = models.DateTimeField()
    utilisateur_ajout_id = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class CertificatMedical(models.Model):
    id_certificat = models.AutoField(primary_key=True)
    id_dpi = models.ForeignKey(DossierPatientInformatise, on_delete=models.CASCADE)
    id_medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    numero_securite_sociale = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_emission = models.DateTimeField()
    date_debut_validite = models.DateField()
    date_fin_validite = models.DateField()
    type_certificat = models.CharField(max_length=21, choices=TypeCertificat.choices)
    statut_certificat = models.CharField(max_length=20, choices=StatutCertificat.choices)
    motif = models.TextField()
    duree_arret_travail = models.IntegerField()
    pourcentage_incapacite = models.DecimalField(max_digits=5, decimal_places=2)
    recommandations = models.TextField()
    numero_ordre_medecin = models.CharField(max_length=50)
    etablissement = models.CharField(max_length=100)
    signature_numerique = models.CharField(max_length=255)
    chemin_fichier = models.CharField(max_length=255)