#remove elements in a set (pop, remove, update, )
from shlex import split

a= {7,1,2,3,1,7,2,0}
c = {5,2,7,4}
#print(a) #wil remove common elements
# # b = a.pop() #1st element will be removed
# # print(a)
# #remove in set
for x in c:
    if x in a:
        a.remove(x)

# a.remove(0)
#print(a)
# a.discard(2)
# print(a)
#===============================================================
#Union of Sets (or |) combined 2 set
A = {4,5,7,8}
B = {7,8,9,4} #4,5,7,8,9
C = A | B
#print(C) #4,5,7,8,9
#==============================================================
#Intersection of Sets (AND &) Common element -> {8,20}
C = {10,20,30,8,50}
D = {90,8,8,80,20}
E = D & C
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
#===================================================================
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
#print(sim1)
#================================================================
#Check Subset (A subset is a set whose every element is present in another set.)
#Subset (⊆) → Small set inside a larger set.
subset1 = {1,4,6,9,10}
subset2 = {9,6,4,2,6,10,1}
#print("subset:",subset1.issubset(subset2))
#=================================================================
#Check Superset: A superset is a set that contains all the elements of another set.
#A set B is a superset of A if B contains every element of A. Superset (⊇) → Larger set containing a smaller set.
supsubset = {1,4,6,9,10}
subsubset1 = {1,4,6,9,10,13,14}
#print("Superset:",supsubset.issuperset(subsubset1))
#=================================================================
#Set Intersection Check: A set intersection check determines whether two sets have at least one common element.
interset1 = {1,4,6,9,10}
interset2 = {9,6,4,2,1,6,10}
if interset1.intersection(interset2):
    print("sets intersect")
else:
    print("sets not intersect")
#=================================================================================
#Set Symmetric Difference Update
#The symmetric difference contains elements that belong to only one of the two sets.
syssets1 = {1,4,6,9,10}
syssets2 = {9,6,4,2,6,10,1}
syssets1.symmetric_difference_update(syssets2)
#print("set1:",syssets1) # set1: {2}
#==============================================================================
#Set Intersection Update
#The intersection_update() method updates a set so that it contains only the elements that are common to both sets.
intset1 = {10,6,3,7,2,1}
intset2 = {9,6,4,2,6,10,1} #result of intersection {1, 2, 3, 6, 7, 10}
set.intersection_update(intset1,intset2)
#print(intset1) #result od intersection_update {1, 2, 10, 6}
#=================================================================================
#Find Common Elements in Two Lists
eleset1 = [1,4,6,9,10]
eleset2 = [9,6,4,2,6,10,1]
result3 = list(set(eleset1) & set(eleset2)) #[1, 4, 6, 9, 10]
#print(result3)
#==========================================================================
#Frozen Set : immutable version of a set, Unordered, Cannot be modified after creation
froset = [6,2,6,3,7,9,10,11]
result5 = frozenset(froset) #this will modifine to set or {}
#print(result5) #frozenset({2, 3, 6, 7, 9, 10, 11})
#==============================================================================
#Count Unique Words
text = "apple banana apple orange banana mango"
settext = split(text) #convert to list, #['apple', 'banana', 'apple', 'orange', 'banana', 'mango']
print(settext)
unique_words = set(settext) #{'mango', 'banana', 'apple', 'orange'} -> convert it to set
print(unique_words)
#==========================================================================================














