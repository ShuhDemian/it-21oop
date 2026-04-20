from datetime import date


class Person:
    def __init__(self, first_name: str, last_name: str, date_of_birth: date):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years

    def info(self):
        return f"Повне ім'я: {self.full_name}\nВік: {self.age}"



class Student(Person):
    def __init__(self, first_name: str, last_name: str, group: str, date_of_birth: date):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )
        self.group = group

    def info(self):
        return f"{super().info()}\nГрупа: {self.group}"

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, position: str, date_of_birth: date, group_curator: str = None):
        super().__init__(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth
        )
        self.position = position
        self.group_curator = group_curator
        self._subjects = list()

    @property
    def subjects(self) -> list[str]:
        return self._subjects.copy()

    def add_subject(self, subject: str):
        self._subjects.append(subject)

    def remove_subject(self, subject: str):
        self._subjects.remove(subject)

    def info(self):
        return f"{super().info()}\nПосада: {self.position}\nПредмети: {", ".join(self.subjects)}"

if __name__ == '__main__':
    teacher = Teacher(
        first_name='Назар',
        last_name='Заплатинський',
        position="старший викладач",
        date_of_birth=date(year=1991, month=10, day=12)
    )
    teacher.add_subject("ООП")

    print(type(teacher))
    print(teacher.info())
    print("\n")

    student = Student(
        first_name='Олійник',
        last_name='Богдан',
        group="Іт-21",
        date_of_birth=date(year=2002, month=1, day=18)
    )

    print(type(student))
    print(student.info())
    print("\n")
