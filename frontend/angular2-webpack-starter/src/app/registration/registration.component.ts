import {
  Component,
  OnInit,
  ViewChild,
} from '@angular/core';
import { UserService } from '../models/user.service';
import { User } from '../models/user.model';

import { 
	FormBuilder, 
	FormControl, 
	FormGroup,
	Validators 
} from '@angular/forms';
import { Response } from '@angular/http';
import { ModalDialogContent } from '../modals';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
	selector: 'registration-form',
	styleUrls: ['./registration.style.css'], 
	templateUrl: './registration.component.html',
	providers: [ UserService ]
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
				private userService: UserService,
				private modalService: NgbModal){
	}

	public ngOnInit(){
    	this.buildRegistrationForm();
	}	

	showModalDialog(){
		let redirectAfterRegistration = ['/login'];
		let content = 'Please go to your email for confirm account and try to login.';
		const modalRef = this.modalService.open(ModalDialogContent, { windowClass: 'in modal' });
		console.log(modalRef);
		modalRef.componentInstance.routedLink = redirectAfterRegistration;
		modalRef.componentInstance.body = content;
	}

	createNewUser(userData: any){
		let result = this.userService.createNewUser(userData)
										.subscribe(
											value => { 
												console.log(value);
												this.showModalDialog();
											},
											error => {
												console.log(error);
												this.formErrors = error.json();
											}
										);
	}

	onSubmit(userForm: FormGroup){
		this.userForRegistration = new User(userForm.value);
		const result = this.createNewUser(this.userForRegistration);
	}

	onValueChanged(data?: any) {
	 	this.formErrors = {
			'first_name': '',
			'last_name': '',
			'email': '',
			'username': '',
			'password': ''
		};
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