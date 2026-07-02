fruits = ["apple", "Banana","Mango"]

print("print my fruits", fruits)
print(fruits[1])
print(fruits[0])
print(fruits[2])
#modifing the above list*/
fruits[1] = "grapes"
print(fruits)
#append
fruits.append("water melon")
print(fruits)
#insert
fruits.insert(1,"orange")
print(fruits)

#add multiple elements -> extend
fruits.extend(["papya", "pear"])
print(fruits)

#remove
fruits.remove("grapes")
print(fruits)
#remove by index
fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)

#delete
del fruits[0]
print(fruits)

#clear entire list
#fruits.clear()
#print(fruits)

#search if fruit exist in the fruit list
print("water melon" in fruits)
print("apple" in fruits)

#Iterates or Loop
for fruit in fruits:
    print(fruit)