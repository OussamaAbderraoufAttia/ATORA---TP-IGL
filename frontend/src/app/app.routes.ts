import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PatientComponent } from './patient/patient.component';
import { AdminComponent } from './admin/admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    {path:'patient', component:PatientComponent, canActivate: [authGuard]},
    {path:'admin/profile', component: AdminComponent, canActivate: [authGuard]},
    { path: '', redirectTo: '/login', pathMatch: 'full' },
    {path:'dpi/dashboard', component:DashboardComponent, canActivate: [authGuard]}
   
];
