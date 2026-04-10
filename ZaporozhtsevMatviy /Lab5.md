## Міністерство освіти і науки України

## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

# Звіт
про виконання лабораторної роботи №5 з дисциплини "Об'єктно-орієнтоване програмування" 

на тему "Змінні класу та об’єкта"

Виконав: студент групи ІТ-21 Запорожцев Матвій

Прийняв: Ст. викладач Заплатинський Назар Богданович

## Львів 2026

Мета роботи – ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні 

## Хід роботи

1. Набути навичок у створенні класів. Створити клас, який приймає 
декілька аргументів. На їх основі у конструкторі класу створити набір 
атрибутів об’єкта (класу), один з яких створюється на основі інших. 

```
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = f"{brand} {model}"

phone1 = Smartphone("Apple", "iPhone 15", 40000)
print(phone1.full_name)
```

2. Реалізувати метод, який генерує опис об’єкта на основі його 
властивостей.  

```
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = f"{brand} {model}"

    def get_description(self):
        return f"Смартфон: {self.full_name}, ціна: {self.price} грн."

phone1 = Smartphone("Samsung", "Galaxy S23", 35000)
print(phone1.get_description())
```

3. Навчитися створювати об’єкти. Створити декілька об’єктів на основі 
класу. Викликати реалізований метод, використовуючи об’єкт і клас. 

```
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = f"{brand} {model}"

    def get_description(self):
        return f"Смартфон: {self.full_name}, ціна: {self.price} грн."

phone1 = Smartphone("Google", "Pixel 8", 30000)
phone2 = Smartphone("Xiaomi", "13T", 20000)

print(phone1.get_description())
print(Smartphone.get_description(phone2))
```

4. Познайомитися з поняттям змінної класу. Реалізувати змінну класу і 
метод, що її використовує. 

```
class Smartphone:
    currency = "UAH"

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = f"{brand} {model}"

    def get_description(self):
        return f"Смартфон: {self.full_name}, ціна: {self.price} {Smartphone.currency}."

    def change_price_format(self):
        return f"{self.price} {self.currency}"

phone1 = Smartphone("Nothing", "Phone 2", 25000)
print(phone1.change_price_format())
```

5. Реалізувати лічильник створених за допомогою класу об’єктів. 

```
class Smartphone:
    currency = "UAH"
    count = 0

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.full_name = f"{brand} {model}"
        Smartphone.count += 1

    def get_description(self):
        return f"Модель: {self.full_name}, Ціна: {self.price} {Smartphone.currency}"

    def print_total_info(self):
        print(f"Зараз у базі смартфонів: {Smartphone.count}")

phone1 = Smartphone("Apple", "iPhone 15", 40000)
phone2 = Smartphone("Samsung", "S23", 35000)
print(phone1.get_description())
print(Smartphone.get_description(phone2))
phone1.print_total_info()
```

## Висновок 
У ході виконання лабораторної роботи я ознайомився з різними типами змінних классу та об'єкта в об’єктно-орієнтованому програмуванні. 
