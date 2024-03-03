import dataclasses
from enum import Enum
import datetime


class Gender(Enum):
    Male = 1
    Female = 2
    Other = 3


class Hobbies(Enum):
    Sports = 1
    Reading = 2
    Music = 3


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    birth_date: datetime.date
    subjects: str
    hobbies: Hobbies
    file_name: str
    current_address: str
    state: str
    city: str
    file: str


nikolai = User(first_name='Nikolai', last_name='Titenok', email='ntitenok@gmail.com', gender=Gender.Male,
               mobile_number='1234567890', birth_date=datetime.date(1989, 5, 22), subjects='Computer Science',
               hobbies=Hobbies.Music, file_name='myfile.txt', current_address='Bombey street',
               state='Uttar Pradesh', city='Agra', file='myfile.txt')
