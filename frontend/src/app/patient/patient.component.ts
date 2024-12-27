import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-patient',
  imports: [CommonModule],
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})
export class PatientComponent {
  activeTab: string = 'personal';
  userRole:string = "admin" // Default state
  isModalOpen = false;
  modalTitle = '';
  modalHeaders: string[] = [];
  modalRows: string[][] = [];

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  setRole(role:string):void{
    this.userRole = role;
  }

  getRole():string{
    return this.userRole;
  }
  
  handleCardClick(category: string) {
    this.modalTitle = category;
    this.modalHeaders = this.getTableHeaders(category);
    this.modalRows = []; // No data rows for now
    this.isModalOpen = true;
  }

  closeModal() {
    this.isModalOpen = false;
  }

  getTableHeaders(category: string): string[] {
    switch (category) {
      case "Consultations":
        return ['ID', 'Date', 'Résumé', 'Actions'];
      case "Bilans Biologique":
        return ['ID', 'Date', 'Laboratoire', 'Actions'];
      case "Soins":
        return ['ID', 'Date', 'Description', 'Actions'];
      case "Diagnostiques":
        return ['ID', 'Date', 'Diagnostic', 'Actions'];
      case "Bilans Radio":
        return ['ID', 'Date', 'Examen', 'Actions'];
      default:
        return [];
    }
  }

  

}
