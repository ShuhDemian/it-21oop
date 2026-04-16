# Варіант 3

Задана матриця розмірності n*m. Знайти максимальний за модулем елемент матриці. 
Переставити рядки і стовпці матриці так, щоб цей елемент опинився на перетині k-го рядка і k-го стовпця

```
import random

n = int(input("Кількість рядків n: "))
m = int(input("Кількість стовпців m: "))
k = int(input("Цільовий індекс k (починаючи з 1): ")) - 1

matrix = [[random.randint(-100, 100) for _ in range(m)] for _ in range(n)]

print("\nПочаткова матриця:")
for row in matrix:
    print(row)

max_val = matrix[0][0]
max_row, max_col = 0, 0

for i in range(n):
    for j in range(m):
        if abs(matrix[i][j]) > abs(max_val):
            max_val = matrix[i][j]
            max_row, max_col = i, j

print(f"\nМаксимальний за модулем елемент: {max_val} в позиції ({max_row+1}, {max_col+1})")

matrix[max_row], matrix[k] = matrix[k], matrix[max_row]

for i in range(n):
    matrix[i][max_col], matrix[i][k] = matrix[i][k], matrix[i][max_col]

print(f"\nМатриця після перестановки на перетин {k+1}-го рядка та стовпця:")
for row in matrix:
    print(row)
```
