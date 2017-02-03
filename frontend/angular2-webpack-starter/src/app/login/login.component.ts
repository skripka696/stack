import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormBuilder, Validators } from '@angular/forms';
import { UserService } from '../models/user.service';
import { User } from '../models/user.model';

@Component({
	selector: 'login-form',
	templateUrl: './login.component.html',
	providers: [UserService]
})
export class LoginComponent implements OnInit{
	user?: null;

	username = new FormControl('', [Validators.required]);
	password = new FormControl('', [Validators.required, Validators.minLength(2)]);

	loginForm: FormGroup;

	formErrors = {
		'username': '',
		'password': ''
	}

	validationMessages = {
		'username': {
			'required': 'This field is required',
		},
		'password': {
			'required': "This field is required",
			'minlength': "Must be at least 8 characters"			
		}
	}

	constructor(private userService: UserService,
				private formBuilder: FormBuilder){}

	onValueChanged(data?: any){
		if (!this.loginForm) { return; }
		const form = this.loginForm;
	  	for (const field in this.formErrors) {
	    	this.formErrors[field] = '';
	    	const control = form.get(field);
		    if (control && control.touched && !control.valid) {
		        const messages = this.validationMessages[field];
		    	for (const key in control.errors) {
		        	this.formErrors[field] += messages[key] + ' ';
		      	}
		    }
	  	}
	}

	buildForm(){
		this.loginForm = this.formBuilder.group({
			username: this.username,
			password: this.password
		});

		this.loginForm.valueChanges
      		.subscribe(data => this.onValueChanged(data));

  		this.onValueChanged();
	}	

	ngOnInit(){
		this.buildForm();
	}

	onSubmit(form: any){
		this.userService.loginUser(form.value)
						.subscribe(
							value => localStorage.setItem('currentUser', value['token']),
							error => console.log(error)
						);
	}
}