import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-info-item',
  templateUrl: './info-item.component.html',
  styleUrls: ['./info-item.component.css']
})
export class InfoItemComponent {
  @Input() icon!: string; // Ensure this is defined
  @Input() label!: string; // Ensure this is defined
  @Input() value!: string; // Ensure this is defined
}