import {
	Component,
	Input,
	OnInit
} from '@angular/core';
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

	constructor(private userService: UserService,
              private answerService: AnswerService){}

	ngOnInit(){}

	getFullAuthorName(user: any): string{
		return this.userService.getFullName(user);
	}

	getCorrectDate(answer: Answer): string{
		return answer.create_date.getHours() + ":" + answer.create_date.getMinutes() ;
	}

  updateAnswer(value: Object, answer: Answer){
    let changed_answer = this.answers.filter(function(value){
      return value.id == answer.id;
    });
    for (let key of Object.keys(value)){
      if (answer.hasOwnProperty(key)){
        changed_answer[0][key] = value[key];
      }
    }

  }

	sendAnswerVote(vote: string, answer: Answer){
		console.log(vote);
		console.log(answer);
    this.answerService.sendVote(vote, answer)
                      .subscribe(
                        value => this.updateAnswer(value, answer),
                        error => console.log(error)
                      )
	}
}
