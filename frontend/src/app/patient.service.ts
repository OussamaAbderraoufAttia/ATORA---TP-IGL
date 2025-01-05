import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import axios from 'axios';

@Injectable({
  providedIn: 'root',
})
export class PatientService {
  private apiUrl = 'http://127.0.0.1:8000/newapi/'; // Replace with your actual API URL

  constructor() {}

  async addConsultation(consultation: any): Promise<any> {
    try {
      const response = await axios.post(`${this.apiUrl}consultations/add/`, consultation, {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
      });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data;
      } else {
        throw error;
      }
    }
  }
  
}
