import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LogincomponentComponent } from './logincomponent/logincomponent.component';
import { RemoveplateComponent } from './removeplate/removeplate.component';

const routes: Routes = [
  { path: 'remove', component: RemoveplateComponent },
  { path: 'login', component: LogincomponentComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
