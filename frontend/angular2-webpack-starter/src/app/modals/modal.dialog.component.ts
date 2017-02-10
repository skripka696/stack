import { 
	Component,
	Input
} from '@angular/core';
import { NgbActiveModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
	selector: 'modal-dialog',
	templateUrl: './modal.dialog.template.html'
})

export class ModalDialogContent{
	@Input() routedLink;
	@Input() body;

	constructor(public activeModal: NgbActiveModal) {}
}