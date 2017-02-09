import { 
	Directive, 
	ElementRef, 
	ViewContainerRef, 
	Input
} from '@angular/core';
import { Overlay } from 'angular2-modal';
import { Modal } from 'angular2-modal/plugins/bootstrap';


@Directive({
	selector: 'modal-dialog',
})

export class ModalDialogDirective{
	constructor(private el: ElementRef,
				overlay: Overlay, 
				vcRef: ViewContainerRef, 
				public modal: Modal){
		overlay.defaultViewContainer = vcRef;
	}

	openModal(message: string) {
    	this.modal.alert()
    	.message(message)
    	.open();
	}
}