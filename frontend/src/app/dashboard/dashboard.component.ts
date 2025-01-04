import { Component } from '@angular/core';
import { DpiTableComponent } from '../dpi-table/dpi-table.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { Router } from '@angular/router';
import { DashboardService } from '../dashboard.service';


@Component({
  selector: 'app-dashboard',
  imports: [  DpiTableComponent, CommonModule, FormsModule], // Add FormsModule to the imports arrayimport { Component } from '@angular/core';
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  constructor(private router: Router, private dashboardService: DashboardService) { }
  patient ={
    nom: "",
    prenom: "",
    nss: "",
    birth_date: "",
    location: "",
    contact_number: "",
    insurance: "",
    emergency_contact: "",
    doctor_full_name: ""
  }
async  createDPI() {
  const nom = (document.getElementById("family name") as HTMLInputElement)?.value;
  const prenom = (document.getElementById("Name") as HTMLInputElement)?.value;
  const nss = (document.getElementById("NSS") as HTMLInputElement)?.value;
  const birth_date = (document.getElementById("birthdate") as HTMLInputElement)?.value;
  const location = (document.getElementById("address") as HTMLInputElement)?.value;
  const contact_number = (document.getElementById("phone") as HTMLInputElement)?.value;
  const insurance = (document.getElementById("insurance") as HTMLInputElement)?.value;
  const emergency_contact = (document.getElementById("Contact name") as HTMLInputElement)?.value;
  const doctor_full_name = (document.getElementById("doctor name") as HTMLInputElement)?.value;

  
  this.patient = {
    nom: nom,
    prenom: prenom,
    nss: nss,
    birth_date: birth_date,
    location: location,
    contact_number: contact_number,
    insurance: insurance,
    emergency_contact: emergency_contact,
    doctor_full_name: doctor_full_name
  }
  try {
    const response = await this.dashboardService.createDpi(this.patient);
    console.log('DPI created successfully', response);
    // Handle success response
  } catch (error) {
    console.error('Error creating DPI', error);
    alert('Failed to create DPI');
    // Handle error response
  }
  
}
  isDialogOpen: boolean = false;

  
  openDialog() {
    this.isDialogOpen = true;
  }
  getrole(): string {
    return localStorage.getItem('role') || '';
  }

  closeDialog() {
    this.isDialogOpen = false;
  }
  isQRCodeScannerVisible = false;

  openQRCodeScanner(): void {
    this.isQRCodeScannerVisible = true;
  }
  navigateToProfile() {
    this.router.navigate(['/profile']);
  }

  closeQRCodeScanner(): void {
    this.isQRCodeScannerVisible = false;
  }

  startScanning(): void {
    alert('QR Code scanner started!');
    // Here you can integrate a QR code scanning library
  }

}
