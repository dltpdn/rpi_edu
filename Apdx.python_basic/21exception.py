import sys

class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg


def plus(a, b):
    if a >= 0 or b >= 0 :
        return a + b
    else:
        raise MyException('negative parameter')
    
try:
    print plus(1,2)
    print plus(-1,-2)
except Exception as e:
    print e.msg
    print sys.exc_info()