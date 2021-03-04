import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MongodisplayComponent } from './mongodisplay.component';

describe('MongodisplayComponent', () => {
  let component: MongodisplayComponent;
  let fixture: ComponentFixture<MongodisplayComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MongodisplayComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MongodisplayComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
