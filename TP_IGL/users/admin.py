from django.contrib import admin
from .models import Utilisateur, Medecin, Infirmier, Patient, Radiologue, Laboratoire

# Inline for Patient
class PatientInline(admin.TabularInline):
    model = Patient
    extra = 1  # To allow adding multiple patients

# Register the Utilisateur model with a custom admin
@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'user_type', 'is_active', 'is_staff', 'date_creation')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('email', 'nom', 'prenom')
    # inlines = [PatientInline]  # Allows adding Patients directly from the Utilisateur admin

# Register Medecin model
@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'numero_ordre', 'specialite')
    search_fields = ('numero_ordre', 'specialite')

# Register Infirmier model
@admin.register(Infirmier)
class InfirmierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'service', 'hospital_name')
    search_fields = ('service',)

# Register Patient model
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'NSS', 'date_naissance', 'adresse', 'mutuelle', 'medecin_traitant', 'hopital_residence')
    search_fields = ('NSS', 'adresse', 'mutuelle')
    list_filter = ('hopital_residence', 'medecin_traitant')

# Register Radiologue model
@admin.register(Radiologue)
class RadiologueAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'etablissement', 'qualification')
    search_fields = ('etablissement', 'qualification')

# Register Laboratoire model
@admin.register(Laboratoire)
class LaboratoireAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'nom_etablissement', 'specialisation')
    search_fields = ('nom_etablissement', 'specialisation')
