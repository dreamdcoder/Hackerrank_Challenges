p=0
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    p = i
    for j in range(i):
        print (F"{p}",end='')
    print()


for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10**i//9)*i)