from peewee import *
from datetime import date

db= SqliteDatabase('personas.db')

class Person(Model):
    name=CharField()
    is_relative= BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, column_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db



def create_an_connect():
    db.connect()
    db.create_tables([Person, Pet], safe=True)

def add_person():
    rodrigo = Person.create(name='Grandma', is_relative=True)
    erika = Person.create(name='Erika', is_relative=True)
    juan = Person.create(name='Juancho', is_relative=True)

    tommy=Pet.create(owner=rodrigo,name="Fido",animal_type="Perro")

    tommy.name="Firulais"
    tommy.save();

def get_person():
    for per in Person.select():
        print('Nombre: {} is relative {} '.format(per.name, per.is_relative))
#Obtenemos todo

def get_person_id(data):
    id=Person.select().where(Person.name == data).get()
    print("Se encontro a: {} ".format(id.name))


create_an_connect()

# add_person()

get_person()

get_person_id("Juancho")


