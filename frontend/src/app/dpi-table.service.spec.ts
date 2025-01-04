import { TestBed } from '@angular/core/testing';

import { DpiTableService } from './dpi-table.service';

describe('DpiTableService', () => {
  let service: DpiTableService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DpiTableService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
