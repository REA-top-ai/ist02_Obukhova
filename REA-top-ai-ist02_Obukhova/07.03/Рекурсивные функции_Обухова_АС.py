#Задание
def find_factorial_rec(num):
    if num==1:
        return 1
    return num*find_factorial_rec(num-1)

def find_factorial(num):
    res = 1
    for i in range(1,num+1):
        res*=i
    return res

print(find_factorial_rec(5))
print(find_factorial(5))

#Задание
def square(spisok):
    res = [el**2 for el in spisok]
    return res
print(square(list(map(int,input().split()))))