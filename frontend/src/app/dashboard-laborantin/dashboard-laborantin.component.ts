import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-dashboard-laborantin',
  templateUrl: './dashboard-laborantin.component.html',
  styleUrls: ['./dashboard-laborantin.component.css'],
  imports: [CommonModule]
})
export class DashboardLaborantinComponent {
  constructor(private router: Router) { }
  tests = [
    { patientName: 'John Doe', test: 'Blood Test', status: 'Pending' },
    { patientName: 'Jane Smith', test: 'Urine Analysis', status: 'In Progress' },
    { patientName: 'Alice Johnson', test: 'Cholesterol Test', status: 'Completed' }
  ];
  navigateToProfile() {
    this.router.navigate(['/profile']);
    }
    showDialog = false;
    selectedPatient: any = null;
    bilan: string = '';
  
    openDialog(patient: any) {
      this.selectedPatient = patient;
      this.showDialog = true;
    }
  
    closeDialog() {
      this.showDialog = false;
      this.selectedPatient = null;
      this.bilan = '';
    }
  
    updateStatus() {
      console.log(`Bilan for ${this.selectedPatient.name}: ${this.bilan}`);
      this.closeDialog();
    }

 
}
