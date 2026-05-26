#1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)
for game in sport_games:
    print(game)

#2
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

#3
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    print(student)

#4
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print('У них есть собака, которую я хочу!')
        break

#5
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for shops in sales_data:
    for types in shops:
        scoops_sold += types
print(scoops_sold)

#6
single_digits = list(range(0,10))
squares = []
for digit in single_digits:
    squares.append(digit**2)
    print(digit)
print(squares)
cubes = [i**3 for i in single_digits]
print(cubes)