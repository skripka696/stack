import { Injectable } from '@angular/core';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class CommonService{
	serverName: string = 'http://172.16.205.7';
	// serverName: string = 'http://stackoverflow.loc';
	constructor(){}

	public jwt(): RequestOptions{
		// create authorization header with jwt token
        let currentUser = JSON.parse(localStorage.getItem('currentUser'));
        if (currentUser && currentUser.token) {
            let headers = new Headers({ 'Authorization': 'Token ' + currentUser.token });
            return new RequestOptions({ headers: headers });
        }
	}

	public getCookie(name) {
	    let value = "; " + document.cookie;
	    let parts = value.split("; " + name + "=");
	    if (parts.length == 2)
	      return parts.pop().split(";").shift();
	}

	public getCSRFToken(){
		return new Headers({
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCookie('csrftoken')
        });
	}
}