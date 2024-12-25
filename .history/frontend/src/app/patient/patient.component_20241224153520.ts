import { Component, Input } from '@angular/core';

interface PatientInfo {
  securityNumber: string;
  lastName: string;
  firstName: string;
  dateOfBirth: string;
  address: string;
  phone: string;
  insurance: string;
  doctor: string;
  emergencyContact: string;
  emergencyPhone: string;
}

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  @Input() patient!: PatientInfo;
  activeTab: string = 'personal';

  setActiveTab(tab: string) {
    this.activeTab = tab;
  }
}