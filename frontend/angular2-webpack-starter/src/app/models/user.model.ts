export class User{
	public first_name: string;
	public last_name: string;
	public email: string;
	public username: string;
	public password: string;
	public id?: number;

	constructor({first_name, last_name, email, username, password, id}){
		this.first_name = first_name;
		this.last_name = last_name;
		this.email = email;
		this.username = username;
		this.password = password;
		if (id){
			this.id = id;
		}
	}
}