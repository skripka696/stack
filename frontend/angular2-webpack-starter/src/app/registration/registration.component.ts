import {
  Component,
  OnInit,
} from '@angular/core';
import { UserService } from '../models/user.service';
import { User } from '../models/user.model';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
	selector: 'registration-form',
	styleUrls: ['./registration.style.css'], 
	templateUrl: './registration.component.html',
	providers: [UserService]
})
export class RegistrationComponent implements OnInit{
	userForRegistration?: User;

	first_name = new FormControl('');
	last_name = new FormControl('');
	email = new FormControl('', [Validators.required, Validators.pattern('[a-zA-Z0-9]+@[a-zA-Z]+.[a-zA-Z]+')]);
	username = new FormControl('', Validators.required);
	password = new FormControl('', [Validators.required, Validators.minLength(8)]);
	
	registrationForm: FormGroup;

	formErrors = {
		'first_name': '',
		'last_name': '',
		'email': '',
		'username': '',
		'password': ''
	};

	validationMessages = {
		'email': {
			'required': 'This field is required',
			'pattern': 'This field should be in correct format'
		},
		'username': {
			'required': 'This field is required',
		},
		'password': {
			'required': 'This field is required',
			'minlength': 'Must be at least 8 characters'			
		}
	};

	constructor(private formBuilder: FormBuilder, 
				private userService: UserService){}

	public ngOnInit(){
    	this.buildRegistrationForm();
	}

	onSubmit(userForm: FormGroup){
		this.userForRegistration = new User(userForm.value);
		const result = this.userService.createNewUser(this.userForRegistration);
		console.log(result);
	}

	onValueChanged(data?: any) {
		if (!this.registrationForm) { return; }
		const form = this.registrationForm;
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

	buildRegistrationForm(): void{
		this.registrationForm = this.formBuilder.group({
		 	first_name: this.first_name,
		    last_name: this.last_name,
		    email: this.email,
		    username: this.username,
		    password: this.password,
	    });

	    this.registrationForm.valueChanges
      		.subscribe(data => this.onValueChanged(data));

  		this.onValueChanged();
	}
}