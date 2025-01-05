import { Component, AfterViewInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-landing',
  templateUrl: './landing.component.html',
  styleUrls: ['./landing.component.css']
})
export class LandingComponent implements AfterViewInit {

  constructor(private route: ActivatedRoute,private router: Router) {}

  ngAfterViewInit(): void {
    // Vérifier s'il y a une ancre dans l'URL après le chargement de la vue
    this.route.fragment.subscribe(fragment => {
      if (fragment) {
        const element = document.getElementById(fragment);
        if (element) {
          element.scrollIntoView({ behavior: 'smooth' });
        }
      }
    });
  }
  navigateToLogin() {
    this.router.navigate(['/login']);
  }
}
