import {Injectable} from '@angular/core';
import {User} from './user.model';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class UserService{
	user: User;

	constructor(private http: Http){}

	private jwt(): RequestOptions{
		// create authorization header with jwt token
        let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            let headers = new Headers({ 'Authorization': 'Bearer ' + currentUser.token });
            return new RequestOptions({ headers: headers });
        }
	}

	createNewUser(newUser: User): Observable<User>{
		console.log('New User');
		console.log(newUser);
		return this.http.post('/api/users', newUser, 
							this.jwt())
							.map((response: Response) => response.json())
							.catch((response: Response) => response.json());
	}
}