import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../login.service';
import { delay } from 'rxjs';




@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  imports: []
})
export class LoginComponent {
  

  constructor(private router: Router, private loginService: LoginService) {
   
  }

  async onSubmit() {
   const email = (document.getElementById('username') as HTMLInputElement)?.value;
    const password = (document.getElementById('password')as HTMLInputElement)?.value;
    const response = await this.loginService.login(email,password);
    console.log('Login successful', response);
    localStorage.setItem('isLoggedIn', 'true');
    if (localStorage.getItem('role') == 'admin') {
      this.router.navigate(['/profile'], { state: { user: response.user_data } });
    } else if (localStorage.getItem('role') == 'patient') {
    this.router.navigate(['/patient'], { state: { user: response.user_data } });
    }
    
    
  }
}
