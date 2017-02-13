import { User } from './user.model';

export class Question{
	public username: string
	public title: string
	public content: string
	public vote: number
	public id?: number

	constructor({username, title, content, vote, id}){
		this.username = username;
		this.title = title;
		this.content = content;
		this.vote = vote;
		if (id){
			this.id = id;
		}
	}
}