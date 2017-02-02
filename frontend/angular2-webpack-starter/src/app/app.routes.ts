import { Routes } from '@angular/router';
import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { RegistrationComponent } from './registration';
import { NoContentComponent } from './no-content';

import { DataResolver } from './app.resolver';

export const ROUTES: Routes = [
  { path: '',      component: HomeComponent },
  { path: 'home',  component: HomeComponent },
  { path: 'login',  component: LoginComponent },
  { path: 'registration',  component: RegistrationComponent },
  { path: '**',    component: NoContentComponent },
];
