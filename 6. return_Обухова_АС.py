#Задание
def define_age(current_year,user_age):
    age = current_year - user_age
    return age

my_age = define_age(2049,1993)
dads_age = define_age(2049,1953)
print(f'Мне {my_age} лет, а моему отцу {dads_age} лет')


#Задание
def get_boundaries(target,margin):
    low_limit = target - margin
    high_limit = margin + target
    return low_limit, high_limit

low_limit, high_limit = get_boundaries(100,20)
print(f'Нижний предел: {low_limit}, верхний предел: {high_limit}')


#Задание
def repeat_stuff(stuff,num_repeats=10):
    returnstatement = stuff * num_repeats
    return returnstatement

lyrics = repeat_stuff('Row',3) + " Your Boat "
song = repeat_stuff(lyrics)
print(song)