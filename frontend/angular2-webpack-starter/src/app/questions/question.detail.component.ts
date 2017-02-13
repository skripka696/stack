import { Component, OnInit } from '@angular/core';
import { QuestionService } from '../models/question.service';
import { Question } from '../models/question.model';
import 'rxjs/add/operator/switchMap';
import { Router, ActivatedRoute, Params } from '@angular/router';

@Component({
	selector: 'question-detail',
	templateUrl: './question.detail.template.html',
	providers: [ QuestionService ]
})
export class QuestionDetailComponent implements OnInit{
	question: Question;

	constructor(private questionService: QuestionService,
				private route: ActivatedRoute){}

	ngOnInit(){
		this.route.params.switchMap((params: Params) => this.questionService.getQuestionByID(+params['id']))
      					 .subscribe(
      					 		value => {
      					 			this.question = new Question(value);
      					 			console.log(value);
  					 			},
      					 		error => error
      					 	);
	}
}