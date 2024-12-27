import { Component } from '@angular/core';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css'],
})
export class AdminComponent {
  // Static admin data
  admin = {
    email: 'admin@example.com',
    phone: '+1 234 567 890',
    joinedDate: 'January 15, 2022',
    profilePicture: 'https://storage.googleapis.com/a1aa/image/nUGcHtlLyyZXPNGfShTygaqy50E9z8P3loTqaPIWQs8yMdfTA.jpg',
  };

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
