import { CanActivateFn } from '@angular/router';

export const dashboardsGuard: CanActivateFn = (route, state) => {
  const role = localStorage.getItem('role');
  return (role === 'admin' || role === 'medecin' ); // or any other condition based on your requirements
};
