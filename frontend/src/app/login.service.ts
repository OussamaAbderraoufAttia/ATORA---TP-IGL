// filepath: /C:/Users/ramymou/Desktop/simpleForm/ATORA---TP-IGL/frontend/src/app/login.service.ts
import { Injectable, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import axios from 'axios';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  private loginUrl: string;
  private logoutUrl: string;

  constructor(private http: HttpClient, @Inject('BACKEND_URL') private backendUrl: string) {
    this.loginUrl = `${this.backendUrl}/myapi/login/`;
    this.logoutUrl = `${this.backendUrl}/api/logout/`;
  }

  async login(credentials: string, auth_key: string): Promise<any> {
    try {
      const response = await axios.post(this.loginUrl, { credentials , auth_key }, { withCredentials: true });
      const data = response.data;

      // Store tokens in local storage
      localStorage.setItem('access_token', data.access_token);
      localStorage.setItem('refresh_token', data.refresh_token);
      localStorage.setItem('role', data.role);

      return data;
    } catch (error) {
      if (axios.isAxiosError(error) && error.response) {
        throw error.response.data;
      } else {
        throw error;
      }
    }
  }

  async logout(): Promise<any> {
    try {
      const response = await axios.post(this.logoutUrl, {}, { withCredentials: true });
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