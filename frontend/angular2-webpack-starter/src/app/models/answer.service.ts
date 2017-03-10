import { Injectable } from '@angular/core';
import { CommonService } from './common.service';
import { Answer } from './answer.model';
import {
	Http,
	Response
} from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';

@Injectable()
export class AnswerService extends CommonService{
	answer: Answer;

	constructor(private http: Http){
		super();
	}

  sendVote(choice: string, answer: Answer): Observable<Response>{
    let options = this.jwt();
    let data = {
      'choice': choice == 'up' && 'U' || 'D',
      'content_type': 'answer',
      'object_id': answer.id,
      'rating': 1,
      'update_at': new Date()
    };
    return this.http.post(`${this.serverName}/api/vote/`, data, options)
                    .map((response: Response) => response.json());
  }
}
