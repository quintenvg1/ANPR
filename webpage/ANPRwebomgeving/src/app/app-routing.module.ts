import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ChangeplateComponent } from './changeplate/changeplate.component';
import { CreateaccountComponent } from './createaccount/createaccount.component';
import { LogincomponentComponent } from './logincomponent/logincomponent.component';
import { RemoveAccComponent } from './remove-acc/remove-acc.component';
import { RemoveplateComponent } from './removeplate/removeplate.component';

const routes: Routes = [
  { path: 'remove', component: RemoveplateComponent },
  { path: 'login', component: LogincomponentComponent },
  { path: "remove_acc", component: RemoveAccComponent },
  { path: "", component: LogincomponentComponent },
  { path: "change", component: ChangeplateComponent },
  { path: "signup", component: CreateaccountComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
