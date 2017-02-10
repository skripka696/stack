import { Injectable } from '@angular/core';
import { Question } from './question.model';
import { Http, Headers, RequestOptions, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { CommonService } from './common.service';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class QuestionService extends CommonService{
	question: Question;

	// serverName: string = 'http://172.16.205.7';
	serverName: string = 'http://stackoverflow.loc';

	constructor(){
		super();
	}

	getAllQuestions(): Observable<Response>{
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.get(`${this.serverName}/api/question/`, options)
						.map((response: Response) => response.json());
	}

}
