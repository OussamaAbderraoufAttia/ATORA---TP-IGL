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
  isDialogOpen = false;
  selectedExam: any = null;
  compteRendu: string = '';
  selectedFile: File | null = null;

  viewResults(patientName: string): void {
    console.log(`Viewing results for ${patientName}`);
    // Implement viewing logic here
  }
  openDialog(exam: any) {
    this.isDialogOpen = true;
    this.selectedExam = exam;
  }

  closeDialog() {
    this.isDialogOpen = false;
    this.selectedExam = null;
    this.compteRendu = '';
    this.selectedFile = null;
  }

  onFileSelect(event: Event) {
    const target = event.target as HTMLInputElement;
    if (target.files) {
      this.selectedFile = target.files[0];
    }
  }

  onSubmit() {
    if (this.selectedFile && this.compteRendu) {
      const formData = new FormData();
      formData.append('compteRendu', this.compteRendu);
      formData.append('radio', this.selectedFile);
      formData.append('patientName', this.selectedExam.patientName);
    } else {
      alert('Please fill out all fields.');
    }
  }
}
