friends = ['cat', 'dog', 'elephant', 'snake', 'flog' ]
for item in friends: 
    print item

print friends[0]
friends[1] = 1
friends.append(10)
friends.remove('snake')
del friends[3]
print friends.pop() 

for i in range(len(friends)): 
    print i, ':', friends[i]

