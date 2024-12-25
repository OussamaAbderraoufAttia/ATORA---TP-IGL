import { Component } from '@angular/core';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent {
  activeTab: string = 'personal'; // Default tab

  patient = {
    securityNumber: '704.SSS4266 x52155',
    lastName: 'Doe',
    firstName: 'Madelynn',
    dateOfBirth: '15/05/1985',
    address: '4703 Davis Trace',
    phone: '212-640-9006',
    insurance: 'Mutuelle 2',
    doctor: 'Dr. Katherine Feil',
    emergencyContact: 'Timmy Schimmel',
    emergencyPhone: '217-21S-73S3'
  };

  setActiveTab(tab: string) {
    this.activeTab = tab;
  }
}
