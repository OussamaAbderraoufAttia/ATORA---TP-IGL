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
   const username = (document.getElementById('username') as HTMLInputElement)?.value;
    const password = (document.getElementById('password')as HTMLInputElement)?.value;
    console.log(username);
    const response = await this.loginService.login(username, password);
    console.log('Login successful', response);
    if (response.user_data.user_type == 'admin') {
      this.router.navigate(['/admin/profile'], { state: { user: response.user_data } });
    } else if (response.user_data.user_type == 'patient') {
    this.router.navigate(['/patient'], { state: { user: response.user_data } });
    }
    
    
  }
}
