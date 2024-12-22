from django.contrib import admin
from .models import (
    Consultation,
    Diagnostic,
    Ordonnance,
    Resume,
    Compte_Rendu,
    CertificatMedical,
    Hospital,
    Soin,
    DPI,
)

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('date_consultation', 'medecin', 'patient')
    search_fields = ('patient__nom', 'patient__prenom', 'medecin__nom', 'medecin__prenom')
    list_filter = ('date_consultation', 'medecin')


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('id_diagnostic', 'description', 'patient', 'medecin')
    search_fields = ('patient__nom', 'patient__prenom', 'description')
    list_filter = ('medecin',)


@admin.register(Ordonnance)
class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('date_creation', 'validated', 'patient', 'medecin')
    search_fields = ('patient__nom', 'patient__prenom', 'validated')
    list_filter = ('date_creation', 'validated', 'medecin')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('consultation_date', 'patient', 'text')
    search_fields = ('patient__nom', 'patient__prenom', 'text')
    list_filter = ('consultation_date',)


@admin.register(Compte_Rendu)
class CompteRenduAdmin(admin.ModelAdmin):
    list_display = ('id_compte_rendu', 'patient', 'content')
    search_fields = ('patient__nom', 'patient__prenom', 'content')
    list_filter = ('patient',)


@admin.register(CertificatMedical)
class CertificatMedicalAdmin(admin.ModelAdmin):
    list_display = ('id_certificat', 'description', 'patient', 'medecin')
    search_fields = ('patient__nom', 'patient__prenom', 'description')
    list_filter = ('medecin',)


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id_hospital', 'name')
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Soin)
class SoinAdmin(admin.ModelAdmin):
    list_display = ('id_soin', 'date_soin', 'infirmier', 'patient', 'status')
    search_fields = ('patient__nom', 'patient__prenom', 'infirmier__utilisateur__username', 'status')
    list_filter = ('date_soin', 'status', 'infirmier')


@admin.register(DPI)
class DPIAdmin(admin.ModelAdmin):
    list_display = ('id_dpi', 'patient', 'date_creation', 'hospitalisation')
    search_fields = ('patient__nom', 'patient__prenom', 'commentaire_administratif', 'chemin_QR_code')
    list_filter = ('date_creation', 'hospitalisation')
