set1 = {10,20,30,40,50}
print"len(set1) :", len(set1)
set1.add(60)
set1.add(70)
print set1
set2 = {60,70,80,90,100}

resultSet = set1.union(set2)
print"set1 U set2 : ", resultSet
resultSet2 = set1.intersection(set2)
print"set1 n set2 : ", resultSet2
resultSet3 = set1-set2
print"set1 - set2 : ", resultSet3


for item in set1:
    print item


set3={"kim","lee"}
list1 = ["park","cho","lee"]
tuple1 = ("one","two")
set3.update(list1)
print  set3
set3.update(tuple1)
print  set3
set3.discard("park")
print  set3
set3.discard("zzz") 
set3.clear()
print set3


list3 = [10,20,30,10,10,30,40,50,50]
set4 = set(list3)

print"set4 : ",set4
list4 = list(set4)
print"list4 : ",list4
