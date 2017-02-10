import { Injectable } from '@angular/core';
import { User } from './user.model';
import { Http, RequestOptions, Response } from '@angular/http';
import { CommonService } from './common.service';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class UserService extends CommonService{
	user: User;
    options: RequestOptions;

	constructor(){
		super();
		this.options 
	}	

	createNewUser(newUser: User): Observable<Response>{
        let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.post(`${this.serverName}/api/users/`, newUser, options)
							.map((response: Response) => response);
	}

	loginUser(user: User){
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.post(`${this.serverName}/api-token-auth/`, JSON.stringify(user), options)
							 .map((response: Response) => response.json());
	}
}
