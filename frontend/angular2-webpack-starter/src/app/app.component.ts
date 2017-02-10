/*
 * Angular 2 decorators and services
 */
import {
  Component,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import { AppState } from './app.service';

/*
 * App Component
 * Top Level Component
 */
@Component({
  selector: 'app',
  encapsulation: ViewEncapsulation.None,
  styleUrls: [
    './app.component.css'
  ],
  template: `    
    <div class="container">
      <nav>       
        <a [routerLink]=" ['./home'] " routerLinkActive="active">
          Home
        </a>
        <a [routerLink]=" ['./login'] " routerLinkActive="active">
          Login
        </a>     
        <a [routerLink]=" ['./registration'] " routerLinkActive="active">
          Registration
        </a> 
      </nav>

      <main>
        <router-outlet></router-outlet>        
      </main>
    </div>

    <footer class="footer">
      <div class="container">
        <p>@OurStackoverflow 2017</p>
      </div>
    </footer>
  `
})
export class AppComponent implements OnInit {
  public angularclassLogo = 'assets/img/angularclass-avatar.png';
  public name = 'Angular 2 Webpack Starter';
  public url = 'https://twitter.com/AngularClass';

  constructor(
    public appState: AppState
  ) {}

  public ngOnInit() {
    console.log('Initial App State', this.appState.state);
  }

}

/*
 * Please review the https://github.com/AngularClass/angular2-examples/ repo for
 * more angular app examples that you may copy/paste
 * (The examples may not be updated as quickly. Please open an issue on github for us to update it)
 * For help or questions please contact us at @AngularClass on twitter
 * or our chat on Slack at https://AngularClass.com/slack-join
 */
