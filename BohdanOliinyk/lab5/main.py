from datetime import date


class Student:
    def __init__(self, first_name: str, lost_name: str, group: str, date_of_birth: date):
        self.first_name = first_name
        self.lost_name = lost_name
        self.group = group
        self.date_of_birth = date_of_birth

    @property
    def full_name(self):
        return f'{self.first_name} {self.lost_name}'

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

    def info(self) -> str:
        return f"{self.full_name}, група: {self.group}, вік: {self.age}"


if __name__ == '__main__':
    first_student = Student(first_name='John', lost_name='Doe', group="Іт-21", date_of_birth=date(year=2002, month=1, day=18))
    print(type(first_student))
    print(first_student.info())

