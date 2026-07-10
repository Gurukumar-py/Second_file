#====================================================
#Tuple Unpacking
tuple1 = ('guru', 30, 'deva')
name, age, place = tuple1
#print(name, age, place)
#========================================================
#Swap Variables Using Tuples
a=10
b=20
a,b = b,a
#print(a, b)
#========================================================
#Modify Tuple indirectly
tup = (20, 30, 40)

temp = list(tup)
temp[1] = 100
tup = tuple(temp)
#print(temp)
#========================================================
#Slicing Tuples
tup1 = (30,20,10,40,60)
print(tup1[1:3])
print(tup1[:3])
print(tup1[2:])
#==========================================================
#Reverse the tuple
tup2 = (30,50,50,60,2)
