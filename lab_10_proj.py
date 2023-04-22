#exes 1
import random

employees = {}

check_true = True

while check_true:
    #10
    employees_name = input("Введите имя сотрудника: ")
    employees_surname = input("Введите фамилью сотрудника: ")
    #1
    employees_age = int(input("Введите зарплату сотрудника: "))
    #2
    employees_id = random.randrange(1, 100)
    #3
    employees[employees_id] = {"name: {}".format(employees_name, employees_surname), "payment: {}".format(employees_age)}
    #4
    if input("Введите exit, если хотите выйти...").lower() == "exit":
        break

#5
for item in sorted(employees.keys()):
    #6
    print(str(employees[item]) + ": сотрудник, id: " + str(item))

check_true = True
while check_true:
    find_id = int(input("Введите id сотрудника, который хотите уволить: "))
    print(str(employees[find_id]) + ": сотрудник, id: " + str(find_id))
    #10
    employees.pop(find_id)

    for item in sorted(employees.keys()):
        print(str(employees[item]) + ": сотрудник, id: " + str(item))

    if input("Введите exit, если хотите выйти...").lower() == "exit":
        break

#7, 8
print("Минимальная зарплата: " + str(min(employees.items(), key=lambda x: x[1])))
#9
print("Максимальная зарплата: " + str(max(employees.items(), key=lambda x: x[1])))
