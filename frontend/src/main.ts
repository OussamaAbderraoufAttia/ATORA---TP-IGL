// filepath: /C:/Users/ramymou/Desktop/simpleForm/ATORA---TP-IGL/frontend/src/main.ts
import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideRouter } from '@angular/router';
import { routes } from './app/app.routes';
import { provideHttpClient, withInterceptors } from '@angular/common/http';

const BACKEND_URL = 'http://127.0.0.1:8000'; // Django development server URL

// CSRF Interceptor
import { HttpInterceptorFn } from '@angular/common/http';

const csrfInterceptor: HttpInterceptorFn = (req, next) => {
  const csrfToken = getCookie('csrftoken');
  if (csrfToken) {
    req = req.clone({
      setHeaders: {
        'X-CSRFToken': csrfToken
      }
    });
  }
  return next(req);
};

function getCookie(name: string): string | null {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) {
    const cookieValue = parts.pop();
    if (cookieValue) {
      return cookieValue.split(';').shift() || null;
    }
  }
  return null;
}

bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideHttpClient(),
    provideHttpClient(withInterceptors([csrfInterceptor])),
    { provide: 'BACKEND_URL', useValue: BACKEND_URL }
  ]
}).catch((err) => console.error(err));