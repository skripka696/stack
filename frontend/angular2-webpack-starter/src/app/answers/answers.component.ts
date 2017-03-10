import { Component, Input, OnInit } from '@angular/core';
import { Answer } from '../models/answer.model';
import { AnswerService } from '../models/answer.service';
import { UserService } from '../models/user.service';

@Component({
	selector: 'answers',
	styleUrls: ['./answers.style.css'],
	templateUrl: './answers.component.template.html',
	providers: [ AnswerService, UserService ]
})
export class AnswersComponent implements OnInit{
	@Input() answers;
	@Input() parent;

	constructor(private userService: UserService){}

	ngOnInit(){}

	getFullAuthorName(user: any): string{
		return this.userService.getFullName(user);
	}

	getCorrectDate(answer: Answer): string{
		return answer.create_date.getHours() + ":" + answer.create_date.getMinutes() ;
	}

	sendAnswerVote(vote: string, answer: Answer){
		console.log(vote);
		console.log(answer);
	}
}