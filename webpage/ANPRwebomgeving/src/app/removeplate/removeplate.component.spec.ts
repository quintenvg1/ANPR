import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoveplateComponent } from './removeplate.component';

describe('RemoveplateComponent', () => {
  let component: RemoveplateComponent;
  let fixture: ComponentFixture<RemoveplateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RemoveplateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RemoveplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
