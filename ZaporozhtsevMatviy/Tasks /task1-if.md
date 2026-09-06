# Варіант 3

1. Дано 4 числа a, b, c, d. Знайти max{min(a, b), min(c, d)}:

```
a = 1
b = 2
c = 3
d = 4
x = max(min(a, b), min(c, d))
print(x)
```



2. Для даного x обчислити значення функції: 

F(x) = 

= {9 ,         якщо x <= -3

= {1/(x^2+1) , якщо x > -3

```
def func(x):
    if x <= -3:
        return 9
    elif x > -3:
        return 1/((x**2)+1)
    else:
        return "chomu"
        
print(func(-4))

# > 9
```
