from dataclasses import dataclass


@dataclass
class Person:
    first_name: str = None
    last_name: str = None
    email: str = None
    current_adress: str = None
    mobile: str = None
    subject: str = None