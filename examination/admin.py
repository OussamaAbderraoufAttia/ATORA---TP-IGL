from django.contrib import admin
from .models import (
    ImageMedicale,
    Examen_Consultation,
    Examen_Radiologique,
    ResultatBiologique,
    BilanBiologique,
    ExamenRadiologique,
    BilanRadiologique,
    Examen_Complementaire,
)

@admin.register(ImageMedicale)
class ImageMedicaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'chemin_fichier', 'patient')  # Use 'id' instead of 'id_image'
    search_fields = ('chemin_fichier',)
    list_filter = ('patient',)

@admin.register(Examen_Consultation)
class ExamenConsultationAdmin(admin.ModelAdmin):
    list_display = ('id', 'outils', 'patient', 'description')
    search_fields = ('outils', 'description', 'patient__nom')
    list_filter = ('patient',)

@admin.register(Examen_Radiologique)
class ExamenRadiologiqueAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_radio', 'date_examen', 'radiologue', 'patient', 'resultat')  # Use 'id' if no custom primary key
    search_fields = ('type_radio', 'radiologue__nom', 'patient__nom')  # Adjust search fields based on actual model fields
    list_filter = ('date_examen', 'radiologue')

@admin.register(ResultatBiologique)
class ResultatBiologiqueAdmin(admin.ModelAdmin):
    list_display = ('id_resultat', 'parametre', 'valeur', 'unite')  # Use 'id_resultat' for primary key
    search_fields = ('parametre',)
    list_filter = ('parametre',)

@admin.register(BilanBiologique)
class BilanBiologiqueAdmin(admin.ModelAdmin):
    list_display = ('id_bilan_biologique', 'date_bilan', 'laboratoire')  # Use 'id_bilan_biologique' for primary key
    search_fields = ('laboratoire__nom',)
    list_filter = ('date_bilan',)

@admin.register(ExamenRadiologique)
class ExamenRadiologiqueAdmin(admin.ModelAdmin):
    # Corrected list_display
    list_display = ('id_examen', 'type_radio', 'date_examen', 'radiologue', 'resultat')  
    search_fields = ('type_radio', 'radiologue__nom')
    list_filter = ('date_examen',)

@admin.register(BilanRadiologique)
class BilanRadiologiqueAdmin(admin.ModelAdmin):
    list_display = ('id_bilan_radiologique', 'date_bilan')  # Use 'id_bilan_radiologique' for primary key
    search_fields = ('date_bilan',)
    list_filter = ('date_bilan',)

@admin.register(Examen_Complementaire)
class ExamenComplementaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'patient', 'bilan_Biologique_id', 'bilan_Radiologique_id')  # Use 'id' instead of custom primary keys
    search_fields = ('description', 'patient__nom')
    list_filter = ('patient',)
