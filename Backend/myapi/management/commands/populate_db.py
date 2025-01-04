import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Utilisateur, Medecin, Infirmier, Patient, Laborantin, Hospital
from medical_record.models import DPI

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Populating the database...")

        # Create a superuser
        self.create_superuser()

        # Create a medecin user
        self.create_medecin_user()

        # Create a patient with DPI
        self.create_patient_with_dpi()

        # Create an infirmier user
        self.create_infirmier_user()

        # Create a laborantin user
        self.create_laborantin_user()

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))

    def create_superuser(self):
        """Create a superuser."""
        superuser = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            nom='Admin',
            prenom='User',
            role='admin'
        )
        self.stdout.write(self.style.SUCCESS(f"Superuser created: {superuser.email}"))

    def create_medecin_user(self):
        """Create a medecin user."""
        medecin_user = User.objects.create_user(
            email='medecin@example.com',
            password='medecinpassword',
            nom='Medecin',
            prenom='User',
            role='medecin'
        )
        hospital = Hospital.objects.create(name='General Hospital')
        medecin = Medecin.objects.create(
            utilisateur=medecin_user,
            specialite='Cardiology',
            hospital_name=hospital
        )
        self.stdout.write(self.style.SUCCESS(f"Medecin user created: {medecin_user.email}"))

    def create_patient_with_dpi(self):
        """Create a patient user with a DPI."""
        patient_user = User.objects.create_user(
            email='patient@example.com',
            password='patientpassword',
            nom='Patient',
            prenom='User',
            role='patient'
        )
        hospital = Hospital.objects.create(name='City Hospital')
        medecin = Medecin.objects.first()  # Assign the first medecin as the medecin_traitant
        patient = Patient.objects.create(
            utilisateur=patient_user,
            NSS='12345678901',
            date_naissance='1990-01-01',
            adresse='123 Main St',
            mutuelle='Mutuelle A',
            medecin_traitant=medecin,
            personne_contact_nom='John Doe',
            personne_contact_telephone='123-456-7890',
            hopital_residence=hospital
        )
        dpi = DPI.objects.create(
            patient=patient,
            medecin=medecin,
            antecedents='No known allergies.'
        )
        self.stdout.write(self.style.SUCCESS(f"Patient user created: {patient_user.email} with DPI: {dpi.id_dpi}"))

    def create_infirmier_user(self):
        """Create an infirmier user."""
        infirmier_user = User.objects.create_user(
            email='infirmier@example.com',
            password='infirmierpassword',
            nom='Infirmier',
            prenom='User',
            role='infirmier'
        )
        hospital = Hospital.objects.create(name='Community Hospital')
        infirmier = Infirmier.objects.create(
            utilisateur=infirmier_user,
            service='Emergency',
            hospital_name=hospital
        )
        self.stdout.write(self.style.SUCCESS(f"Infirmier user created: {infirmier_user.email}"))

    def create_laborantin_user(self):
        """Create a laborantin user."""
        laborantin_user = User.objects.create_user(
            email='laborantin@example.com',
            password='laborantinpassword',
            nom='Laborantin',
            prenom='User',
            role='laborantin'
        )
        laborantin = Laborantin.objects.create(
            id_utilisateur=laborantin_user,
            nom_etablissement='Lab Corp',
            specialisation='Microbiology'
        )
        self.stdout.write(self.style.SUCCESS(f"Laborantin user created: {laborantin_user.email}"))