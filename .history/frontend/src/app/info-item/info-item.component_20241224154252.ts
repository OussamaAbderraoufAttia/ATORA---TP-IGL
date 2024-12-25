import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-info-item',
  templateUrl: './info-item.component.html',
  styleUrls: ['./info-item.component.css']
})
export class InfoItemComponent {
  @Input() icon!: string; // Use string for icon representation
  @Input() label!: string;
  @Input() value!: string;
}