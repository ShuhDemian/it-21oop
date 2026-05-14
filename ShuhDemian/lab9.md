# Міністерство освіти і науки України
# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

  ## Звіт
про виконання лабораторної роботи №9 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Шух Дем'ян

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026
#Мета роботи - засвоїти застосування принципу поліморфізму в об’єктно-орієнтованому програмуванні.
1. Ознайомитися з поняттям поліморфізму в ООП. 
```
class Animal:

    def sound(self):
        print("Тварина видає звук")


class Dog(Animal):

    def sound(self):
        print("Гав-гав")


class Cat(Animal):

    def sound(self):
        print("Мяу")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

2. Навчитися перевизначати поведінку методів. 

```
class Employee:

    def work(self):
        print("Працівник працює")


class Programmer(Employee):

    def work(self):
        print("Програміст пише код")


emp = Employee()
prog = Programmer()

emp.work()
prog.work()
```

3. Реалізувати декілька “магічних методів” для роботи з визначеними раніше класами.
```
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, Вік: {self.age}"


s1 = Student("Іван", 18)

print(s1)
```
4. Магічний метод len()
```
class Group:

    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)


g1 = Group(["Іван", "Олег", "Марія"])

print(len(g1))
```
5. Магічний метод add()
```
class Money:

    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __str__(self):
        return f"{self.amount} грн"


m1 = Money(100)
m2 = Money(250)

result = m1 + m2

print(result)

```
## Висновок:
У ході роботи було вивчено поняття поліморфізму та перевизначення методів у Python. Також було реалізовано магічні методи для роботи з об’єктами класів і перевірено їхню роботу на практиці.

