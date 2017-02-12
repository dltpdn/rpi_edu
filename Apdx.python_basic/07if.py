if True:
    print "run!"
if False:
    print "run2!"
  
isWait = False
if isWait:
    print "wait"    
num=10
if num%2==0:
    print "{} is even".format(num)
else:
    print "{} is odd".format(num)

if num>0:
    print "{} is positive".format(num)
elif num<0:
    print "{} is negative".format(num)
else:
    print "{} is zero".format(num)
    
isMan = True
result = "Man" if isMan else 'Women'
print result
