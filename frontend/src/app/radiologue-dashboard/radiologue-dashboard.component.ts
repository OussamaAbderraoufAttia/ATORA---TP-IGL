import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-radiologue-dashboard',
  templateUrl: './radiologue-dashboard.component.html',
  styleUrls: ['./radiologue-dashboard.component.css'],
  imports: [CommonModule]
})
export class RadiologueDashboardComponent {
  exams = [
    { patientName: 'John Doe', exam: 'X-Ray', status: 'Scheduled' },
    { patientName: 'Jane Smith', exam: 'MRI', status: 'Completed' },
    { patientName: 'Alice Johnson', exam: 'CT Scan', status: 'In Progress' }
  ];

  viewResults(patientName: string): void {
    console.log(`Viewing results for ${patientName}`);
    // Implement viewing logic here
  }
}
