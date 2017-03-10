import { Injectable } from '@angular/core';
import { Comment } from './comment.model';
import { CommonService } from './common.service';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';


@Injectable()
export class CommentService extends CommonService{
	comment: Comment;

	constructor(private http: Http){
		super();
	}

	createNewComment(data: any): Observable<Response>{
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.post(`${this.serverName}/api/comment/`, data, options)
						.map((response: Response) => response.json());
	}
}