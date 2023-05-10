from peewee import *
import datetime


db = PostgresqlDatabase('people', user='banana', 
password='123', 
host='localhost', 
port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db

class Person(BaseModel):
    name = CharField()
    birthday = DateField()

class Pet(BaseModel):
    name = CharField()
    animal_type = CharField()

db.drop_tables([Person, Pet])
db.create_tables([Person, Pet])


zakk = Person(name='Zakk', birthday=datetime.date(1990, 11, 18))
zakk.save()

pets = [
        {'name': 'Goose', 'animal_type': 'dog'},
        {'name': 'Pig','animal_type': 'dog'},
        {'name': 'Baci', 'animal_type': 'cat'},
        {'name': 'Luna', 'animal_type': 'bunny'},
        {'name': 'Shits', 'animal_type': 'rock'},
        {'name': 'Giggles', 'animal_type': 'snake'}
]

Pet.insert_many(pets).execute()


# use .get() to find a SINGLE record. otherwise use .select()
Person.get(Person.name == 'Zakk')
Person.get(Person.birthday == datetime.date(1990, 11, 18))
Person.select()
Person.select().where(Person.birthday < datetime.date(1990, 1, 1))

# use .delete_instance() method to delete data
# zakk.delete_instance()

grabbing_zakk = Person.get(Person.name == 'Zakk')
print(grabbing_zakk.birthday)
# output: 'Zakk'

list_of_people = Person.select().where(Person.birthday > datetime.date(1990, 1, 1))
print([user.birthday for user in list_of_people])

find_goose = Pet.get(Pet.name == 'Goose')
print(find_goose)
# Outputs: 1; which is the records ID
print(find_goose.name)
# Outputs: Goose
print(find_goose.animal_type)
# Outputs: dog


list_of_pets = Pet.select().where(Pet.animal_type == 'rock')
print([pet.name for pet in list_of_pets])
# Output: ['Shits']
