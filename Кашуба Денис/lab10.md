# Міністерство освіти і науки України

# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

## Звіт

про виконання лабораторної роботи №10 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Кашуба Денис

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026

\#Мета роботи - освоїти роботу з декораторами в Python 3.

1. Навчитися використовувати декоратор “@property”. Написати принаймні один метод з його використанням.

```
class Student:

    def \_\_init\_\_(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}, {self.age} років"


s1 = Student("Діма", 20)

print(s1.info)

```

2. Ознайомитися з концепцією getter’ів, setter’ів і delete’рів. Реалізувати хоча б один метод з їх використанням.

```
class Employee:

    def \_\_init\_\_(self, salary):
        self.\_salary = salary

    # getter
    @property
    def salary(self):
        return self.\_salary

    # setter
    @salary.setter
    def salary(self, value):

        if value > 0:
            self.\_salary = value
        else:
            print("Зарплата повинна бути більшою за 0")


emp = Employee(20000)

print(emp.salary)

emp.salary = 35000

print(emp.salary)
```

3. Delete’r

```
class Product:

    def \_\_init\_\_(self, name):
        self.\_name = name

    @property
    def name(self):
        return self.\_name

    @name.deleter
    def name(self):
        print("Назву товару видалено")
        del self.\_name


p1 = Product("Ноутбук")

print(p1.name)

del p1.name

```



## Висновок:

У ході роботи було вивчено використання декоратора @property, а також принцип роботи getter’ів, setter’ів і deleter’ів. Було реалізовано методи для отримання, зміни та видалення властивостей об’єктів класу.

