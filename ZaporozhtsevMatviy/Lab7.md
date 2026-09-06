## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лабораторної роботи №7 з дисциплини "Об'єктно-орієнтоване програмування" 

на тему "Використання методів класу і статичних методів"

Виконав: студент групи ІТ-21 Запорожцев Матвій

Прийняв: Ст. викладач Заплатинський Назар Богданович

## Львів 2026

Мета роботи полягає в ознайомленні з різними типами методів у 
об’єктно-орієнтованому програмуванні.

## Хід роботи

1. Засвоїти різницю між звичайними методами, методами класу та 
статичними методами.

Звичайні методи (instance methods) працюють з конкретним об'єктом через self і мають доступ до його унікальних даних. 
Методи класу (class methods) позначаються декоратором @classmethod, приймають посилання на сам клас cls замість об'єкта
і використовуються для роботи зі спільними даними класу або створення альтернативних конструкторів. Статичні методи 
(static methods) з декоратором @staticmethod не мають доступу ні до класу, ні до об'єкта; це просто логічно згруповані 
у класі функції, які не залежать від стану програми.

3. Навчитися створювати альтернативні конструктори. 

```
class Rectangle:
    default_color = "Green"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def from_string(cls, data_str):
        w, h = map(int, data_str.split("-"))
        return cls(w, h)
```

4. Для створеного у попередній роботі класу реалізувати “метод класу”, 
який повинен працювати зі змінними класу. 

```
class Rectangle:
    default_color = "Green"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def set_default_color(cls, color):
        cls.default_color = color
        print(f"Тепер стандартний колір для всіх прямокутників: {cls.default_color}")

Rectangle.set_default_color("Red")
```

5. Реалізувати альтернативний конструктор класу за допомогою методу 
класу. 

6. Створити статичний метод і перевірити його роботу.

```
class Rectangle:
    default_color = "Green"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def set_default_color(cls, color):
        cls.default_color = color
        print(f"Тепер стандартний колір для всіх прямокутників: {cls.default_color}")
    
    @staticmethod
    def is_valid(width, height):
        return width > 0 and height > 0

is_ok = Rectangle.is_valid(10, -5)
print(f"Чи валідні розміри? {is_ok}")

Rectangle.set_default_color("Red")
```

## Висновок 
У ході виконання лабораторної роботи я досяг успіхів в ознайомленні з різними типами методів у 
об’єктно-орієнтованому програмуванні.
