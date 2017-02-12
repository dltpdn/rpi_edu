import random

for x in range(1,11):
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    print '%d: %d, %d' %(x,n1, n2)
    if n1 + n2 == 7:
        print("seven!")
    elif n1 + n2 == 11:
        print ("eleven")
    if n1 == n2:
        print("double!")
