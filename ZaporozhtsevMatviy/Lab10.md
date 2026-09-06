## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лабораторної роботи №10 з дисциплини "Об'єктно-орієнтоване програмування" 
на тему "Використання декораторів методів"

Виконав: студент групи ІТ-21 Запорожцев Матвій
Прийняв: Ст. викладач Заплатинський Назар Богданович

## Львів 2026

Мета роботи - освоїти роботу з декораторами в Python 3. 

## Хід роботи

1. Навчитися використовувати декоратор “@property”. Написати принаймні 
один метод з його використанням.

```
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    @property
    def full_name(self):
        return f"{self.brand} {self.model}"

phone = Smartphone("Apple", "iPhone 15", 40000)
print(phone.full_name)
```

2. Ознайомитися з концепцією getter’ів, setter’ів і delete’рів. Реалізувати хоча 
б один метод з їх використанням.

```
class Smartphone:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Виклик геттера: отримання ціни...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Помилка: ціна не може бути меншою за нуль!")
        else:
            print(f"Виклик сеттера: зміна ціни на {value}")
            self._price = value

    @price.deleter
    def price(self):
        print("Виклик делетера: видалення ціни...")
        del self._price

phone = Smartphone(30000)
print(phone.price)
phone.price = 35000
phone.price = -100
del phone.price
```

## Висновок 
У ході виконання лабораторної роботи я освоїв роботу з декораторами в Python 3. 
