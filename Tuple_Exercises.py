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
#temp[1] = 100
#print(temp)
tup = tuple(temp)
#print(tup)
#========================================================
#Slicing Tuples
tup1 = (30,20,10,40,60)
#print(tup1[1:3])
#print(tup1[:3])
#print(tup1[2:])
#==========================================================
#Reverse the tuple
tup2 = (30,50,50,60,2)
tup3 = tuple(reversed(tup2))
#print(tup3)
#using start-> stop-> step ::=-1 Slicing technique
tup4 = tup2[::-1]
#print(tup4)
#========================================================
#Sum and average of a tuple
tuplle = (20,20,30,10)
#print(sum(tuplle))
#print(sum(tuplle)/len(tuplle))
#===========================================================
#Access nested Tuple
ntuplle = ((20,20,30,10),
           (3,5,6,7),
           (9,6,3,8,2)
           )
#print(ntuplle[0][3])
#print(ntuplle[2][4])
#======================================================
#Create a tuple with single item 50
stuple = (50,)
#print(stuple)
#print(type(stuple))
#=========================================================
#Unpack the tuple into 4 variables
utuple = ("Guru","Office",9,"Winner")
name, office, number, win = utuple
# print(name)
# print(win)
# print(office)
# print(number)
#========================================================
#Swap two tuples in Python
swapTup1 = (10,20,40)
swapTup2 = (20,50,60)
swapTup1, swapTup2 = swapTup2, swapTup1
# print(swapTup1)
# print(swapTup2)
#=======================================================
#Copy Specific Elements From Tuple
swapTup1 = (10,20,40)
copy = swapTup1[2]
#print(copy)
#or
copytup =  swapTup1[1],swapTup1[2],swapTup1[0]
#print(copytup)
#=====================================================
#Function Returning Tuple
def funTuple(tup):
    #print(tup)
    temp = list(tup)
    temp[1] += 1
    #print(temp)
    tup = tuple(temp)
    return tup

tuple5 = (6,22,9,2)
tumple = funTuple(tuple5)
#print(tumple)
#================================================================
#Comparing Tuples
comtup1 = (10,'harrays',40)
comtup2 = (10,'gurur',60)
#print(comtup1 > comtup2)
#========================================================
#Removing Duplicates from Tuple
duptup = (2,5,7,'hello',5,2)
duptup = tuple(set(duptup))
#print(duptup)
#=========================================================
#Filter Tuples
filtup = (3,5,6,8,2)
resulttup = tuple(x for x in filtup if x%2 == 0)
#print(resulttup)
#using Loop
countftl = ()
for x in filtup:
    if x%2 == 0:
        countftl += (x,)
print(countftl)
#================================================================
#Map Tuples
maoTuple = (3,4,5,6,2,6)
mapTuple = tuple(map(lambda x: x*2, maoTuple))
#print(mapTuple)
#using generators
maoTuple = tuple(i*2 for i in maoTuple)
print(maoTuple)
#================================================================
#Sort a tuple of tuples by 2nd item -> pending
sorttupl = (
    ('john',5),
    ('guru',7),
    ('deva',1)
)
#=======================================================
#Count Elements
eletuplr = (10,20,30,30,350)
elelen = len(eletuplr)
print(elelen)
elelen = eletuplr.count(30)
print(elelen)
#===============================================================
#Check if all items in the tuple are the same
sametupl = (5,5,5,5,5,5)
same = True
# for x in sametupl:
#     if x!= sametupl[x]:
#         same = False
#         break
# print(same)
#second method using set (duplicate numbers remove)
if len(set(sametupl)) == 1:
    print("All elements are same")
else:
    print("Not same")
#==========================================================================
