#Dictionary Exercises.
#Exercises 1/24 : Perform basic dictionary operations
from pdb import test

office = {
    "name": "Intel",
    "year": 1990
}
#print(office)
# print(office.keys())
#print(office.values())
#print(office.items())
#Dictionary iterate
# for key, value in office.items():
#     print(key, value)
#check Key exists
# print("name" in office)
# print("salary" in office)
# #Dictionary Length
# print("Length", len(office))
#copy dict
# new_office = office.copy()
# print("new office", new_office)
#==========================================================================
# #clear
# office.clear()
# print("clear",office)
#================================================================
#Merge 2 dictionaries:
dict1 = {"Guru": 33, "shankar": 25}
dict2 = {"balu": 22, "Pandu": 27, "shankar": 29}
dict2.update(dict1)
#print(dict2)
#--------------------------------------------------------------------
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
# dict1.update(dict2)
# print(dict1)
#========================================================================
#Nested Dictionary
student = {
    "student1" : {
    "name": "Guru",
    "age": 21
    },
    "student2" : {
    "name": "raj",
    "age": 24
    }
}
#print("Len of Student/Dictionary", len(office))
# print(student)
# print(student["student1"] ["name"])
# print(student["student2"]["age"])
# print(student.items())

#Print the value of key ‘history’ from nested dict
# Sample_dict = {
#     "class": {
#         "student":{
#             "name":"Guru",
#             "markd":{
#                 "history" : 88,
#                 "Hindi" : 99,
#                 "English" : 96
#             }
#         }
#     }
# }
# print(Sample_dict["class"]["student"]["markd"]["Hindi"])
#
# #Modify Nested Dictionary
# Sample_dict["class"]["student"]["markd"]["English"] = 98
# print(Sample_dict["class"]["student"]["markd"]["English"])
#============================================================================
#dictionary from the list
key = ["Guru", 33, "shankar", 25]
value = ["balu", 22, "Pandu", 27]
dict3 = dict(zip(key, value))
# #print(dict3)

# #from the loop
key = ["Guru", 33, "shankar", 25]
value = ["balu", 22, "Pandu", 27, "shankar", 80]
student4 = {}
# for key, value in zip(key, value):
#     student4[key] = value
#print(student4)
for i in range(len(key)):
    student4[key[i]] = value[i]
print(student4)
#Output -> {'Guru': 'balu', 33: 22, 'shankar': 'Pandu', 25: 27}
#=============================================================================
#Merge two Python dictionaries into one
office1 = {
    "name" : "Intel",
    "year" : 1990,
    "HeadCount" : 8000000
}
office2 = {
    "n" : "AMD",
    "y" : 1995,
    "h" : 3500000
}
#1st method
# office3 = dict(zip(office1, office2))
# print(office3) #This is the right method O/p: {'name': 'name', 'year': 'year', 'Head Count': 'Head coumt'}
# office1.update(office2)
# print(office1)
# #2ns Method
# for key, value in office1.items():
#     office2[key] = value
# print(office2)
# #3rd method
# office3 = office1 | office2
# print(office3)

#Count Character Frequencies in Dictionary
# text = "programming"
# result = {}
#
# for char in test:
#     if char in result:
#         result[char] += 1
#     else:
#         result[char] = 1
# print(result)
#=========================================================================================================
#Count Character Frequencies in Dictionary
