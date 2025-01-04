import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class PatientService {
  private apiUrl = 'https://your-backend-api-url.com/api'; // Replace with your actual API URL

  constructor(private http: HttpClient) {}

  getConsultations(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/consultations`);
  }

  getBilansBiologique(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/bilans-biologique`);
  }

  getSoins(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/soins`);
  }

  getDiagnostiques(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/diagnostiques`);
  }

  getBilansRadio(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/bilans-radio`);
  }
}
