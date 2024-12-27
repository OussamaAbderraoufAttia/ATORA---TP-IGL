import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PatientComponent } from './patient/patient.component';
import { AdminComponent } from './admin/admin.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    {path:'patient', component:PatientComponent},
    {path:'admin/profile', component: AdminComponent},
    { path: '', redirectTo: '/login', pathMatch: 'full' },
   
];
