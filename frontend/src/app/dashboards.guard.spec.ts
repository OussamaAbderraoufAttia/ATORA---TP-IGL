import { TestBed } from '@angular/core/testing';
import { CanActivateFn } from '@angular/router';

import { dashboardsGuard } from './dashboards.guard';

describe('dashboardsGuard', () => {
  const executeGuard: CanActivateFn = (...guardParameters) => 
      TestBed.runInInjectionContext(() => dashboardsGuard(...guardParameters));

  beforeEach(() => {
    TestBed.configureTestingModule({});
  });

  it('should be created', () => {
    expect(executeGuard).toBeTruthy();
  });
});
