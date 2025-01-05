import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RadiologueDashboardComponent } from './radiologue-dashboard.component';

describe('RadiologueDashboardComponent', () => {
  let component: RadiologueDashboardComponent;
  let fixture: ComponentFixture<RadiologueDashboardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RadiologueDashboardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RadiologueDashboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
