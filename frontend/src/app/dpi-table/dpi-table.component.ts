import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule
import { DpiTableService } from '../dpi-table.service';
import { Router } from '@angular/router';
import { AuthInterceptor } from '../auth.interceptor';
import {  HTTP_INTERCEPTORS, HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-dpi-table',
  templateUrl: './dpi-table.component.html',
  styleUrls: ['./dpi-table.component.css'],
  imports: [CommonModule, FormsModule], // Proper syntax
  providers: [
    DpiTableService,
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true }
  ] // Proper syntax
})
export class DpiTableComponent implements OnInit {

  errorMessage: string = ''; // For error messages
  dpis: any[] = []; // Initialize as an array
  filteredData: any[] = []; // Initialize as an array
  searchText: string = ''; // Initialize searchText
  record: any; // Placeholder for individual record actions
  

  constructor(private router: Router , private dpiTableService: DpiTableService) { }

  ngOnInit(): void {
    this.fetchDpis();
  }
  async getDPIById(id: any) {
    try {
      const dpi = await this.dpiTableService.getDpiById(id);
      console.log('DPI record:', dpi);
      this.router.navigate(['/patient'], { state: { dpi: dpi, id : id } });
      // Handle the DPI record as needed
    } catch (error) {
      console.error('Error fetching DPI record:', error);
      this.errorMessage = 'Failed to load DPI record';
    }
  }
  /**
   * Fetch all DPI records from the service.
   */
  fetchDpis(): void {
    this.dpiTableService.getAllDpi().then(
      (data) => {
        this.dpis = data || []; // Ensure data is an array
        this.filteredData = [...this.dpis]; // Copy initial data for filtering
        console.log('DPI records:', this.dpis);
      },
      (error) => {
        this.errorMessage = 'Failed to load DPI records';
        console.error('Error fetching DPI records:', error);
      }
    );
  }

  /**
   * Filter table based on the search text.
   */
  showtodoctor():boolean{
    return (localStorage.getItem('role') === 'medecin');
  }
  filterTable(): void {
    // Ensure searchText is valid
    const lowerCaseSearch = this.searchText?.toLowerCase() || '';
    // Safely filter the data
    this.filteredData = this.dpis.filter((record) =>
      record.nss.toString().toLowerCase().includes(lowerCaseSearch)
    );
  }

  /**
   * Placeholder for handling row actions.
   */
  handleRowAction(arg0: any): void {
    this.router.navigate(['/patient'], { state: { user: arg0.patient } });
  }
}
