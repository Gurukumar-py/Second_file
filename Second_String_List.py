fruits = ["apple", "Banana","Mango"]
# print("print my fruits", fruits)
# print(fruits[1])
# print(fruits[0])
# print(fruits[2])
#modifying the above list*/
#fruits[1] = "grapes"
#print(fruits)
#append
# fruits.append("water melon")
# print(fruits)
#index
index = fruits.index("Mango")
print(index)
# #insert
fruits.insert(index,"orange")
print(fruits)

#add multiple elements -> extend
# fruits.extend(["papya", "pear"])
# print(fruits)

#remove
# fruits.remove("grapes")
# print(fruits)
#remove by index
# fruits.pop() #remove the last one
# print(fruits)
# fruits.pop(1) #remove the index 1
# print(fruits)

#delete
# del fruits[0]
# print(fruits)

#clear entire list
#fruits.clear()
#print(fruits)

#search if fruit exist in the fruit list
# print("water melon" in fruits)
# print("apple" in fruits)

#Iterates or Loop
# for fruit in fruits:
#     print(fruit)
#==============================================================
#Remove empty strings from the list of strings
#1st method
# fruits = ["apple", "", "banana", "", "mango"]
# result = []
# for item in fruits:
#     if item != "":
#         result.append(item)
# print(result)
# #2nd method same statement in one line
# result = [item for item in fruits if item != ""]
# print(result)
#==========================================================