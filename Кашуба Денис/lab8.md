# Міністерство освіти і науки України

# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

## Звіт

про виконання лабораторної роботи №8 з дисципліни "об'єктно орієнтовне програмування" на тему "Основи структурного програмування в Python 3"

Виконав: студент групи Іт-21 Кашуба Денис

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026

\#Мета роботи - оволодіти концепцією наслідування класів.

1. Навчитися повторно використовувати існуючий код завдяки наслідуванню.

```
class Animal:
    def \_\_init\_\_(self, name):
        self.name = name

    def make\_sound(self):
        print("Тварина видає звук")
```

2. Створити один батьківський клас і декілька дочірніх. Наслідувати частину властивостей та функціоналу від батьківського класу в дочірніх класах. Освоїти використання методу super.

```
class Animal:
    def \_\_init\_\_(self, name):
        self.name = name

    def make\_sound(self):
        print("Тварина видає звук")


class Dog(Animal):

    def \_\_init\_\_(self, name, breed):
        super().\_\_init\_\_(name)
        self.breed = breed

    def make\_sound(self):
        print("Гав-гав")


dog1 = Dog("Бобік", "Бігль")

print(dog1.name)
print(dog1.breed)

dog1.make\_sound()

```

3. У одному з дочірніх класів організувати використання методів об’єктів-представників іншого дочірнього класу.

```
class Animal:
    def \_\_init\_\_(self, name):
        self.name = name


class Cat(Animal):

    def \_\_init\_\_(self, name, color):
        super().\_\_init\_\_(name)
        self.color = color

    def make\_sound(self):
        print("Мяу")


cat1 = Cat("Мурчик", "Білий")

print(cat1.name)
print(cat1.color)

cat1.make\_sound()

```

4. Ознайомитися з методами instanceof, issubclassof.

```
class Animal:
    def \_\_init\_\_(self, name):
        self.name = name


class Cat(Animal):

    def make\_sound(self):
        print("Мяу")


class Dog(Animal):

    def play\_with\_cat(self, cat):
        print(f"{self.name} грається з котом {cat.name}")
        cat.make\_sound()


cat1 = Cat("Мурчик")
dog1 = Dog("Джессі")

dog1.play\_with\_cat(cat1)
```



## Висновок:

У ході роботи було вивчено наслідування класів у Python та використання методу super(). Також було реалізовано взаємодію між дочірніми класами і перевірено роботу функцій isinstance() та issubclass().

