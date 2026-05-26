#1
from datetime import datetime
current_time = datetime.now()
print(current_time)

#2
import random
random_list = [random.randint(1,100) for i in range(101)]
randomer_number = random.choice(random_list)
print(randomer_number)

#3
from matplotlib import pyplot as plt
import random
number_a = list(range(1,13))
number_b = [random.randint(0,1000) for i in range(12)]
plt.plot(number_a,number_b)
plt.show()

#Задание 1
from datetime import datetime
from datetime import date
employees = [
    ["Иванов Иван Иванович", "Менеджер", "22.10.2013", 250000],
    ["Сорокина Екатерина Матвеевна", "Аналитик", "12.03.2020", 75000],
    ["Струков Иван Сергеевич", "Старший программист", "23.04.2012", 150000],
    ["Корнеева Анна Игоревна", "Ведущий программист", "22.02.2015", 120000],
    ["Старчиков Сергей Анатольевич", "Младший программист", "12.11.2021", 50000],
    ["Бутенко Артем Андреевич", "Архитектор", "12.02.2010", 200000],
    ["Савченко Алина Сергеевна", "Старший аналитик", "13.04.2016", 100000]
]

def count_awards(salary):
    return salary*0.03 + 2000

def calculate_term(hire_date):
    today = date.today()
    term = today.year - hire_date.year - ((today.month, today.day) < (hire_date.month, hire_date.day))
    return term

for emp in employees:
    #Рассчитываем стаж работы и добавляем его в список характеристик сотрудников
    emp.append(calculate_term(datetime.strptime(emp[-2], "%d.%m.%Y").date()))
    #Проводим индексацию зарплат тем, кто проработал больше 10 лет
    if emp[-1]>10:
        emp[-2]+=emp[-2]*0.07
    else:
        emp[-2]+=emp[-2]*0.05

def vacation(employee):
    list_of_vacations = [emp for emp in employee if emp[-1]>6]
    return list_of_vacations
list_of_vacations = vacation(employees)
print(list_of_vacations)


#Задание 2
import random
random_1= random.randint(1,9)
random_2= random.randint(1,9)
counter = 0
for i in range(1,100):
    if sum([int(x) for x in str(i)]) % random_2 == 0:
        print(i, random_2)
        counter+=1
    elif counter>=5:
        break

#Задания для самостоятельной работы
#Задание 1.
import random
def coin_side(num):
    if num == 1:
        return 'Решка'
    elif num == 0:
        return 'Орел'

tries = int(input("Введите количество попыток"))
list_of_tries = [random.randint(0,1) for i in range(tries)]
for t in list_of_tries:
    print(coin_side(t))


#Задание 2.
import random

tries = int(input("Введите количество попыток"))
list_of_tries = [random.randint(1,6) for i in range(tries)]
for t in list_of_tries:
    print(t)


#Задание 3.
import string
import random
lenght = int(input('Введите длину пароля'))
alphabet = list(string.ascii_lowercase+string.ascii_uppercase)
password = ''
for i in range(lenght):
    password+=random.choice(alphabet) 
print(password)
