import {Injectable} from '@angular/core';
import {User} from './user.model';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class UserService{
	user: User;
	serverName: string = 'http://stackoverflow.loc';

	constructor(private http: Http){}

	private jwt(): RequestOptions{
		// create authorization header with jwt token
        let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            let headers = new Headers({ 'Authorization': 'Bearer ' + currentUser.token });
            return new RequestOptions({ headers: headers });
        }
	}

	getCookie(name) {
	    let value = "; " + document.cookie;
	    let parts = value.split("; " + name + "=");
	    if (parts.length == 2) 
	      return parts.pop().split(";").shift();
	}

	createNewUser(newUser: User): Observable<User>{
		console.log('New User');
		console.log(newUser);
		let headers = new Headers({
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken')
        });

        let options = new RequestOptions({ headers: headers });
		return this.http.post(`${this.serverName}/api/users`, newUser, 
							options)
							.map((response: Response) => response.json())
							.catch((response: Response) => response.json());
	}
}