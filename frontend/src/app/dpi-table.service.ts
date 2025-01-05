import { Injectable, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import axios from 'axios';
import { AuthInterceptor } from './auth.interceptor';

@Injectable({
  providedIn: 'root'
})
export class DpiTableService {
  private dpiUrl: string;
  private dpiUrl2: string;

  constructor(private http: HttpClient, @Inject('BACKEND_URL') private backendUrl: string) {
    this.dpiUrl = `${this.backendUrl}/newapi/dpis/`;
    this.dpiUrl2 = `${this.backendUrl}/newapi/dpi/`;
  }

  // Fetch all DPI records
  async getAllDpi(): Promise<any> {
    try {
      const response = await axios.get(this.dpiUrl, { withCredentials: true });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data;
      } else {
        throw error;
      }
    }
  }

  // Fetch a single DPI record by ID
  async getDpiById(id: number): Promise<any> {
    try {
      const response = await axios.get(`${this.dpiUrl2}${id}/`, {
        withCredentials: true,
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

  // Create a new DPI record
  async createDpi(dpiData: any): Promise<any> {
    try {
      const response = await axios.post(this.dpiUrl, dpiData, { withCredentials: true });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data;
      } else {
        throw error;
      }
    }
  }

  // Update an existing DPI record
  async updateDpi(id: number, dpiData: any): Promise<any> {
    try {
      const response = await axios.put(`${this.dpiUrl}${id}/`, dpiData, { withCredentials: true });
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data;
      } else {
        throw error;
      }
    }
  }

  // Delete a DPI record
  async deleteDpi(id: number): Promise<any> {
    try {
      const response = await axios.delete(`${this.dpiUrl}${id}/`, { withCredentials: true });
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