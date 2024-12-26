import { Component } from '@angular/core';

@Component({
  selector: 'app-patient',
  imports: [],
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})
export class PatientComponent {
  activeTab: string = 'personal';
  userRole:string = "admin" // Default state

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  setRole(role:string):void{
    this.userRole = role;
  }

  getRole():string{
    return this.userRole;
  }

  

}
