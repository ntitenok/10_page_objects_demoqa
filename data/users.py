import dataclasses
from enum import StrEnum
from datetime import date

class Gender(StrEnum):
    MALE = '[for="gender-radio-1"]'
    FEMALE = '[for="gender-radio-2"]'
    OTHER = '[for="gender-radio-3"]'



class Hobbies(StrEnum):
    sports = '[for="hobbies-checkbox-1"]'
    reading = '[for="hobbies-checkbox-2"]'
    music = '[for="hobbies-checkbox-3"]'
@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    birth_date: date
    subjects: str
    hobbies: Hobbies






