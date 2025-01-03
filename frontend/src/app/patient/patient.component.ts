import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { Router } from '@angular/router';
// Define the type for Antecedents
interface Antecedents {
  allergies: string;
  medical_history: string;
  family_history: string;
}

// Define the type for Consultations
interface Consultation {
  consultation: number;
  date_consultation: string;
  outils: string;
  description: string;
  text: string;
  antecedents: Antecedents;
}

// Define the type for Bilans Biologiques
interface BilanBiologique {
  id_bilan_biologique: number;
  date_bilan: string;
  laboratoire_id: number;
  parametre: string;
  valeur: number;
  unite: string;
}

// Define the type for Soins
interface Soin {
  id_soin: number;
  date_soin: string;
  infirmier_name: string;
  description_soin: string;
  observation_patient: string;
  status: string;
}

// Define the type for Diagnostics
interface Diagnostic {
  id_diagnostic: number;
  diagnostic: string;
  date_creation: string;
  medecin_name: string;
  consultations: number;
  ordonnance_id: number;
  validated: string;
  description_examen_complementaire: string;
  bilan_Biologique_id: number | null;
  bilan_Radiologique_id: number | null;
  medicament_names: string;
  medicament_doses: string;
  medicament_duree_traitement: string;
}

// Define the type for Bilans Radiologiques
interface BilanRadiologique {
  id_examen: number;
  date_examen: string;
  radiologue_name: string;
  type_radio: string;
  id_image: number;
  image_link: string;
}

@Component({
  selector: 'app-patient',
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  constructor(private router : Router) { }
  activeTab: string = 'personal';
  userRole: string = "admin"; // Default state
  isModalOpen: boolean = false;
  isBilanModalOpen: boolean = false;
  isSoinsModalOpen: boolean = false;
  isDiagnosticsModalOpen: boolean = false;
  isBilansRadioModalOpen: boolean = false;

  // Flags to control add modals
  isAddConsultationModalOpen: boolean = false;
  isAddBilanModalOpen: boolean = false;
  isAddSoinsModalOpen: boolean = false;
  isAddDiagnosticsModalOpen: boolean = false;
  isAddBilansRadioModalOpen: boolean = false;

  // Form models for new entries
  newConsultation: Consultation = {
    consultation: 0,
    date_consultation: '',
    outils: '',
    description: '',
    text: '',
    antecedents: { allergies: '', medical_history: '', family_history: '' }
  };

  newBilanBiologique: BilanBiologique = {
    id_bilan_biologique: 0,
    date_bilan: '',
    laboratoire_id: 0,
    parametre: '',
    valeur: 0,
    unite: ''
  };

  newSoin: Soin = {
    id_soin: 0,
    date_soin: '',
    infirmier_name: '',
    description_soin: '',
    observation_patient: '',
    status: ''
  };

  newDiagnostic: Diagnostic = {
    id_diagnostic: 0,
    diagnostic: '',
    date_creation: '',
    medecin_name: '',
    consultations: 0,
    ordonnance_id: 0,
    validated: '',
    description_examen_complementaire: '',
    bilan_Biologique_id: null,
    bilan_Radiologique_id: null,
    medicament_names: '',
    medicament_doses: '',
    medicament_duree_traitement: ''
  };

  newBilanRadiologique: BilanRadiologique = {
    id_examen: 0,
    date_examen: '',
    radiologue_name: '',
    type_radio: '',
    id_image: 0,
    image_link: ''
  };

  // Existing data arrays
  consultations: Consultation[] = [
    {
      consultation: 1,
      date_consultation: '2024-12-15 09:00:00',
      outils: 'Tool A',
      description: 'Routine health checkup.',
      text: 'Patient is experiencing general discomfort.',
      antecedents: { allergies: 'None', medical_history: 'Hypertension', family_history: 'No significant issues' }
    },
    {
      consultation: 2,
      date_consultation: '2024-12-16 11:30:00',
      outils: 'Tool B',
      description: 'Blood test analysis for cholesterol.',
      text: 'Symptoms include severe headaches and dizziness.',
      antecedents: { allergies: 'Penicillin', medical_history: 'Asthma', family_history: 'Heart disease in father' }
    }
  ];

  bilansBiologiques: BilanBiologique[] = [
    {
      id_bilan_biologique: 1,
      date_bilan: '2024-12-01 10:00',
      laboratoire_id: 101,
      parametre: 'Hemoglobine',
      valeur: 14.2,
      unite: 'g/dL'
    },
    {
      id_bilan_biologique: 2,
      date_bilan: '2024-12-01 10:00',
      laboratoire_id: 101,
      parametre: 'Leucocytes',
      valeur: 6.5,
      unite: 'x10^9/L'
    }
  ];

  soins: Soin[] = [
    {
      id_soin: 1,
      date_soin: '2024-12-01 08:30',
      infirmier_name: 'John Doe',
      description_soin: 'Dressing change',
      observation_patient: 'Patient in good condition',
      status: 'Completed'
    },
    {
      id_soin: 2,
      date_soin: '2024-12-01 09:00',
      infirmier_name: 'Jane Smith',
      description_soin: 'Blood pressure check',
      observation_patient: 'Slightly elevated BP',
      status: 'Pending'
    }
  ];

  diagnostics: Diagnostic[] = [
    {
      id_diagnostic: 1,
      diagnostic: 'Acute bronchitis',
      date_creation: '2024-12-01 10:30',
      medecin_name: 'Dr. Alice Lee',
      consultations: 1,
      ordonnance_id: 101,
      validated: 'Yes',
      description_examen_complementaire: 'Blood test for liver function',
      bilan_Biologique_id: 1,
      bilan_Radiologique_id: null,
      medicament_names: 'Paracetamol, Ibuprofen',
      medicament_doses: '500 mg, 200 mg',
      medicament_duree_traitement: '5 days, 7 days'
    },
    {
      id_diagnostic: 2,
      diagnostic: 'Fractured arm',
      date_creation: '2024-12-02 12:00',
      medecin_name: 'Dr. John Brown',
      consultations: 2,
      ordonnance_id: 102,
      validated: 'No',
      description_examen_complementaire: 'Chest X-ray for lung check',
      bilan_Biologique_id: null,
      bilan_Radiologique_id: 1,
      medicament_names: 'Amoxicillin, Aspirin',
      medicament_doses: '250 mg, 300 mg',
      medicament_duree_traitement: '10 days, 3 days'
    }
  ];

  bilansRadiologiques: BilanRadiologique[] = [
    {
      id_examen: 1,
      date_examen: '2024-12-03',
      radiologue_name: 'Dr. Alice Green',
      type_radio: 'MRI',
      id_image: 103,
      image_link: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRggxFCY0B7t6ygNNJqp90Zb_QdQpLO_stV2A&s'
    }
  ];
  navigateToProfile() {
    this.router.navigate(['/profile']);
    }
  // Method to set the active tab
  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  // Open modals for viewing data
  openModal(): void {
    this.isModalOpen = true;
  }

  openBilanModal(): void {
    this.isBilanModalOpen = true;
  }

  openSoinsModal(): void {
    this.isSoinsModalOpen = true;
  }

  openDiagnosticsModal(): void {
    this.isDiagnosticsModalOpen = true;
  }

  openBilansRadioModal(): void {
    this.isBilansRadioModalOpen = true;
  }

  // Close modals for viewing data
  closeModal(): void {
    this.isModalOpen = false;
  }

  closeBilanModal(): void {
    this.isBilanModalOpen = false;
  }

  closeSoinsModal(): void {
    this.isSoinsModalOpen = false;
  }

  closeDiagnosticsModal(): void {
    this.isDiagnosticsModalOpen = false;
  }

  closeBilansRadioModal(): void {
    this.isBilansRadioModalOpen = false;
  }

  // Open modals for adding data
  openAddConsultationModal(): void {
    this.isAddConsultationModalOpen = true;
  }

  openAddBilanModal(): void {
    this.isAddBilanModalOpen = true;
  }

  openAddSoinsModal(): void {
    this.isAddSoinsModalOpen = true;
  }

  openAddDiagnosticsModal(): void {
    this.isAddDiagnosticsModalOpen = true;
  }

  openAddBilansRadioModal(): void {
    this.isAddBilansRadioModalOpen = true;
  }

  // Close modals for adding data
  closeAddConsultationModal(): void {
    this.isAddConsultationModalOpen = false;
    this.resetConsultationForm();
  }

  closeAddBilanModal(): void {
    this.isAddBilanModalOpen = false;
    this.resetBilanForm();
  }

  closeAddSoinsModal(): void {
    this.isAddSoinsModalOpen = false;
    this.resetSoinsForm();
  }

  closeAddDiagnosticsModal(): void {
    this.isAddDiagnosticsModalOpen = false;
    this.resetDiagnosticsForm();
  }

  closeAddBilansRadioModal(): void {
    this.isAddBilansRadioModalOpen = false;
    this.resetBilansRadioForm();
  }

  // Reset forms
  resetConsultationForm(): void {
    this.newConsultation = {
      consultation: 0,
      date_consultation: '',
      outils: '',
      description: '',
      text: '',
      antecedents: { allergies: '', medical_history: '', family_history: '' }
    };
  }

  resetBilanForm(): void {
    this.newBilanBiologique = {
      id_bilan_biologique: 0,
      date_bilan: '',
      laboratoire_id: 0,
      parametre: '',
      valeur: 0,
      unite: ''
    };
  }

  resetSoinsForm(): void {
    this.newSoin = {
      id_soin: 0,
      date_soin: '',
      infirmier_name: '',
      description_soin: '',
      observation_patient: '',
      status: ''
    };
  }

  resetDiagnosticsForm(): void {
    this.newDiagnostic = {
      id_diagnostic: 0,
      diagnostic: '',
      date_creation: '',
      medecin_name: '',
      consultations: 0,
      ordonnance_id: 0,
      validated: '',
      description_examen_complementaire: '',
      bilan_Biologique_id: null,
      bilan_Radiologique_id: null,
      medicament_names: '',
      medicament_doses: '',
      medicament_duree_traitement: ''
    };
  }

  resetBilansRadioForm(): void {
    this.newBilanRadiologique = {
      id_examen: 0,
      date_examen: '',
      radiologue_name: '',
      type_radio: '',
      id_image: 0,
      image_link: ''
    };
  }

  // Add new entries
  addConsultation(): void {
    this.consultations.push({ ...this.newConsultation });
    this.closeAddConsultationModal();
  }

  addBilanBiologique(): void {
    this.bilansBiologiques.push({ ...this.newBilanBiologique });
    this.closeAddBilanModal();
  }

  addSoin(): void {
    this.soins.push({ ...this.newSoin });
    this.closeAddSoinsModal();
  }

  addDiagnostic(): void {
    this.diagnostics.push({ ...this.newDiagnostic });
    this.closeAddDiagnosticsModal();
  }

  addBilanRadiologique(): void {
    this.bilansRadiologiques.push({ ...this.newBilanRadiologique });
    this.closeAddBilansRadioModal();
  }

  // Helper method to get keys and custom labels from antecedents object
  getAntecedentKeys(antecedents: Antecedents): { key: keyof Antecedents, label: string }[] {
    const keyLabels: Record<keyof Antecedents, string> = {
      allergies: 'Allergies',
      medical_history: 'Medical History',
      family_history: 'Family History'
    };
    return (Object.keys(antecedents) as (keyof Antecedents)[]).map(key => ({ key, label: keyLabels[key] }));
  }
}