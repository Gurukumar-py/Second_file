#Dictionary Exercises.
#Exercises 1/24 : Perform basic dictionary operations
from pdb import test
from selectors import SelectSelector

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
#print(dict3)
#o/p: {'Guru': 'balu', 33: 22, 'shankar': 'Pandu', 25: 27}
# #Using from the loop
key = ["Guru", 33, "shankar", 25]
value = ["balu", 22, "Pandu", 27, "shankar", 80]
student4 = {}
# for key, value in zip(key, value):
#     student4[key] = value
#print(student4)
for i in range(len(key)):
    student4[key[i]] = value[i]
#print(student4)
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
text = "programming"
result = {}

for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1
#print(result)
#=========================================================================================================
#Initialize dictionary with default values
# keyList = ["name", "Hero", "Brahma", "School"]
# #resultlist= {}
# resultlist = dict.fromkeys(keyList, "N/A")
# print(resultlist)
# resultlist = dict.fromkeys(keyList, 55)
# print(resultlist)
#==========================================================================
dict1 = {"arun": 33, "c": 25}
dict2 = {"b": 22, "d": 27}
dict1.update(dict2)
#print(dict1)
#==========================================================================
#Create a dictionary by extracting the keys from a given dictionary
# sample_dict = {
#     "name": "Guru",
#     "age": 30,
#     "salary": 80000,
#     "city": "Hyderabad"
# }
# keys = ["name", "salary"]
# result = {}
# for i in keys:
#     result[i] = sample_dict[i]
# #print(result)
# #=====================================================================
# #Delete a list of keys from a dictionary
# sample_dict1 = {
#     "name": "Guru",
#     "age": 30,
#     "salary": 80000,
#     "city": "Hyderabad"
# }
# del_keys = ["name", "salary"]
# for i in del_keys:
#     del sample_dict1[i]
#print(sample_dict1)
#==============================================================
#Check if a value exists in a dictionary
# sample_dict1 = {
#     "name": "Guru",
#     "age": 30,
#     "salary": 30,
#     "city": "Hyderabad"
# }
# values = 30
# for i in sample_dict1:
#     if values == sample_dict1[i]:
#         #print(f"Present {i} ")
# #To find the key
# key = "city"
# for i in sample_dict1:
#     if i == key:
#         #print("Present", sample_dict1[i])

#=====================================================================
#Rename key value of a dictionary
# sample_dict1 = {
#     "name": "Guru",
#     "age": 30,
#     "salary": 30,
#     "city": "Hyderabad"
# }
# keyren = "city"
# for i in sample_dict1:
#     if i == keyren:
#         sample_dict1[i] = "Bengaluru"
#         print(sample_dict1)
#Rename key of a dictionary
sample_dict2 = {
    "name": "Guru",
    "age": 30,
    "salary": 30,
    "city": "Hyderabad"
}
sample_dict2["new_city"] = sample_dict2.pop("city")
#print(sample_dict2)
#================================================================================
#Get the key of a minimum value
sample_dict4 = {
    "name": 2,
    "age": 30,
    "salary": 3,
    "city": 1
}
min1=0
max1=0
for i in sample_dict4:
    if max1 < sample_dict4[i]:
        max1 = sample_dict4[i]
    else:
        min1 = sample_dict4[i]
#print(min1)
#print(max1)
l1 = [1,2,3,4,5]
min1 = min(sample_dict4.values())
#min1 = min(l1)
#print(min1)
#==============================================================================
#Change value of a key in a nested dictionary
netdict1 = {
    "student" :
    {
    "num1" : 1,
    "num2" : 2,
    "num3" : 3
    },
    "student2" :
    {
    "num4" : 4,
    "num5" : 5,
    "num6" : 6
    }
}
netdict1["student"]["num3"] = 30
#print(netdict1)
#====================================================================================================
#Invert Dictionary
school = {
    'student' : 'Brahma',
    'student1' : 'shankar',
    'student2' : 'guru'
}
inverted = {value: key for key, value in school.items() }
#print(inverted)
#Invert Dictionary using loop
school = {
    'student' : 'Brahma',
    'student1' : 'shankar',
    'student2' : 'guru'
}
inverted = {}
for key, value in school.items():
    inverted[value] = key
#print(inverted)
#===================================================================================
#Sort Dictionary by Keys
# school1 = {
#     'zapple' : 3,
#     'xba' : 23,
#     'ycaa' : 12
# }
# #sorted1 = {}
# sorted1 = dict(sorted(school1.items()))
# print(sorted1)
#=========================================================================
#Sort Dictionary by keys
# school1 = {
#     'xpple' : 3,
#     'ba' : 23,
#     'caa' : 12
# }
# for ilu in sorted(school1.keys()):
#     print(ilu,':', school1[ilu])

#===============================================================
#Sort Dictionary by values


#================================================================
#Check if All Values are Unique in dictinoary
leng = {
    'a' : 3,
    'b': 4,
    'c': 5
}
if len(leng.values()) == len(set(leng.values())):
    print("All values are unique")
else:
    print("Some values are not unique")
#print(len(set(leng.values())))
#print(len(leng.values()))
#========================================================================
#Sorting the dictionary using bubble sort method
d1 = {'mani':12, 'satya':3000, 'chinni':300}
l1=list(d1.items())
print("Before sorting", l1)
for i in range(len(l1)):
    for j in range(len(l1)):
        if l1[i][1] < l1[j][1]:
            l1[i],l1[j] = l1[j],l1[i]
print("After sorting", l1)
print("Converting to dict", dict(l1))