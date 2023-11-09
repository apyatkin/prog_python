"""
Task 1
Привітання користувача. Напишіть Python-скрипт, який вітає користувача за його ім'ям.
Ім'я вводить користувач з клавіатури за допомогою функції input,
а потім виводиться привітання за допомогою функції print.
"""
print("Task 1")
print("=============")
name = input("Please insert your name: ")
print(f"Hello, {name}!")

"""
Task 2
Написати Python-скрипт, який для п'яти цілочисельних значень (вводить користувач з клавіатури),
знаходить мінімум, максимум та середнє.
Для пошуку мінімального та максимального значення потрібно використовувати функції min, max:.
"""


def avg(list_int):
    return sum(list_int) / len(list_int)


print("Task 2")
print("=============")
n = 1
int_list = []
while n < 6:
    user_input = int(input(f"Please input number {n}: "))
    int_list.append(user_input)
    n += 1
print(f"Min:", min(int_list))
print(f"Max:", max(int_list))
print(f"Avg:", avg(int_list))

"""
Task 3
Написати Python-скрипт, який буде повертати результат
арифметичних дій +, -, *, /, // для заданих x та y (вводить користувач з клавіатури).
"""


def is_num(user_input_int):
    if user_input_int.isdigit():
        return int(user_input_int)


print("Task 3")
print("=============")
first_num = is_num(input(f"Please input first number: "))
second_num = is_num(input(f"Please input second number: "))
operator = input(f"Please input operator: ")

match operator:
    case "+":
        print(f"The answer is: {first_num} {operator} {second_num} = ", first_num + second_num)
    case "-":
        print(f"The answer is: {first_num} {operator} {second_num} = ", first_num - second_num)
    case "*":
        print(f"The answer is: {first_num} {operator} {second_num} = ", first_num * second_num)
    case "/":
        print(f"The answer is: {first_num} {operator} {second_num} = ", first_num / second_num)


"""
Task 4
Написати Python-скрипт, який для кола заданого радіуса (вводить користувач з клавіатури) знаходить діаметр,
довжину і площу окружності.
"""

print("Task 4")
print("=============")


"""
Task 5
Деякі інвестиційні консультанти вважають, що розумно очікувати 10% прибутку
в довгостроковій перспективі на фондовому ринку.
Припускаючи, що ви починаєте з 1000 доларів і залишаєте свої гроші інвестованими, обчисліть і відобразіть,
скільки грошей ви матимете через 10, 20 і 30 років.
Використовуйте наступну формулу для визначення цих сум:
a = p(1 + r)^n
де p — початкова інвестована сума (тобто основна сума 1000 доларів США),
r – річна норма прибутку (10%),
n - кількість років (10, 20 або 30),
a — сума на депозиті на кінець n-го року.
"""

radius = float(input("Введите радиус круга: "))

diameter = 2 * radius
circumference = 2 * 3.14159 * radius
area = 3.14159 * radius**2

print(f"Диаметр круга: {diameter}")
print(f"Длина окружности: {circumference}")
print(f"Площадь окружности: {area}")

print("Task 5")
print("=============")

amount = float(input("Начальная инвестированная сумма: "))
invest_year = int(input("Количество лет: "))

a = round(amount * (1 + 0.1)**invest_year, 2)
print(a)

"""
Task 6
Створіть скрипт-конвертер валюти,
який запитує у користувача суму в доларах і переводить її в гривні згідно поточного обмінного курсу.
Обмінний курс можна вказати в програмі.
"""
print("Task 6")
print("=============")

usd_amount = float(input("Сумма в долларах: "))
rate = 1.7
print("Курс доллара к манату - 1.7")
print("Вы получите", usd_amount * rate, "долларов.")


"""
Task 7
Написати скрипт, яких тризначне ціле число (вводить користувач з клавіатури) розділяє на окремі цифри.
Кожну цифру треба вивести в окремому рядку.
Наприклад, якщо користувач вводить число 987, скрипт має вивести в термінал
9
8
7
"""
print("Task 7")
print("=============")

int_to_operate = input("Число: ")
for entry in int_to_operate:
    print(entry)
