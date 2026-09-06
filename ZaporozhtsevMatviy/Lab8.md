## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лабораторної роботи №8 з дисциплини "Об'єктно-орієнтоване програмування" 

на тему "Наслідування в об’єктно-орієнтованому програмуванні"

Виконав: студент групи ІТ-21 Запорожцев Матвій

Прийняв: Ст. викладач Заплатинський Назар Богданович

## Львів 2026

Мета роботи - оволодіти концепцією наслідування класів.

## Хід роботи

1. Навчитися повторно використовувати існуючий код завдяки наслідуванню. 
2. Створити один батьківський клас і декілька дочірніх. Наслідувати частину 
властивостей та функціоналу від батьківського класу в дочірніх класах. 
Освоїти використання методу super. 

```
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} їсть...")

class Dog(Animal):
    def __init__(self, name, poroda):
        super().__init__(name)
        self.poroda = poroda

    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} каже: Мяу!")
```

3. У одному з дочірніх класів організувати використання методів 
об’єктів-представників іншого дочірнього класу.

```
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} їсть...")

class Dog(Animal):
    def __init__(self, name, poroda):
        super().__init__(name)
        self.poroda = poroda

    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} каже: Мяу!")

class Trainer(Animal):
    def train_dog(self, dog_instance):
        print(f"Тренер {self.name} дає команду собаці...")
        dog_instance.bark()

my_dog = Dog("Сірко", "Вівчарка")
my_trainer = Trainer("Олег")
my_trainer.train_dog(my_dog)
```

4. Ознайомитися з методами instanceof, issubclassof.

```
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} їсть...")

class Dog(Animal):
    def __init__(self, name, poroda):
        super().__init__(name)
        self.poroda = poroda

    def bark(self):
        print(f"{self.name} гавкає: Гав-гав!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} каже: Мяу!")

class Trainer(Animal):
    def train_dog(self, dog_instance):
        print(f"Тренер {self.name} дає команду собаці...")
        dog_instance.bark()

my_dog = Dog("Сірко", "Вівчарка")
my_trainer = Trainer("Олег")
my_trainer.train_dog(my_dog)

print(isinstance(my_dog, Dog))
print(isinstance(my_dog, Animal))
print(isinstance(my_dog, Cat))

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
```

## Висновок 
У ході виконання лабораторної роботи я оволодів концепцією наслідування класів. 
