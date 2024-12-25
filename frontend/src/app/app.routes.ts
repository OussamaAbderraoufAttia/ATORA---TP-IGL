import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { PatientComponent } from './patient/patient.component';

export const routes: Routes = [
    { path: 'login', component: LoginComponent },
    {path:'patient', component:PatientComponent}
];
