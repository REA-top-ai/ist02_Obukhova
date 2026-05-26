#1
spisok = ['торт',1]

#2
household_chemicals = [['laundry',1],['dishes',1]]

#3
Names=["Ben", "Holly", "Ann"]
dogs_names= ["Sharik", "Gab", "Beethoven"]
names_and_dogs_names = zip(Names,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

#4
orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders)

#5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень','ирис']
print(new_orders)
broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

#6
list1=[1,8]
list1 = list(range(9))
print(list1)
list2 = list(range(7))

#7
list1 = list(range(5,16,3))
print(list1)
list2 = list(range(0,40,5))
print(list2)

#8
first_names = ['Эйнсли','Бен','Чани' ,'Депак']
age = []
age.append(42)
all_ages = [32,41,29] + age
name_and_age = list(zip(first_names,all_ages))
ids = list(range(4))