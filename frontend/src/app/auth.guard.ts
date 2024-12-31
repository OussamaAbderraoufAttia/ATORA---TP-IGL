import { CanActivateFn, Router } from '@angular/router';
import { inject } from '@angular/core';
import { LoginService } from './login.service';

export const authGuard: CanActivateFn = (route, state) => {
  const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
  const router = inject(Router);
  if (!isLoggedIn) {
    // If not logged in, redirect to login page
    router.navigate(['/login']);
    return false;
  }
  return true;
};