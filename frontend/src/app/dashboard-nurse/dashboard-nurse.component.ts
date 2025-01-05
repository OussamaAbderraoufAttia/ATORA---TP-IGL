import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard-nurse',
  templateUrl: './dashboard-nurse.component.html',
  styleUrls: ['./dashboard-nurse.component.css'],
  imports: [CommonModule]
})
export class DashboardNurseComponent {
  constructor(private router: Router) { }
navigateToProfile() {
this.router.navigate(['/admin/profile']);
}
  tasks = [
    { patientName: 'John Doe', task: 'Administer medication', time: '09:00' },
    { patientName: 'Jane Smith', task: 'Change dressing', time: '10:30' },
    { patientName: 'Alice Johnson', task: 'Check vital signs', time: '11:15' }
  ];

  completeTask(index: number): void {
    console.log(`Task ${index + 1} completed!`);
    // Logique supplémentaire pour marquer une tâche comme terminée
  }
  showDialog = false;
  selectedTask: any = null;

  openDialog(task: any): void {
    this.selectedTask = { ...task }; // Clone the task object
    this.showDialog = true;
  }

  closeDialog(): void {
    this.showDialog = false;
    this.selectedTask = null;
  }

  saveTask(): void {
    // Update the task in the main list
    const index = this.tasks.findIndex(task => task.patientName === this.selectedTask.patientName);
    if (index > -1) {
      this.tasks[index] = { ...this.selectedTask };
    }
    console.log("here is patientName:", this.tasks)
    this.closeDialog();
  }
}
