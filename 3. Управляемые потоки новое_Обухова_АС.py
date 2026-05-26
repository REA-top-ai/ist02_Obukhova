# Задание
print((6 * 6) - 1 >= 8 + 1 )
print(13 - 7 <= (3 * 2) + 1 )
print(3 * (2 - 1) > 4 - 1 )


# Задание
bool_variable = 'true'
print(type(bool_variable))
bool_variable_2 = True
print(type(bool_variable_2))


# Задание
user_name = input("Введите имя")
Dmitriy_check = ("Дмитрий, твое рабочее место находится в другой комнате. "
                 "Отойди от чужого компьютера и займись работой!")
user_check = "Добро пожаловать"
if user_name == "Дмитрий":
    print(Dmitriy_check)
else:
    print(user_check)

enter_number = 0
if enter_number < 3:
    print(f'Попробуйте еще раз. У вас осталось {3- enter_number} попыток')
if enter_number >= 3:
    print('Вы превысили максимальное число попыток. Ваша учетная запись заблокирована. '
          'Для разблокировки обратитесь в службу поддержки')


# Задание
#1
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)
#2
Dmitriy_APM = 1
Angelina_APM = 2
Vasiliy_APM = 3
Ekaterina_APM = 4
ARM = int(input())
if (ARM == Dmitriy_APM and user_name=='Дмитрий') or (ARM == Angelina_APM and user_name=='Ангелина') or (ARM == Vasiliy_APM and user_name=='Василий') or (ARM == Ekaterina_APM and user_name=='Екатерина'):
    print('«Добро пожаловать!')
elif user_name != 'Дмитрий':
    print('Логин или пароль не верный, попробуйте еще раз')
elif user_name == 'Дмитрий':
    print('Дмитрий, твое рабочее место находится в другой комнате. '
          'Отойди от чужого компьютера и займись работой!')


# Задание
print((2 - 1 > 3) or (-5 * 2 == -10) )
print((9 + 5 <= 15) or (7 != 4 + 3) )


# Задание
grade = float(input('Введите средний балл'))
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