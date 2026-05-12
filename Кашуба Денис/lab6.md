# Міністерство освіти і науки України
# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

  ## Звіт
про виконання лабораторної роботи №6 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Кашуба Денис

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026
#Мета роботи – ознайомитися з різними типами змінних в
об’єктно-орієнтованому програмуванні
1. Набути навичок у створенні класів. Створити клас, який приймає
декілька аргументів. На їх основі у конструкторі класу створити набір
атрибутів об’єкта (класу), один з яких створюється на основі інших.
```
class Rectangle:
    def __init__(self, length, width):
        self.length = length     
        self.width = width        
        
     
        self.area = length * width   # площа

    
    def show_info(self):
        print("Довжина:", self.length)
        print("Ширина:", self.width)
        print("Площа:", self.area)



rect1 = Rectangle(5, 3)


rect1.show_info()
```
2. Реалізувати метод, який генерує опис об’єкта на основі його
властивостей.
```
class Book:
    def __init__(self, title, author, year):
        self.title = title     
        self.author = author   
        self.year = year      

  
    def get_description(self):
        description = f"Книга '{self.title}'
        return description



book1 = Book("Кобзар", "Тарас Шевченко", 1840)


print(book1.get_description())
```
3. Навчитися створювати об’єкти. Створити декілька об’єктів на основі
класу. Викликати реалізований метод, використовуючи об’єкт і клас.
```
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_description(self):
        return f"Книга '{self.title}', автор {self.author}, {self.year} рік."


book1 = Book("Кобзар", "Тарас Шевченко", 1840)
book2 = Book("Лісова пісня", "Леся Українка", 1911)
book3 = Book("Захар Беркут", "Іван Франко", 1883)
print(book1.get_description())
print(book2.get_description())
print(book3.get_description())

print()

# Виклик методу через клас
print(Book.get_description(book1))
print(Book.get_description(book2))
print(Book.get_description(book3))
```
4. Познайомитися з поняттям змінної класу. Реалізувати змінну класу і
метод, що її використовує.
```
class Student:
    university = "ЛНУ ім. Івана Франка"

    def __init__(self, name):
        self.name = name  

  
    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Університет: {Student.university}")



student1 = Student("Денис")
student2 = Student("Дем'ян")


student1.show_info()
print()
student2.show_info()

Student.university = "ЛНУ Ветиренарної медицини та біотехнологій"

print("\nПісля зміни змінної класу:\n")

student1.show_info()
student2.show_info()
```
5. Реалізувати лічильник створених за допомогою класу об’єктів.
```

class User:
    
    count = 0

    def __init__(self, name):
        self.name = name
        User.count += 1   
  
    @classmethod
    def show_count(cls):
        print("Кількість створених об'єктів:", cls.count)



user1 = User("Іван")
user2 = User("Олег")
user3 = User("Марія")


User.show_count()
```
## Висновок:
Я ознайомився з різними типами змінних в
об’єктно-орієнтованому програмуванні

