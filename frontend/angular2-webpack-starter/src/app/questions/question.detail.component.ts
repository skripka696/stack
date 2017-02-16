import { Component, OnInit } from '@angular/core';
import { QuestionService } from '../models/question.service';
import { Question } from '../models/question.model';
import 'rxjs/add/operator/switchMap';
import { Router, ActivatedRoute, Params } from '@angular/router';

@Component({
	selector: 'question-detail',
	templateUrl: './question.detail.template.html',
	styleUrls: ['./question.detail.style.css'],
	providers: [ QuestionService ]
})
export class QuestionDetailComponent implements OnInit{
	question? : Question;

	constructor(private questionService: QuestionService,
				private route: ActivatedRoute){}

	ngOnInit(){
		this.route.params.switchMap((params: Params) => this.questionService.getQuestionBySlug(params['slug']))
      					 .subscribe(
      					 		value => {
      					 			this.question = new Question(value);
  					 			},
      					 		error => error
      					 	);
	}

	sendVote(vote: string){
		console.log(vote);
		console.log(vote == 'up');
		console.log(this.question.id);
		this.questionService.sendVote('question', this.question.id, vote)
							.subscribe(
								value => {
									console.log(value);
									// this.question.vote = value;
								},
								error => error
							);
	}
}