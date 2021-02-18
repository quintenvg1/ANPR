import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChangeplateComponent } from './changeplate.component';

describe('ChangeplateComponent', () => {
  let component: ChangeplateComponent;
  let fixture: ComponentFixture<ChangeplateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChangeplateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChangeplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
