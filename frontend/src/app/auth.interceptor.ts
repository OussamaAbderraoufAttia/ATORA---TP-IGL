// filepath: /src/app/auth.interceptor.ts
import { Injectable } from '@angular/core';
import { HttpEvent, HttpInterceptor, HttpHandler, HttpRequest, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import axios from 'axios';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const accessToken = localStorage.getItem('access_token');
    const refreshToken = localStorage.getItem('refresh_token');

    if (accessToken) {
      req = req.clone({
        setHeaders: {
          Authorization: `Bearer ${accessToken}`
        }
      });
    }

    return next.handle(req).pipe(
      catchError((error: HttpErrorResponse) => {
        if (error.status === 401 && refreshToken) {
          // Token expired, try to refresh it
          return this.refreshToken(refreshToken).pipe(
            switchMap((newToken: string) => {
              localStorage.setItem('access_token', newToken);
              req = req.clone({
                setHeaders: {
                  Authorization: `Bearer ${newToken}`
                }
              });
              return next.handle(req);
            }),
            catchError((refreshError) => {
              // Refresh token failed, handle accordingly
              return throwError(refreshError);
            })
          );
        } else {
          return throwError(error);
        }
      })
    );
  }

  private refreshToken(refreshToken: string): Observable<string> {
    return new Observable<string>((observer) => {
      axios.post('http://127.0.0.1:8000/myapi/token/refresh/', { refresh: refreshToken })
        .then(response => {
          observer.next(response.data.access);
          console.log('Token refreshed:', response.data.access);
          observer.complete();
        })
        .catch(error => {
          observer.error(error);
        });
    });
  }
}