import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { QuestionService } from '../models/question.service';
import { Question } from '../models/question.model';

@Component({
	selector: 'all-questions',
	providers: [ QuestionService ],
	styleUrls: ['./questions.style.css'],
	templateUrl: './question.template.html'
})
export class QuestionsComponent implements OnInit{
	public allQuestions: Array<Question> = [];

	constructor(private questionService: QuestionService,
				private router: Router){}

	private getListOfQuestions(questions: any){
		this.allQuestions = questions;
	}

	public loadAllQuestions(){
		console.log('LOADING');
		let questions_tmp = this.questionService.getAllQuestions()
							.subscribe(
								value => {
									this.getListOfQuestions(value);
								},
								error => {
									console.log('ERROR');
									alert(error);
								}
						 	);
	 	console.log(questions_tmp);
 	} 	

	public ngOnInit(){
		this.loadAllQuestions();
	}

	public getAnswersLen(question: Question): number{
		return question.answers.length;
	}
}