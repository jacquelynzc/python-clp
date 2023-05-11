from peewee import *
import datetime

db = PostgresqlDatabase('notes', user='rude', password='123', host='localhost', port=5432)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    body = TextField()

def create_note():
    print("Hi! Welcome to your new favorite notes utility : ")
    answer = input("What would you like to do? View Notes(v), Add Notes(a), Update Notes(u), Delete Notes(d) ").lower()
  
    if answer == "v":
          list_notes = Note.select()
          for note in list_notes:
            print(f"{note.title}, {note.body}")
            
    elif answer == "a":
        while True:
            title = input("Enter note title: ")
            body = input("Enter note body: ")
            try:
                note = Note.create(title=title, body=body)
                print(f"Note '{note.title}' created successfully!")
                break
            except IntegrityError:
                print(f"A note with title '{title}' already exists. Please choose a different title")
  
    elif answer == "u":
        title = input("Enter title of note to update: ")
        note = Note.get_or_none(Note.title == title)
        if note is None:
            print(f"No note with title '{title}' found.")
        else:
            new_title = input(f"Enter new title for note '{note.title}': ")
            new_body = input(f"Enter new body for note '{note.title}': ")
            note.title = new_title
            note.body = new_body
            note.save()
            print(f"Note '{title}' updated successfully!")
            
    elif answer == "d":
        title = input("Enter title of note to delete: ")
        note = Note.get_or_none(Note.title == title)
        if note is None:
            print(f"No note with title '{title}' found.")
        else:
            note.delete_instance()
            print(f"Note '{title}' deleted successfully!")
  
create_note()
