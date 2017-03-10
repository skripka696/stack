import { User } from './user.model';
import { Question } from './question.model';
import { Comment } from './commen.model';

export class Answer{
	public user: User
	public question: Question
	public title: string
	public content: string
	public vote: number
	public create_date: Date
	public comments?: Array<Comment>
	public id?: number

	constructor({user, question, title, content, vote, create_date, comments, id}){
		this.user = new User(user);
		this.question = question;
		this.title = title;
		this.content = content;
		this.vote = vote;
		if (create_date){
			this.create_date = new Date(create_date);
		}
		if (comments){
			this.comments = comments;
		}
		if (id){
			this.id = id;
		}
	}
}