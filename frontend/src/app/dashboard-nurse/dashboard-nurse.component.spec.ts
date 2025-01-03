import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DashboardNurseComponent } from './dashboard-nurse.component';

describe('DashboardNurseComponent', () => {
  let component: DashboardNurseComponent;
  let fixture: ComponentFixture<DashboardNurseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DashboardNurseComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DashboardNurseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
