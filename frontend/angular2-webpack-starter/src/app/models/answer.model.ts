import { User } from './user.model';
import { Question } from './question.model';
import { Comment } from './comment.model';

export class Answer{
	public user: User;
	public question: Question;
	public title: string;
	public content: string;
	public vote: number;
	public create_date: Date;
	public comments: Array<Comment> = [];
	public id: number;

	constructor({user, question, title, content, vote, create_date, comment, id}){
		this.user = new User(user);
		this.question = question;
		this.title = title;
		this.content = content;
		this.vote = vote;
		if (create_date){
			this.create_date = new Date(create_date);
		}
		if (comment){
      for (let current_comment of comment){
				this.comments.push(new Comment(current_comment));
			}
		}
		if (id){
			this.id = id;
		}
	}
}
