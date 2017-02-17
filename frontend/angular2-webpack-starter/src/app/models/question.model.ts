import { User } from './user.model';

export class Question{
	public user: string
	public title: string
	public content: string
	public vote: number
	public slug: string
	public id?: number
	public tag?: Array<string>

	constructor({user, title, content, vote, slug, id, tag}){
		this.user = user;
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
	}
}