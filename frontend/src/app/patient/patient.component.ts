import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-patient',
  imports: [CommonModule],
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})
export class PatientComponent implements OnInit {
  activeTab: string = 'personal';
  userRole:string = "" // Default state
  isModalOpen = false;
  modalTitle = '';
  modalHeaders: string[] = [];
  modalRows: string[][] = [];
  user: any = {};

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }
  constructor(private router: Router) {}

  ngOnInit() {
    // Retrieve the user data from the router state
    this.user = history.state.user;
    this.userRole = this.user.user_type;
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
