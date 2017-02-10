import { User } from './user.model';

export class Question{
	public user: User
	public title: string
	public content: string
	public vote: number

	constructor({user, title, content, vote}){
		this.user = user;
		this.title = title;
		this.content = content;
		this.vote = vote;
	}
}