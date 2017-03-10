export class User{
	public first_name: string;
	public last_name: string;
	public email: string;
	public username: string;
	public password: string;
	public avatar_url: string;
	public id?: number;

	constructor({first_name, last_name, email, username, password, avatar_url, id}){
		this.first_name = first_name;
		this.last_name = last_name;
		this.email = email;
		this.username = username;
		this.password = password;
		if (avatar_url){
			this.avatar_url = avatar_url;
		}else{
			this.avatar_url = './assets/img/user_image.jpg';
		}
		if (id){
			this.id = id;
		}
	}
}