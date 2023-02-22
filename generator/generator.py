import random

from data.data import Person
from faker import Faker

faker_en = Faker('En')


def generated_person():
    return Person(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        current_adress=faker_en.address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )

def generated_file():
    path = rf'C:\Users\Vredina\PycharmProjects\qa_example_python\test{random.randint(10,100)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(23,100)}')
    file.close()
    return path