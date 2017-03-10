import { User } from './user.model';
import { Answer } from './answer.model';
import { Comment } from './comment.model';

export class Question{
	public user: User;
	public title: string;
	public content: string;
	public vote: number;
	public slug: string;
	public id: number;
	public tag: Array<string>;
	public create_date: Date;
	public answers: Array<Answer> = [];
	public comments: Array<Comment> = [];

	constructor({user, title, content, vote, slug, id, tag, create_date, answers, comment}){
		this.user = new User(user);
		this.title = title;
		this.content = content;
		this.vote = vote;
		this.slug = slug;
		if (id){
			this.id = id;
		}
		if (tag){
			this.tag = tag;
		}
		if(create_date){
			this.create_date = new Date(create_date);
		}
		if(answers){
			for (let answer of answers){
				this.answers.push(new Answer(answer));
			}
		}
		if(comment){
			for (let current_comment of comment){
				this.comments.push(new Comment(current_comment));
			}
		}
	}
}
