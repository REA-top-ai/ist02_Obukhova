#Задание
def f_to_c(f_temp):
    c_temp = (f_temp-32)*5/9
    return c_temp

def c_to_f(c_temp):
    f_temp = c_temp*9/5+32
    return f_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)


#Задание
def get_force(mass,acceleration):
    return mass*acceleration

def get_energy(mass,c = 3 * 10 ** 8):
    return mass*c**2

def get_work(mass,acceleration,distance):
    return get_force(mass,acceleration)*distance

train_mass = 22680
train_acceleration = 10
train_distance = 100
train_force = get_force(train_mass,train_acceleration)
print(train_force)
print(f'Поезд GE поставляет {train_force} ньютонов силы')

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)

print(f'1 кг бомбы составляет {bomb_energy} Джоулей')

train_work = get_work(train_mass,train_acceleration,train_distance)

print(f'Поезд выполняет {train_work} Джоулей за {train_distance} метров')


#Задание
clothes = 'домашняя одежда'
print('У меня большой гардероб')
print(f'Утром лучше всего подходит {clothes}')
print(f'Вечером лучше всего подходит {clothes}')
print(f'Ночью лучше всего подходит {clothes}')

meal = 'мои предпочтения в еде'
print(f"На завтрак я предпочитаю {meal}")
print(f"На обед я предпочитаю {meal}")
print(f"На ужин я предпочитаю {meal}")

def print_clothes(clothes):
    print('У меня большой гардероб')
    print(f'Утром лучше всего подходит {clothes}')
    print(f'Вечером лучше всего подходит {clothes}')
    print(f'Ночью лучше всего подходит {clothes}')

def print_meal(meal):
    print(f"На завтрак я предпочитаю {meal}")
    print(f"На обед я предпочитаю {meal}")
    print(f"На ужин я предпочитаю {meal}")

print_clothes(input())
print_meal(input())


#Задание
def check_user(username):
    Dmitriy_check = ("Дмитрий, твое рабочее место находится в другой комнате. "
                     "Отойди от чужого компьютера и займись работой!")
    user_check = "Добро пожаловать"
    if user_name == "Дмитрий":
        print(Dmitriy_check)
    else:
        print(user_check)

user_name = input("Введите имя")
ARM = int(input('Введите ARM'))

check_user(user_name)


def check_arm(username, APM):
    if username == "Дмитрий":
        if APM == 1:
            print("Добро пожаловать!")
        else:
            print("Дмитрий, твое рабочее место находится в другой комнате. "
                  "Отойди от чужого компьютера и займись работой!")

    elif username == "Ангелина":
        if APM == 2:
            print("Добро пожаловать!")
        else:
            print("Логин или пароль не верный, попробуйте еще раз")

    elif username == "Василий":
        if APM == 3:
            print("Добро пожаловать!")
        else:
            print("Логин или пароль не верный, попробуйте еще раз")

    elif username == "Екатерина":
        if APM == 4:
            print("Добро пожаловать!")
        else:
            print("Логин или пароль не верный, попробуйте еще раз")

    else:
        print("Логин или пароль не верный, попробуйте еще раз")

check_arm(user_name,ARM)


#Задание
def check_grades(grade):
    if grade >= 4.0:
        print('A')
    elif grade >= 3.0:
        print('B')
    elif grade >= 2.0:
        print('C')
    elif grade >= 1.0:
        print('D')
    elif grade >= 0.0:
        print('F')

average_grade = float(input('Введите средний балл'))
check_grades(average_grade)