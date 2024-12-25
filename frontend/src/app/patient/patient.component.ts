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
