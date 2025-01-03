import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PatientComponent } from './patient/patient.component';
import { AdminComponent } from './admin/admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LandingComponent } from './landing/landing.component';
import { DashboardNurseComponent } from './dashboard-nurse/dashboard-nurse.component';
import { RadiologueDashboardComponent } from './radiologue-dashboard/radiologue-dashboard.component';
import { DashboardLaborantinComponent } from './dashboard-laborantin/dashboard-laborantin.component';

export const routes: Routes = [
    { path: 'landing', component: LandingComponent },
    { path: 'login', component: LoginComponent },
    { path: 'patient', component: PatientComponent }, // authGuard removed
    { path: 'profile', component: AdminComponent },  // authGuard removed
    { path: '', redirectTo: 'laborantin-dashboard', pathMatch: 'full' },
    { path: 'dashboard-medecin', component: DashboardComponent }, // authGuard removed
    { path: 'nurse-dashboard', component: DashboardNurseComponent }, // authGuard removed
    { path: 'radiologue-dashboard', component: RadiologueDashboardComponent }, // authGuard removed
    { path: 'laborantin-dashboard', component: DashboardLaborantinComponent }, // authGuard removed
    { path: '**', redirectTo: 'laborantin-dashboard' }
];