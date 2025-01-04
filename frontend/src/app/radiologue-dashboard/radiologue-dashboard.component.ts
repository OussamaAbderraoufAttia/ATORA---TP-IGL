import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

interface Exam {
  patientName: string;
  exam: string;
  status: 'Scheduled' | 'Completed' | 'In Progress';
  compteRendu: string;
  imagePath: string; // Path to the uploaded image
}

@Component({
  selector: 'app-radiologue-dashboard',
  templateUrl: './radiologue-dashboard.component.html',
  styleUrls: ['./radiologue-dashboard.component.css'],
  standalone: true,
  imports: [CommonModule, FormsModule],
})
export class RadiologueDashboardComponent {
  constructor(private router: Router) {}

  exams: Exam[] = [
    {
      patientName: 'John Doe',
      exam: 'X-Ray',
      status: 'Scheduled',
      compteRendu: '',
      imagePath: '/images/brain.png', // Default image
    },
    {
      patientName: 'Jane Smith',
      exam: 'MRI',
      status: 'Completed',
      compteRendu: 'No abnormalities detected.',
      imagePath: '/images/brain.png', // Example uploaded image
    },
    {
      patientName: 'Alice Johnson',
      exam: 'CT Scan',
      status: 'In Progress',
      compteRendu: '',
      imagePath: '/images/brain.png', // Default image
    },
  ];

  isDialogOpen = false;
  selectedExam: Exam | null = null;
  selectedFile: File | null = null;

  openDialog(exam: Exam) {
    this.selectedExam = { ...exam }; // Create a copy of the exam
    this.isDialogOpen = true;
  }

  closeDialog() {
    this.isDialogOpen = false;
    this.selectedExam = null;
    this.selectedFile = null;
  }

  navigateToProfile() {
    this.router.navigate(['/profile']);
  }

  onFileSelect(event: Event) {
    const target = event.target as HTMLInputElement;
    if (target.files) {
      this.selectedFile = target.files[0];
    }
  }

  onSubmit() {
    if (this.selectedExam) {
      if (this.selectedFile) {
        // Simulate saving the image to the `./images` folder
        const fileName = `./images/${this.selectedFile.name}`;
        this.selectedExam.imagePath = fileName;
      }

      // Update the exam status to "Completed"
      this.selectedExam.status = 'Completed';

      // Update the exam in the list
      const index = this.exams.findIndex(
        (e) => e.patientName === this.selectedExam!.patientName
      );
      if (index !== -1) {
        this.exams[index] = { ...this.selectedExam };
      }

      // Close the dialog
      this.closeDialog();
    }
  }
}