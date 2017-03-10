import { User } from './user.model';

export class Comment{
	public user: User
	public like: number
	public create_date: Date
	public description: string
	public object_id: number
	public content_type: string

	constructor({user, like, create_date, description, object_id, content_type}){
		this.user = new User(user);
		this.like = like;
		this.create_date = new Date(create_date);
		this.description = description;
		this.object_id = object_id;
		this.content_type = content_type;
	}
}