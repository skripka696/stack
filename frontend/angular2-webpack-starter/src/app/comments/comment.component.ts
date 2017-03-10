import { 
	Component,
	Input, 
	OnInit,
	trigger,
	state,
	style,
	transition,
	animate
} from '@angular/core';
import {
	FormControl,
	FormBuilder,
	FormGroup,
	Validators
} from '@angular/forms';
import { Comment } from '../models/comment.model';
import { CommentService } from '../models/comment.service';
import { UserService } from '../models/user.service';

@Component({
	selector: 'comments',
	styleUrls: ['./comment.style.css'],
	templateUrl: './comment.component.template.html',
	animations: [
		trigger('hideForm', [
			state('hide', style({transform: 'translateX(-200%)'})),
			state('show', style({transform: 'translateX(0)'})),
		    transition('show => hide', [
		      animate(250, style({transform: 'translateX(100%)'}))
		    ]),
		    transition('hide => show', [
		      animate(250, style({transform: 'translateX(-100%)'}))
		    ])
  		])
	],
	providers: [ CommentService, UserService ]
})
export class CommentComponent implements OnInit{
	@Input() comments;
	@Input() parent;

	commentDescription = new FormControl('');

	commentForm: FormGroup;
	hideForm: string = 'hide';
	hideButton: Boolean = false;

	constructor(private userService: UserService,
				private commentService: CommentService,
				private formBuilder: FormBuilder){}

	buildCommentForm(): void{
		this.commentForm = this.formBuilder.group({
			description: this.commentDescription
		});
	}

	ngOnInit(){
		this.buildCommentForm();
	}

	getFullAuthorName(user: any): string{
		return this.userService.getFullName(user);
	}

	getCorrectDate(comment: Comment): string{
		return comment.create_date.toLocaleDateString();
	}

	openForm(){
		if (this.hideForm == 'show'){
			this.hideForm = 'hide';
		}else{
			this.hideForm = 'show';
		}
		// this.hideButton = true;
	}

	sendComment(){
		let data = {
			'description': '',
			'object_id': this.parent.id,
			'content_type': this.parent.constructor.name.toLowerCase()
		}
		console.log(data);
		// this.commentService.createNewComment(data)
		// 					.subscribe(
		// 						value => console.log(value),
		// 						error => console.log(error)
		// 					);
	}
}