def get_short_strings(strings):
    short_strings = []
    for s in strings:
        if len(s) <= 3:
            short_strings.append(s)
    return short_strings

# Ввод массива строк с клавиатуры
strings = input("Введите строки через пробел: ").split()

# Получение нового массива из строк длиной <= 3
result = get_short_strings(strings)

# Вывод результата
print("Исходный массив строк:", strings)
print("Новый массив из коротких строк:", result)