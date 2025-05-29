#upper cone
for i in range(5):
    for j in range(4-i):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()

for i in range(5*3):
    print(end='  ')
    for j in range(5): 
        print('*',end='')
    for k in range(5*3):
        if i<5 or i>10:
         print(' ',end='')
        else:
            print('*',end='')
    for l in range(5):
        print('*',end='')
    print()
for i in range(5):
    for j in range(5*4):
        print(' ',end='')
    for k in range(i):
        if i==0:
            break
        else:
            print(' ',end='')
    for l in range(9-2*i):
        print('*',end='')
    print()