# Міністерство освіти і науки України
# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

  ## Звіт
про виконання лабораторної роботи №7 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Лущак Олег

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026
#Мета роботи полягає в ознайомленні з різними типами методів у об’єктно-орієнтованому програмуванні.
1. Засвоїти різницю між звичайними методами, методами класу та статичними методами.
```
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # звичайний метод
    def show_info(self):
        print(f"Марка: {self.brand}")
        print(f"Рік: {self.year}")


# створення об'єкта
car1 = Car("BMW", 2020)

# виклик звичайного методу
car1.show_info()
```
2. Навчитися створювати альтернативні конструктори. 
```
class Car:
    # змінна класу
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    # метод класу
    @classmethod
    def change_wheels(cls, number):
        cls.wheels = number


print("До зміни:", Car.wheels)

# зміна змінної класу
Car.change_wheels(6)

print("Після зміни:", Car.wheels)
```

3. Для створеного у попередній роботі класу реалізувати “метод класу”, який повинен працювати зі змінними класу. 
```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # альтернативний конструктор
    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    def show(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age}")


# створення об'єкта через альтернативний конструктор
s1 = Student.from_string("Іван-18")

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

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # звичайний метод
    def show_info(self):
        print(f"Працівник: {self.name}")
        print(f"Зарплата: {self.salary}")
        print(f"Компанія: {Employee.company}")

    # метод класу
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # альтернативний конструктор
    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    # статичний метод
    @staticmethod
    def is_high_salary(salary):
        return salary > 30000


# створення об'єкта
emp1 = Employee("Олег", 40000)

emp1.show_info()

print()

# зміна змінної класу
Employee.change_company("Microsoft")

emp1.show_info()

print()

# альтернативний конструктор
emp2 = Employee.from_string("Іван-25000")

emp2.show_info()

print()

# статичний метод
print("Висока зарплата:", Employee.is_high_salary(40000))
```

## Висновок:
У ході виконання лабораторної роботи було детально розглянуто різні типи методів у Python: звичайні методи, методи класу та статичні методи. Було з’ясовано, що звичайні методи працюють з екземплярами класу, методи класу — з атрибутами самого класу, а статичні методи не залежать ні від класу, ні від його екземплярів. На практиці було реалізовано альтернативний конструктор за допомогою методу класу, що дозволяє створювати об’єкти з різних форматів вхідних даних. Також було створено і протестовано статичний метод для виконання допоміжних операцій, не пов’язаних із станом класу чи об’єкта. Отримані знання дозволяють ефективніше організовувати код, підвищувати його гнучкість і повторне використання, а також краще розуміти принципи об’єктно-орієнтованого програмування в Python.
