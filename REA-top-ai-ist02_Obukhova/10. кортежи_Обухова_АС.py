marks = (1,2,3,2,1,2,1,3,1,2,1,2,3,3,2,1,2,1,2,1)
ans = []
for i in range(20):
    a = int(input())
    ans.append(a)
if marks == ans:
    print('Экзамен сдан')
else:
    print('Экзамен провален')