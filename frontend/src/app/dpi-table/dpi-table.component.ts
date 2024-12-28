import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; // Import FormsModule

@Component({
  selector: 'app-dpi-table',
  templateUrl: './dpi-table.component.html',
  styleUrls: ['./dpi-table.component.css'],
  imports: [CommonModule, FormsModule], // Add FormsModule to the imports arrayimport { Component } from '@angular/core';

})
export class DpiTableComponent {
searchText: any;

record: any;
handleRowAction(arg0: any) {
throw new Error('Method not implemented.');
}
  dpis = [
    {
      id: 1,
      patientId: 'P123456789',
      dateCreated: '12/24/2024, 8:00 AM',
      comment: 'Patient diagnosed with acute appendicitis and started on antibiotics.',
      qrCodePath: '/path/to/qr_code1.png',
    },
    {
      id: 2,
      patientId: 'P987654321',
      dateCreated: '12/25/2024, 2:30 PM',
      comment: 'Patient admitted for chronic sinusitis treatment with prescribed medications.',
      qrCodePath: '/path/to/qr_code2.png',
    },
    // Add more rows as needed
  ];
  filteredData = [...this.dpis];
filterTable() {
  const lowerCaseSearch = this.searchText.toLowerCase();
  this.filteredData = this.dpis.filter((record) =>
    record.patientId.toLowerCase().includes(lowerCaseSearch)
  );
}
}
