import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoveAccComponent } from './remove-acc.component';

describe('RemoveAccComponent', () => {
  let component: RemoveAccComponent;
  let fixture: ComponentFixture<RemoveAccComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RemoveAccComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RemoveAccComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
