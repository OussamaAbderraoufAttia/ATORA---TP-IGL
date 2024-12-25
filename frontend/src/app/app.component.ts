import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
<<<<<<< HEAD
import { LoginComponent } from "./login/login.component";
import { PatientComponent } from "./patient/patient.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, LoginComponent, PatientComponent],
=======


@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
>>>>>>> 051e9f9962861fe12f69190558fbb6952edf26b6
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'] // Corrected from styleUrl to styleUrls
})
export class AppComponent {
  title = 'ATORA';

  // Sample patient data to pass to the PatientComponent
  patientData = {
    securityNumber: "704.SSS4266 x52155",
    lastName: "Doe",
    firstName: "Madelynn",
    dateOfBirth: "15/05/1985",
    address: "4703 Davis Trace",
    phone: "212-640-9006",
    insurance: "Mutuelle 2",
    doctor: "Dr. Katherine Feil",
    emergencyContact: "Timmy Schimmel",
    emergencyPhone: "217-21S-73S3"
  };
}