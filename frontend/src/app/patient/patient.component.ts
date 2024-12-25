<<<<<<< HEAD
import { Component, Input } from '@angular/core';
import { InfoItemComponent } from '../info-item/info-item.component'; // Adjust the path as necessary

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
  standalone: true,
  imports: [InfoItemComponent], // Import InfoItemComponent here
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
=======
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';


@Component({
  selector: 'app-patient',
  imports: [],
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})
export class PatientComponent {
  activeTab: string = 'personal'; // Default state

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

}
>>>>>>> 051e9f9962861fe12f69190558fbb6952edf26b6
