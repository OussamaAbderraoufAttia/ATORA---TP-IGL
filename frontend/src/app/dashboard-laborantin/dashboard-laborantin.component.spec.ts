import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardLaborantinComponent } from './dashboard-laborantin.component';

describe('DashboardLaborantinComponent', () => {
  let component: DashboardLaborantinComponent;
  let fixture: ComponentFixture<DashboardLaborantinComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DashboardLaborantinComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DashboardLaborantinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
