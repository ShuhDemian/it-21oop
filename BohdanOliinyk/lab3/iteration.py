numbers = [1, 10, 4345, 3463, 5, 35, 65]

odd_num = 0
even_num = 0

print(f"\nПідрахунок кількості парних та не парних через for цикл\n")

for num in numbers:
    if num % 2 == 0:
        odd_num += 1
    else:
        even_num += 1

print(f"Кількість парних: {odd_num}\nКількість не парних: {even_num}")

odd_num = 0
even_num = 0
iteration = 0

print(f"\nПідрахунок кількості парних та не парних через while цикл\n")

while iteration < len(numbers):
    if numbers[iteration] % 2 == 0:
        odd_num += 1
    else:
        even_num += 1

    iteration += 1

print(f"Кількість парних: {odd_num}\nКількість не парних: {even_num}")