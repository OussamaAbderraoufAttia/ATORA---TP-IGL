import { Component } from '@angular/core';
import { DpiTableComponent } from '../dpi-table/dpi-table.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  imports: [  DpiTableComponent, CommonModule, FormsModule], // Add FormsModule to the imports arrayimport { Component } from '@angular/core';
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent {
  constructor(private router: Router) { }
createDPI() {
  const patientId = (document.getElementById("patient_id") as HTMLInputElement)?.value;
  const dateCreated = (document.getElementById("dateCreated") as HTMLInputElement)?.value;
  const comment = (document.getElementById("commentaire") as HTMLInputElement)?.value;
  
const newDPI = {patientId: patientId, dateCreated: dateCreated, comment: comment};
console.log(newDPI);
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
