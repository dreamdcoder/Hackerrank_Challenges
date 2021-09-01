import math

for i in range(1 ,int(input() ) +1):
    p = 1
    for j in range(1,i+1) :
        print(F"{p}", end='')
        p += 1
    p -= 1
    while p > 1:
        p -= 1
        print(F"{p}", end='')
    print()

