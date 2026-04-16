# Варіант 3

1. Протабулювати функцію y = ctg x + 1 на проміжку [a, b], з кроком h. Результати вивести на 
екран у вигляді таблиці пар чисел x і y. Обчислити добуток аргументів максимального та 
мінімального значень функції y. 

```
import math

a = 2.0
b = 4.0
h = 0.1

print(f"{'x':<10} | {'y':<10}")
print("-" * 25)

x = a
min_y = float('inf')
max_y = float('-inf')
x_at_min = 0
x_at_max = 0

while x <= b + h/10:
    try:
        y = (1 / math.tan(x)) + 1
        print(f"{round(x, 2):<10} | {round(y, 4):<10}")
        
        if y < min_y:
            min_y = y
            x_at_min = x
        if y > max_y:
            max_y = y
            x_at_max = x
            
    except ZeroDivisionError:
        print(f"{round(x, 2):<10} | Не визначено")
    
    x += h

product_of_x = x_at_min * x_at_max
print("-" * 25)
print(f"Добуток аргументів (x_min * x_max): {round(product_of_x, 4)}")
```

2. Задано натуральне число n. Обчислити:

P = (1-(1/2)) * (1-(1/4)) * (1-(1/6)) * ... * (1-(1/2n))

```
n = int(input("Введіть натуральне число n: "))
p = 1.0

for i in range(1, n + 1):
    term = 1 - (1 / (2 * i))
    p *= term

print(f"Результат P: {round(p, 6)}")
```
