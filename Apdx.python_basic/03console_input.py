input1 = input() #abc
input2 = input() # 123
print(input1, type(input1), input2, type(input2))  #all str

input3 = eval(input()) #'abc'
input4 = eval(input()) #123
print(input3, type(input3), input4, type(input4)) #str, int