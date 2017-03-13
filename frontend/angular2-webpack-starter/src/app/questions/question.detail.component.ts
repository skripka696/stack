import { Component, OnInit } from '@angular/core';
import { QuestionService } from '../models/question.service';
import { Question } from '../models/question.model';
import { User } from '../models/user.model';
import { UserService } from '../models/user.service';
import { Answer } from '../models/answer.model';
import { AnswerService } from '../models/answer.service';
import 'rxjs/add/operator/switchMap';
import { Router, ActivatedRoute, Params } from '@angular/router';

@Component({
	selector: 'question-detail',
	templateUrl: './question.detail.template.html',
	styleUrls: ['./question.detail.style.css'],
	providers: [ QuestionService, UserService ]
})
export class QuestionDetailComponent implements OnInit{
	question? : Question;

	constructor(private questionService: QuestionService,
				private userService: UserService,
				private route: ActivatedRoute){}

	updateQuestion(value: any){
    for (let key of Object.keys(value)){
      if (this.question.hasOwnProperty(key)){
        this.question[key] = value[key];
      }
    }
	}

	getQuestionData(){
		this.route.params.switchMap((params: Params) => this.questionService.getQuestionBySlug(params['slug']))
      					 .subscribe(
      					 		value => {
      					 			this.question = new Question(value);
      					 		},
      					 		error => error
      					 	);
	}

	ngOnInit(){
		this.getQuestionData();
	}

	sendVote(vote: string){
		this.questionService.sendVote('question', this.question.id, vote)
							.subscribe(
								value => {
									this.updateQuestion(value);
								},
								error => error
							);
	}

	getCorrectDate(question: Question): string{
		return question.create_date.getHours() + ":" + question.create_date.getMinutes() ;
	}

	getFullAuthorName(user: any): string{
		return this.userService.getFullName(user);
	}
}
