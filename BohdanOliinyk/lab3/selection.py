number = int(input("Введіть число для перевірки: "))

if number > 0:
    print("Число додатне")
elif number == 0:
    print("Число дорівнює нулю")
else:
    print("Число від’ємне")

if number % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")
