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
  tests = [
    { patientName: 'John Doe', test: 'Blood Test', status: 'Pending' },
    { patientName: 'Jane Smith', test: 'Urine Analysis', status: 'In Progress' },
    { patientName: 'Alice Johnson', test: 'Cholesterol Test', status: 'Completed' }
  ];

  updateStatus(patientName: string): void {
    console.log(`Updating status for ${patientName}`);
    // Implémenter la logique pour mettre à jour le statut
  }
}
