import mymodule1
import mymodule1 as m1
from mymodule1 import function1

import mypack.mymodule2
from mypack import mymodule2
from mypack.mymodule2 import  function1

mymodule1.function1()
m1.function1()
function1()

mypack.mymodule2.function2()
mymodule2.function2()
#function2()


import random

num = random.randint(1, 6)
print num