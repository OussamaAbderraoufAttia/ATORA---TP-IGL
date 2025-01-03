import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PatientComponent } from './patient/patient.component';
import { AdminComponent } from './admin/admin.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { authGuard } from './auth.guard';
import { LandingComponent } from './landing/landing.component';
import { DashboardNurseComponent } from './dashboard-nurse/dashboard-nurse.component';
import { RadiologueDashboardComponent } from './radiologue-dashboard/radiologue-dashboard.component';
import { DashboardLaborantinComponent } from './dashboard-laborantin/dashboard-laborantin.component';
import { dashboardsGuard } from './dashboards.guard';

export const routes: Routes = [
    { path: 'landing', component: LandingComponent },
    { path: 'login', component: LoginComponent },
    {path:'patient', component:PatientComponent, canActivate: [authGuard]},
    {path:'profile', component: AdminComponent, canActivate: [authGuard]},
    { path: '', redirectTo: 'login', pathMatch: 'full' },
    {path:'dashboard-medecin', component:DashboardComponent, canActivate: [authGuard,dashboardsGuard]},
    {path:'nurse-dashboard', component:DashboardNurseComponent, canActivate: [authGuard]},
    {path:'radiologue-dashboard', component:RadiologueDashboardComponent, canActivate: [authGuard]},
    {path:'laborantin-dashboard', component:DashboardLaborantinComponent, canActivate: [authGuard]},
    {path:'**', redirectTo: 'landing'}

   
];
