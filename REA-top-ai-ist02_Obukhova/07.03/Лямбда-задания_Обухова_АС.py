#Задание

contains_a = lambda word: 'a' in word
print(contains_a(input()))

#Задание
long_string = lambda word: len(word)>12
print(long_string(input()))

#Задание
even_or_odd = lambda num: "четное" if num%2==0 else "нечетное"
print(even_or_odd(int(input())))

#Задание
rate_movie = lambda rating: "Мне понравился этот фильм" if rating >= 8.5 else "Этот фильм был не очень хорошим"
print(rate_movie(int(input())))