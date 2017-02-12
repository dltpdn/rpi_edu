count1 = 0
while count1 < 10:
    print count1
    count1 += 1
    
    
    
names = ['aaa', 'bbb', 'ccc']
names.append('ddd')
names.append('eee')

idx = 0
while idx < len(names):
    print idx, ':' , names[idx]
    idx+= 1


idx = len(names)-1
while idx >= 0:
    print idx, ":", names[idx]
    idx -= 1
