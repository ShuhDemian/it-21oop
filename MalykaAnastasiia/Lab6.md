# Міністерство освіти і науки України
# ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ВЕТЕРИНАРНОЇ МЕДИЦИНИ ТА БІОТЕХНОЛОГІЙ ІМЕНІ С.З. ҐЖИЦЬКОГО

  ## Звіт
про виконання лаборотарної роботи №6 з дисциплини "об'єктно орієнтовне програмування" на тему "Змінні класу та об’єкта"

Виконала: студентка групи Іт-21 Малика Анастасія

Прийняв: ст. викладач Заплатинський Н.Б.

# Львів 2026

  Мета: ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні

  ## Хід роботи
  
  1.Набути навичок у створенні класів. Створити клас, який приймає декілька аргументів. На їх основі у конструкторі класу створити набір атрибутів об’єкта (класу), один з яких створюється на основі інших.

`class Parcel:`

`    def __init__(self, item_name, weight_kg):`

`        self.item_name = item_name`

`        self.weight_kg = weight_kg`

`        self.weight_grams = weight_kg * 1000`

`my_parcel = Parcel("Книги", 2.5)`

`print(f"Предмет: {my_parcel.item_name}")`

`print(f"Вага в кг: {my_parcel.weight_kg}")`

`print(f"Вага в грамах: {my_parcel.weight_grams}")`

  2. Реалізувати метод, який генерує опис об’єкта на основі його властивостей.

`class Parcel:`

`    def __init__(self, item_name, weight_kg):`

`        self.item_name = item_name`

`        self.weight_kg = weight_kg`

`        self.weight_grams = weight_kg * 1000`

`    def get_description(self):`

`        return f"Це посилка з предметом '{self.item_name}'. Її вага становить {self.weight_kg} кг ({self.weight_grams} г)."`

`box = Parcel("Печиво", 1.2)`

`description = box.get_description()`

`print(description)`

  3. Навчитися створювати об’єкти. Створити декілька об’єктів на основі класу. Викликати реалізований метод, використовуючи об’єкт і клас.

`class Smartphone:`

`    def __init__(self, brand, model, price):`

`        self.brand = brand`

`        self.model = model`

`        self.price = price`

`        self.price_usd = price / 40`

`    def get_info(self):`

`        return f"Смартфон {self.brand} {self.model} коштує {self.price} грн (${self.price_usd:.2f})"`

`#. — кількість знаків після коми, 2 — кількість знаків після крапки. f — float`

`phone1 = Smartphone("Apple", "iPhone 15", 40000)`

`phone2 = Smartphone("Samsung", "Galaxy S23", 32000)`

`phone3 = Smartphone("Xiaomi", "Redmi Note 12", 8000)`

`print(phone1.get_info())`

`print(phone2.get_info())`

`print(Smartphone.get_info(phone3))`

  4. Познайомитися з поняттям змінної класу. Реалізувати змінну класу і метод, що її використовує.

  5. Реалізувати лічильник створених за допомогою класу об’єктів.

`class Student:`

`    student_count = 0`

`    def __init__(self, name):`

`        self.name = name`

`        Student.student_count += 1`

`    def get_total_info(self):`

`        return f"Студент: {self.name}. Зараз у системі всього студентів: {Student.student_count}"`

`s1 = Student("Олексій")`

`print(f"Додали першого: {Student.student_count}")`

`s2 = Student("Марія")`

`print(f"Додали другого: {Student.student_count}")`

`print("-" * 30)`

`print(s3.get_total_info())`

  ## Висновок:
1. Набуkf навичок у створенні класів. Створиkf клас, який приймає декілька аргументів. На їх основі у конструкторі класу створиkf набір атрибутів об’єкта (класу), один з яких створюється на основі інших.
2. Реалізуваkf метод, який генерує опис об’єкта на основі його властивостей.
3. Навчиkfся створювати об’єкти. Створиkf декілька об’єктів на основі класу. Викликаkf реалізований метод, використовуючи об’єкт і клас.
4. Познайомиkfся з поняттям змінної класу. Реалізуватkf змінну класу і метод, що її використовує.
5. Реалізуваkf лічильник створених за допомогою класу об’єктів.
