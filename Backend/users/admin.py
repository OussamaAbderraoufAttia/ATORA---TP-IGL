from django.contrib import admin
from .models import Utilisateur, Medecin, Infirmier, Patient, Radiologue, Laborantin

# Inline for Patient
class PatientInline(admin.TabularInline):
    model = Patient
    extra = 1  # To allow adding multiple patients

@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'role', 'is_active', 'is_staff', 'date_creation')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('email', 'nom', 'prenom')
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            # Hash the password if it is being set or updated
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)
    # inlines = [PatientInline]  # Allows adding Patients directly from the Utilisateur admin



# Register Medecin model

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ('utilisateur','specialite')
    search_fields = ('specialite',)

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
@admin.register(Laborantin)
class LaboratoireAdmin(admin.ModelAdmin):
    list_display = ('id_utilisateur', 'nom_etablissement', 'specialisation')
    search_fields = ('nom_etablissement', 'specialisation')
