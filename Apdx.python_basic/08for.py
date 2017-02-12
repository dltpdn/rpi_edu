print range(10)
for i in range(10):
    print i

print range(5,-1, -1)

names = ['aaa', 'bbb', 'ccc']
names.append('ddd')

for i in range(len(names)):
    print i, 'th :', names[i]
    
print '-'*80

print range(0,10, 1) 
print range(10,0, -1) 
print range(10,-1, -1) 
for i in range(len(names)-1, -1, -1):
    print i, names[i]
    
    
friends = [{'name':'aaa', 'isMan' : True, }, {'name':'bbb', 'isMan':False}, {'name':'ccc', 'isMan':False}, {'name':'ddd', 'isMan':True}]
for i in range(len(friends)-1, -1, -1):
    if(friends[i]['isMan'] == False):
        del friends[i]
        #friends.remove(friends[i])
        print i, 'removed'
