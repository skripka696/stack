import { Injectable } from '@angular/core';
import { CommonService } from './common.service';
import { Answer } from './answer.model';
import { 
	Http, 
	Headers, 
	RequestOptions, 
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
}