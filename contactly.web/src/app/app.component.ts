import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, inject } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Observable } from 'rxjs';
import { Contact } from '../models/contact.model';
import { AsyncPipe } from '@angular/common';
import {FormControl, FormsModule, ReactiveFormsModule, FormGroup} from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, AsyncPipe, FormsModule, ReactiveFormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  http = inject(HttpClient);

  contactsForm = new FormGroup({
    name: new FormControl<string>(''),
    email: new FormControl<string | null>(null),
    phone: new FormControl<string>(''),
    favorite: new FormControl<boolean>(false),
  })

  contacts$ = this.GetContacts();

  onFormSubmit(){
    console.log(this.contactsForm.value)

    const addContactRequest = {
      Name: this.contactsForm.value.name,
      Email: this.contactsForm.value.email,
      Phone: this.contactsForm.value.phone,
      Favorite: this.contactsForm.value.favorite,
    }

    this.http.post('https://localhost:7299/api/Contacts', addContactRequest, {
      headers: { 'Content-Type': 'application/json' }
    })
    .subscribe({
      next: (value) => {
        console.log(value)
        this.contacts$ = this.GetContacts();
        this.contactsForm.reset();
      },
      error: (error) => {
        console.error('Error al añadir contacto:', error);
        if (error.error && error.error.errors) {
          console.error('Errores específicos:', JSON.stringify(error.error.errors));
        }
      }
    })
  }

  onDelete(id: string){
    this.http.delete(`https://localhost:7299/api/Contacts/${id}`)
    .subscribe({
      next: (value) => {
        alert('Item Deleted');
        this.contacts$ = this.GetContacts();
      }
    })
  }

  private GetContacts(): Observable<Contact[]> {
    return this.http.get<Contact[]>('https://localhost:7299/api/Contacts');

  }
}
