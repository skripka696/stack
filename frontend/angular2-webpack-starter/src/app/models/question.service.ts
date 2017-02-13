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

	constructor(private http: Http){
		super();
	}

	getAllQuestions(): Observable<Response>{
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.get(`${this.serverName}/api/question/`, options)
						.map((response: Response) => response.json());
	}

	getQuestionByID(questionId: number): Observable<Response>{
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.get(`${this.serverName}/api/question/${questionId}/`, options)
						.map((response: Response) => response.json());	
	}

}
