import { Routes } from '@angular/router';
import { HomeComponent } from './home';
import { LoginComponent } from './login';
import { QuestionsComponent, QuestionDetailComponent } from './questions';
import { RegistrationComponent } from './registration';
import { NoContentComponent } from './no-content';

import { DataResolver } from './app.resolver';

export const ROUTES: Routes = [
  { path: '',      component: HomeComponent },
  { path: 'home',  component: HomeComponent },
  { path: 'login',  component: LoginComponent },
  { path: 'question/:slug',  component: QuestionDetailComponent },
  { path: 'questions',  component: QuestionsComponent},
  { path: 'registration',  component: RegistrationComponent },
  { path: '**',    component: NoContentComponent },
];
