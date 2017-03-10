import { User } from './user.model';

export class Comment{
	public user: User;
	public like: number;
	public create_date?: Date;
	public description: string;
	public object_id: number;
	public content_type: string;

	constructor({description, object_id, content_type, like, create_date, user}){
    this.user = new User(user);
		if (like){
			this.like = like;
		}else{
			this.like = 0;
		}
		if (create_date){
			this.create_date = new Date(create_date);
		}else{
			this.create_date = new Date();
		}
		this.description = description;
		this.object_id = object_id;
		this.content_type = content_type;
	}
}
