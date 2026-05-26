# Задание
favour_word = 'фяфяфя'
print(favour_word)


# Задание
first_name = 'Виталий'
last_name = 'Красилов'
new_account = last_name[:5]
temp_password = last_name[2:6]
print(temp_password)


# Задание
first_name =input('Введите имя')
last_name = input('Введите фамилию')
def account_generator(a,b):
    return a[:3]+b[:3]
new_account = account_generator(first_name,last_name)


#Задание
first_name =input('Введите имя')
last_name = input('Введите фамилию')
def password_generator(a,b):
    return a[-3:]+b[-3:]
temp_password = password_generator(first_name,last_name)


#Задание
company_motto= 'Мечты сбываются'
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(final_word)


#Задание
first_name = 'Боб'
# first_name[0] = "Р"
fixed_first_name = 'Р' + first_name[1:]
print(fixed_first_name)


#Задание
password = "theycallme\"crazy\"91"


#Задание
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()
print(poem_title,poem_title_fixed)