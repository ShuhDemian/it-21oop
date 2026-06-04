# Міністерство освіти і науки України

# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

## Звіт

про виконання лабораторної роботи №7 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Кашуба Денис

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026

\#Мета роботи полягає в ознайомленні з різними типами методів у об’єктно-орієнтованому програмуванні.

1. Засвоїти різницю між звичайними методами, методами класу та статичними методами.

```
class Car:
    def \\\_\\\_init\\\_\\\_(self, brand, year):
        self.brand = brand
        self.year = year

    # звичайний метод
    def show\\\_info(self):
        print(f"Марка: {self.brand}")
        print(f"Рік: {self.year}")


# створення об'єкта
car1 = Car("Mercedes", 2022)

# виклик звичайного методу
car1.show\\\_info()
```

2. Навчитися створювати альтернативні конструктори.

```
class Car:
    # змінна класу
    wheels = 4

    def \\\_\\\_init\\\_\\\_(self, brand):
        self.brand = brand

    # метод класу
    @classmethod
    def change\\\_wheels(cls, number):
        cls.wheels = number


print("До зміни:", Car.wheels)

# зміна змінної класу
Car.change\\\_wheels(6)

print("Після зміни:", Car.wheels)
```

3. Для створеного у попередній роботі класу реалізувати “метод класу”, який повинен працювати зі змінними класу.

```
class Student:
    def \\\_\\\_init\\\_\\\_(self, name, age):
        self.name = name
        self.age = age

    # альтернативний конструктор
    @classmethod
    def from\\\_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    def show(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")


# створення об'єкта через альтернативний конструктор
s1 = Student.from\\\_string("Іван-18")

s1.show()
```

4. Реалізувати альтернативний конструктор класу за допомогою методу класу.

```
class MathOperations:

    @staticmethod
    def add(a, b):
        return a + b


# виклик статичного методу
result = MathOperations.add(5, 7)

print("Сума:", result)
```

5. Створити статичний метод і перевірити його роботу.

```
class Employee:
    # змінна класу
    company = "Google"

    def \\\_\\\_init\\\_\\\_(self, name, salary):
        self.name = name
        self.salary = salary

    # звичайний метод
    def show\\\_info(self):
        print(f"Працівник: {self.name}")
        print(f"Зарплата: {self.salary}")
        print(f"Компанія: {Employee.company}")

    # метод класу
    @classmethod
    def change\\\_company(cls, new\\\_company):
        cls.company = new\\\_company

    # альтернативний конструктор
    @classmethod
    def from\\\_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    # статичний метод
    @staticmethod
    def is\\\_high\\\_salary(salary):
        return salary > 30000


# створення об'єкта
emp1 = Employee("Олег", 40000)

emp1.show\\\_info()

print()

# зміна змінної класу
Employee.change\\\_company("Microsoft")

emp1.show\\\_info()

print()

# альтернативний конструктор
emp2 = Employee.from\\\_string("Іван-25000")

emp2.show\\\_info()

print()

# статичний метод
print("Висока зарплата:", Employee.is\\\_high\\\_salary(40000))
```

## Висновок:

У ході роботи було вивчено звичайні методи, методи класу та статичні методи в Python. Також було реалізовано альтернативний конструктор і перевірено роботу всіх методів на практиці.

