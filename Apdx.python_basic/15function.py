# -*- coding:utf-8 -*-

def test1():
    pass

test1()

def test2():
    print "test2"
test2()

def test3(a):
    print "test3",a

test3("abc")
test3(999)

def test4(arg1, arg2):
    print "arg1:",arg1
    print "arg2:",arg2

test4("one", "two")
result1 = test4("three", "four")
print "result1:",result1

def test5():
    print "test5()"
    return

def test6():
    print "test6()"
    return None

result2 = test5()
result3 = test6()
print "result2:",result2
print "result3:",result3

def getSum(num1, num2):
    result= num1+num2
    return result

print getSum(10, 20)
f1 = getSum
print f1(1,2)

def showSum(num1, num2):
    result = num1+num2
    print "showSum:",result

showSum(100, 200)

def test7(*args):
    print args

test7()
test7(10)
test7("one","two","three")
test7(10,20,30,40,50)

def test8(arg1, *args):
    print "arg1:",arg1
    print "args:",args

test8("aaa")
test8("aaa","bbb")
test8("aaa","bbb","ccc")

def test9(num=0):
    print "num:",num

test9()
test9(999)

formatStr = "No:{} name:{} addr:{}".format(1, "lee", "seoul")
print formatStr

def test10(num=0, name="Lee", addr="Seoul"):
    result="No:{} name:{} addr:{}".format(num, name, addr)
    print result

print test10()

def test11(**kwargs):
    print type(kwargs)
    print "kwargs : ",kwargs

test11()
test11(num=1)
test11(num=2,name="Park",addr="Ilsan")

def test12(arg1, *args, **kwargs):
    print "arg1:",arg1
    print "args:",args
    print "kwargs",kwargs

test12(999)
test12(999,"one","two","three")
test12(999,"one","two","three",num=3,name="monkey",addr="seoul")
