import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-medecin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css'],
})
export class AdminComponent implements OnInit {
  user: any;
  admin: any = {};
  constructor(private router: Router) {}

  ngOnInit() {
    // Retrieve the user data from the router state
    this.user = history.state.user;
    this.admin = {
      email: this.user.email,
      phone: this.user.telephone,
      joinedDate: this.user.date_creation,
      profilePicture: 'https://storage.googleapis.com/a1aa/image/nUGcHtlLyyZXPNGfShTygaqy50E9z8P3loTqaPIWQs8yMdfTA.jpg',
    };
  }
  // Static admin data
  

  handleInputChange(event: Event) {
    const target = event.target as HTMLInputElement;
    const name = target.name;
    const value = target.value;

    // Update admin object
    (this.admin as any)[name] = value;
  }

  handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement;
    if (target.files && target.files[0]) {
      const file = target.files[0];
      const reader = new FileReader();

      reader.onload = (e: ProgressEvent<FileReader>) => {
        if (e.target && typeof e.target.result === 'string') {
          this.admin.profilePicture = e.target.result; // Update picture
        }
      };

      reader.readAsDataURL(file);
    }
  }

  handleSubmit(event: Event) {
    event.preventDefault();
    console.log('Updated admin data:', this.admin);
    alert('Profile updated successfully!');
  }
}
