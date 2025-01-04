from django.contrib import admin
from .models import Consultation, Ordonnance, Resume, Soin, DPI
'''
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('date', 'bilans_biologiques')
    # Uncomment the following lines if needed
    # search_fields = ('patient__nom', 'patient__prenom', 'medecin__nom', 'medecin__prenom')
    # list_filter = ('date_consultation', 'medecin')

class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('id_diagnostic', 'description', 'patient', 'medecin')
    search_fields = ('patient__nom', 'patient__prenom', 'description')
    list_filter = ('medecin',)

class OrdonnanceAdmin(admin.ModelAdmin):
    list_display = ('date_creation', 'validated', 'patient', 'medecin')
    search_fields = ('patient__nom', 'patient__prenom', 'validated')
    list_filter = ('date_creation', 'validated', 'medecin')
'''
# Register the models with the admin site
admin.site.register(Consultation)
admin.site.register(Ordonnance)
admin.site.register(Resume)
admin.site.register(Soin)
admin.site.register(DPI)