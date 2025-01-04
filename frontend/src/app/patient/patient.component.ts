import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

// Define the type for Antecedents
interface Antecedents {
  allergies: string;
  medical_history: string;
  family_history: string;
}

// Define the type for Consultations
interface Consultation {
  dpi: number; // Patient ID
  resume: {
    symptoms: string;
    diagnosis: string;
    details: string;
  };
  ordonnance: {
    prescription: {
      dose: string;
      duree: string;
      medicament: {
        nom: string;
        description: string;
        quantite: number;
      };
    }[];
  };
  bilan_biologique: {
    description: string;
    parameters: { [key: string]: string }; // Key-value pairs for parameters
  };
  bilan_radiologue: {
    description: string;
    type: string;
  };
}

// Define the type for Ordonnances
interface Ordonnance {
  dose: string;
  duree: string;
  medicament: {
    nom: string;
    description: string;
    quantite: number;
  };
}

// Define the type for Bilans Biologiques
interface BilanBiologique {
  description: string;
  parameters: { [key: string]: string }; // Key-value pairs for parameters
}

// Define the type for Bilans Radiologiques
interface BilanRadiologique {
  description: string;
  type: string;
}

@Component({
  selector: 'app-patient',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  constructor(private router: Router) {}

  activeTab: string = 'personal'; // Default active tab
  isAddConsultationModalOpen: boolean = false; // Controls consultation modal visibility
  isOrdonnanceModalOpen: boolean = false; // Controls ordonnance modal visibility
  isBilanBiologiqueModalOpen: boolean = false; // Controls bilan biologique modal visibility
  isBilanRadiologiqueModalOpen: boolean = false; // Controls bilan radiologique modal visibility
  showBilanBiologiqueForm: boolean = false; // Controls visibility of Bilan Biologique form
  showBilanRadiologiqueForm: boolean = false; // Controls visibility of Bilan Radiologique form

  // New consultation form model
  newConsultation: Consultation = {
    dpi: 2, // Example patient ID
    resume: {
      symptoms: '',
      diagnosis: '',
      details: ''
    },
    ordonnance: {
      prescription: []
    },
    bilan_biologique: {
      description: '',
      parameters: {} // "b1", "b2",..
    },
    bilan_radiologue: {
      description: '',
      type: ''
    }
  };

  // Temporary variables for adding ordonnances, bilans biologiques, and bilans radiologiques
  newOrdonnance: Ordonnance = {
    dose: '',
    duree: '',
    medicament: {
      nom: '',
      description: '',
      quantite: 0
    }
  };

  newBilanBiologiqueParameter: { key: string; value: string } = { key: '', value: '' };

  newBilanRadiologique: BilanRadiologique = {
    description: '',
    type: ''
  };

  selectedMedication: Ordonnance | null = null; // Holds the selected medication for details

  // Add a new consultation
  addConsultation(): void {
    // Log the consultation object to the console
    console.log('Consultation to be sent to the backend:', this.newConsultation);

    // Reset the form and close the modal
    this.closeAddConsultationModal();
  }

  // Add a new ordonnance to the current consultation
  addOrdonnance(): void {
    this.newConsultation.ordonnance.prescription.push({ ...this.newOrdonnance });
    this.closeOrdonnanceModal();
    this.resetOrdonnanceForm();
  }

  // Add a new parameter to the bilan biologique
  addBilanBiologiqueParameter(): void {
    if (this.newBilanBiologiqueParameter.key) {
      // Set the parameter value to an empty string (or any default value)
      this.newConsultation.bilan_biologique.parameters[this.newBilanBiologiqueParameter.key] = '';
      this.newBilanBiologiqueParameter = { key: '', value: '' }; // Reset the form
    }
  }

  // Remove a parameter from the bilan biologique
  removeBilanBiologiqueParameter(key: string): void {
    delete this.newConsultation.bilan_biologique.parameters[key];
  }

  // Add Bilan Biologique Section
  addBilanBiologiqueSection(): void {
    this.showBilanBiologiqueForm = true;
  }

  // Remove Bilan Biologique Section
  removeBilanBiologiqueSection(): void {
    this.showBilanBiologiqueForm = false;
    this.newConsultation.bilan_biologique = {
      description: '',
      parameters: {}
    };
  }

  // Add Bilan Radiologique Section
  addBilanRadiologiqueSection(): void {
    this.showBilanRadiologiqueForm = true;
  }

  // Remove Bilan Radiologique Section
  removeBilanRadiologiqueSection(): void {
    this.showBilanRadiologiqueForm = false;
    this.newConsultation.bilan_radiologue = {
      description: '',
      type: ''
    };
  }

  // Add a new bilan radiologique to the current consultation
  addBilanRadiologique(): void {
    this.newConsultation.bilan_radiologue = { ...this.newBilanRadiologique };
    this.closeBilanRadiologiqueModal();
    this.resetBilanRadiologiqueForm();
  }

  // Reset the consultation form
  resetConsultationForm(): void {
    this.newConsultation = {
      dpi: 2,
      resume: {
        symptoms: '',
        diagnosis: '',
        details: ''
      },
      ordonnance: {
        prescription: []
      },
      bilan_biologique: {
        description: '',
        parameters: {}
      },
      bilan_radiologue: {
        description: '',
        type: ''
      }
    };
  }

  // Reset the ordonnance form
  resetOrdonnanceForm(): void {
    this.newOrdonnance = {
      dose: '',
      duree: '',
      medicament: {
        nom: '',
        description: '',
        quantite: 0
      }
    };
  }

  // Reset the bilan radiologique form
  resetBilanRadiologiqueForm(): void {
    this.newBilanRadiologique = {
      description: '',
      type: ''
    };
  }

  // Open consultation modal
  openAddConsultationModal(): void {
    this.isAddConsultationModalOpen = true;
  }

  // Close consultation modal
  closeAddConsultationModal(): void {
    this.isAddConsultationModalOpen = false;
    this.resetConsultationForm();
  }

  // Open ordonnance modal
  openOrdonnanceModal(): void {
    this.isOrdonnanceModalOpen = true;
  }

  // Close ordonnance modal
  closeOrdonnanceModal(): void {
    this.isOrdonnanceModalOpen = false;
    this.resetOrdonnanceForm();
  }

  // Open bilan biologique modal
  openBilanBiologiqueModal(): void {
    this.isBilanBiologiqueModalOpen = true;
  }

  // Close bilan biologique modal
  closeBilanBiologiqueModal(): void {
    this.isBilanBiologiqueModalOpen = false;
  }

  // Open bilan radiologique modal
  openBilanRadiologiqueModal(): void {
    this.isBilanRadiologiqueModalOpen = true;
  }

  // Close bilan radiologique modal
  closeBilanRadiologiqueModal(): void {
    this.isBilanRadiologiqueModalOpen = false;
    this.resetBilanRadiologiqueForm();
  }

  // Open medication details modal
  openMedicationDetails(medication: Ordonnance): void {
    this.selectedMedication = medication;
  }

  // Close medication details modal
  closeMedicationDetails(): void {
    this.selectedMedication = null;
  }

  // Remove a medication from the ordonnance
  removeMedication(index: number): void {
    this.newConsultation.ordonnance.prescription.splice(index, 1);
  }

  // Navigate to profile
  navigateToProfile(): void {
    this.router.navigate(['/profile']);
  }

  // Set active tab
  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  // Helper function to get keys from an object
  getKeys(obj: any): string[] {
    return Object.keys(obj);
  }
}