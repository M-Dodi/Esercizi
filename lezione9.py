
#Progettare un sistema di gestione della biblioteca con i seguenti requisiti:

"""Classe Book:
        Attributi:
            book_id: str - Identificatore di un libro.
            title: str - titolo del libro.
            author: str - autore del libro
            is_borrowed: boolean - booleano che indica se il libro è in prestito o meno.
        Metodi:
            borrow()-Contrassegna il libro come preso in prestito se non è già preso in prestito.
            return_book()- Contrassegna il libro come restituito.

    Classe Member:
        Attributi:
            member_id: str - identificativo del membro.
            name: str - il nome del membro.
            borrowed_books: list[Book] - lista dei libri presi in prestito.
        Metodi:
            borrow_book(book): aggiunge il libro nella lista borrowed_books se non è già stato preso in prestito.
            return_book(book): rimuove il libro dalla lista borrowed_books.

    Classe Library:
        Attributi:
            books: dict[str, Book] - dizionario che ha per chiave l'id del libro e per valore l'oggetto Book
            members: dict[str, Member] - dizionario che ha per chiave l'id del membro e per valore l'oggetto Membro
        Methodi:
            add_book(book_id: str, title: str, author: str): Aggiunge un nuovo libro nella biblioteca.
            register_member(member_id:str, name: str): Iscrive un nuovo membro nella biblioteca.
            borrow_book(member_id: str, book_id: str): Permette al membro di prendere in prestito il libro.
            return_book(member_id: str, book_id: str): Permette al membro di restituire il libro.
            get_borrowed_books(member_id): list[Book] - restituisce la lista dei libri presi in prestito dal membro."""



class Book:

    def __init__(self,book_id: str, title: str, author: str):
        
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        
        if  self.is_borrowed ==True:
            
            print(f"Il libro '{self.title}' è stato preso in prestito.")

        else:

            print(f"Il libro '{self.title}' è già in prestito.")



    def  return_book(self):

        if self.is_borrowed == False:

            print(f"Il libro '{self.title}' è stato restituito.")

        else:

            print(f"Il libro '{self.title}' non è in prestito.")


class Member:
    def __init__(self, member_id: str, name: str):

        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Il libro '{book.title}' è già in prestito.")

        else:
            self.borrowed_books.append(book)
            book.borrow()
            print(f"Il libro '{book.title}' è stato preso in prestito da {self.name}.")

    def return_book(self, book):

        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()

            print(f"Il libro '{book.title}' è stato restituito da {self.name}.")

        else:

            print(f"Il libro '{book.title}' non è stato preso in prestito da {self.name}.")




class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id: str, title: str, author: str):
        book = Book(book_id, title, author)
        self.books[book_id] = book

        print([title])

    def register_member(self, member_id: str, name: str):
        member = Member(member_id, name)
        self.members[member_id] = member
        print(f"{name}")

    def borrow_book(self, member_id, book_id):
        
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)
        
        else:
            print("Membro o libro non trovato.")

    def return_book(self, member_id, book_id):
        
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)

        else:
            print("Membro o libro non trovato.")

    
    def get_borrowed_books(self, member_id):
        
        if member_id in self.members:
            member = self.members[member_id]
            return member.borrowed_books
       
        else:
            print("Membro non trovato.")
            return []


library = Library()
library.add_book("B001", "Il Signore degli Anelli", "J.R.R. Tolkien")
library.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
library.add_book("B002", "1984", "George Orwell")
library.add_book("B003", "To Kill a Mockingbird", "Harper Lee")


library.register_member("M001", "Alice")
library.register_member("M002", "Bob")
library.register_member("M003", "Charlie")

library.borrow_book("M001", "B001")
library.borrow_book("M002", "B002")
library.return_book("M001", "B001") 





print(library.get_borrowed_books("M001"))  # Expected output: ['The Great Gatsby']
print(library.get_borrowed_books("M002"))  # Expected output: ['1984']

	

	
	



