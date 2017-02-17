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

	getQuestionBySlug(questionSlug: string): Observable<Response>{
		let options = new RequestOptions({ headers: this.getCSRFToken() });
		return this.http.get(`${this.serverName}/api/question/${questionSlug}/`, options)
						.map((response: Response) => response.json());	
	}

	getQuestionsByTag(questionTag: string): Array<Question>{
		return [];
	}

	sendVote(objectType: string, questionId: number, choice: string){
		let options = this.jwt();
		let data = {
			'content_type': objectType,
			'object_id': questionId,
			'choice': choice == 'up' && 'U' || 'D',
			'rating': 1
		}
		console.log(data);
		console.log(this.http);
		return this.http.post(`${this.serverName}/api/vote/`, data, options)
						.map((response: Response) => response.json());
	}
}
