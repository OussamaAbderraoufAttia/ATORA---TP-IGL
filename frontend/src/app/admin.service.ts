import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AdminService {
  private apiUrl = 'https://api.example.com/admin'; // Replace with your backend URL

  constructor(private http: HttpClient) {}

  getAdminData(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/profile`);
  }

  updateAdminData(adminData: any): Observable<any> {
    return this.http.put<any>(`${this.apiUrl}/profile`, adminData);
  }
}
