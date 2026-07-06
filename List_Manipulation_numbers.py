#List Manipulation
#Length of the list
# numbers = 4,5,6,7
# # print(numbers)
# a = len(numbers)
# print(a)
# print(len(numbers))
#==========================================================
#concatenate 2 lists / merge 2 list
# list1 = [1,2,3]
# list2 = [4,5,6]
# list3 = list1 + list2
# print(list3)
#Merge 2 List using 2 extend
#list2.extend(list1)
#print(list2)
#Concatenate two lists index-wise
# list1 = ["Guru", "shakar", "Guru"]
# list2 = ("Kumar", "Guru", "Brahma")
# result = [x + y for x, y in zip(list1, list2)]
# print(result)
#Concatenate two lists in the following order
# list1 = ["Guru", "Shakar", "Guru"]
# list2 = ("Kumar", "Guru", "Brahma")
# result = [x + y for x in list1 for y in list2]
# print(result)
#Iterate both lists simultaneously
numlist1 = ["A", "B", "C"]
numlist2 = [1, 2, 3]
for num, result in zip(numlist2, numlist1):
    print(num, result)

#============================================================
#Repeat list
# list4 = [5,6,7]
# print(list4 * 3)
#=============================================================
#Sort/assending/descending
#array = [10,20,40,14,81,1]
# array.sort() #arrange in ascending order
# print(array)
# print(array.pop(3)) #remove/pop 81 (last number in array)
# print(array)
# #descending order
#array.reverse() #reverse
#print(array)
# array.sort(reverse=True)#descending order
# print(array)
#=================================================================
#Copy and Index in the below array
# number = [1,8,7,6,4,9,6,8,9,8]
# number2 = number.copy()
# print(number)
# print(number2)
# #count number of occurrence of same number
# print(number.count(9))
# #Find the index of the number/string (ex.9) given in array
# print(number.index(9)) #answer was 5
#===================================================================
#list Slicing
# number = [1,2,3,4,5,6]
# print(number)
# first_slic = number[1:4]
# print(first_slic)
# print(number[:5])
# print(number[3:])
#======================================================================
#List comprehension or multiple with the same numer.
#numbers = [1,2,3,4,5,6]
# #print(numbers)
# squares = [x*x for x in numbers]
# print(squares)
# squares = [] #empty table
# for item in range(1,5):
#     squares.append(item*item)
# print(squares)
#Cube each number in a list
# numList = [2,3,4,6,1]
# cube = [x**3 for x in numList]
# print(cube)
#Even number from the list
# numList = [2,3,4,6,1]
# evenList = [x for x in numList if x % 2 == 0]
# print(evenList)
# #odd
# evenList = [x for x in numList if x % 2 != 0]
# print(evenList)
# #greater than 3
# greatList = [x for x in numList if x > 3]
# print(greatList)
#remove negative number
# Numbers = [-2,4,-4,6,7,9,-7]
# negNum = [x for x in Numbers if x >= 0]
# print(negNum)
#===============================================================================
#Access elements
# numbers = [1,2,3,4,5,5,6]
# print(numbers[2])
# print(numbers[-1])
# print(numbers[-2])
#====================================================================================
#Sum and Average of all the number of the list
#NumList = [3,5,6,7,8]
#sum1 = sum(NumList)
#print(sum1)
#Average = sum(NumList) / len(NumList)
#print(Average)
#===================================================================
#Square
# NumList1 = [3,5,6,7,8]
# square = [x*x for x in NumList1]
# print(square)
#=============================================================
#Find Maximum and Minimum
# List1 = [3,5,6,7,8]
# Maximum = max(List1)
# print("Maximum is ", Maximum )
# Minimum = min(List1)
# print("Minimum is", Minimum)
#===============================================================
#Count occurrence
# list2 = [2,4,6,1,5,3,2,5]
# occu = list2.count(5)
# print(occu)
# count1 = [list2.count(x) for x in list2]
# print(count1)
#========================================================================
#Sort of a list
# slist2 = [2,4,6,1,5,3,2,5]
# slist2.sort()
# print(slist2)
#=============================================================
#Create a copy of a list
# clist2 = [2,4,6,1,5,3,2,5]
# clist1 = clist2.copy()
# print(clist1)
# print(clist2)
#================================================================
#Combine 2 list
# list1 = [2,4,5,6,7,8]
# list2 = [9,8,7,6,5,4]
# list = list2 + list1
# print(list)
#===============================================================
#Remove duplicate from the list
# dlist2 = [2,4,6,1,5,3,2,5]
# dlist1 = list(set(dlist2)) #after removing duplicate and arrange it in ascending
# print(dlist1)
# dlist1 = list(dict.fromkeys(dlist2)) #this will not disturb the originality
# print(dlist1)
#=================================================================================
#Remove all occurrences of a specific item from a list
# dlist2 = [2,4,6,1,5,3,2,5]
# item_remove = 2
# result = [item for item in dlist2 if item != item_remove]
# print(result)
#===========================================================
#interview question
# x = 10
# def func():
#     x = 5
#     return [x * i for i in range(3)]
# result = func()
# print(result)
# print(x)
#============================================================================
#Access Nested list/Matrix
matrix = [
    [4,6,1],
    [1,2,3],
    [6,7,8]
]
# print(matrix[0][1])
# print(matrix[1][2])
# print(matrix[2][0])
# print(matrix[-1][-1]) #last element
# matrix[2][2] = 25
# print(matrix[2][2])
#Flatten Nested List in Python / converting nested list into single list
# flatlist = []
# flatlist = [x for subtile1 in matrix for x in subtile1]
# print(flatlist)
#=====================================================================

