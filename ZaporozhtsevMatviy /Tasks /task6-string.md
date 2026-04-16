# Варіант 3

Дано послідовність слів, відокремлених пропусками, в кінці крапка. 
Видалити зі стрічки всі попередні входження останньої літери. 

```
text = "яблуко апельсин ананас абрикос."
last_char = text[-2]
prefix = text[:-2]
cleaned_prefix = prefix.replace(last_char, "")
result = cleaned_prefix + last_char + "."
print(f"Остання літера для видалення: '{last_char}'")
print(f"Результат: {result}")
```
