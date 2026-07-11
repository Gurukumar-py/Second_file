#remove elements in a set (pop, remove, update, )
# a= {7,1,2,3,1,7,2,0}
# print(a) #wil remove
# # b = a.pop()
# # print(a)
# #remove in set
# a.remove(0)
# print(a)
# a.discard(2)
# print(a)
#===============================================================
#Union of Sets (or |) combined 2 set
A = {4,5,7,8}
B = {7,8,9,4} #4,5,7,8,9
C = A | B
#print(C) #4,5,7,8,9
#==============================================================
#Intersection of Sets (AND &) Command element -> {8,20}
C = {10,20,30,8,50}
D = {90,8,8,80,20}
E = C & D
#print(E)
#=============================================================
#Difference of Sets
#The difference of two sets returns the elements that are present in the first set but not in the second set.
# F= {1,4,6,9,10}
# G = {9,6,4,2,11} #{1,2,4,6,9}
# H = F - G
# print(H) #-> prest in 1st not in second -> 1,10
#================================================================
#Symmetric Difference (^) Elements present in either set, but not both.
# F= {1,4,6,9,10}
# G = {9,6,4,2,11} #{1,2,4,6,9}
# H = F ^ G
# print(H) #-> 1, 2, 10, 11
#=====================================================
#Add a list of Elements to a Set
F= {1,4,6,9,10}
F.add(2)
#print(F) #-> 1, 2, 4,6,9,10
#=========================================================
#Set Difference Update
set1 = {1,4,6,9,10}
set2 = {9,6,4,2,11}
set3 = {5,6,8}
#set1.difference_update(set2,set3) #{1,10} (difference common from set (main set only))
set1.difference(set2,set3) #{1,4,6,9,10} keeps common number from main list
#print(set1)
#============================================================
#Remove Items From Set Simultaneously
sim1 = {1,5,7,4,6,8}
sim1.difference_update({7,8,1})
print(sim1)
#================================================================
#Check Subset (A subset is a set whose every element is present in another set.)

