berta = 12
print ("type of package variable :", type(berta))

import packboy as berta

print("Hello World")
print("Ma couille")

#comment one liner

'''
Hello dude. this is comment format
Multiliner
'''



print ("type of package variable :", type(berta))
print ("type of package attribute :", type(berta.tribulle))


'''
print ("type of module attribute :", type(berta.tribulle.triliste))
print ("type of script.py variable :", type(tribulle))
print ("type of module attribute :", type(tribulle.triliste))
'''


print(berta.__dict__.keys())

listToSort = [1,3,2]
berta.tribulle.triliste(listToSort)

'''
berta.tribulle.triliste(listToSort)
'''

print("now sorted list : ", listToSort)


print("5 + 5", 5+5)
print("5 * 5", 5*5)
print("10 - 5", 10 - 5)
print("5**2 ",5**2)
print("5/2", 5/2)
print("5%2",5%2)
print("5//2", 5//2)

age = 10

if age >= 21 :
    print("you can drive a truck")

elif age>=16 :
    print("you can drive a car")

else:
    print("you cannot drive at all")

for x in range(0,10,1):
    print(" boucle for index : ", x)

aList = [1, 4, 5, 6, 7, 10]
print(aList[2])
print(aList[0:3])
print(aList)

aTuple = tuple(aList)
print(aTuple)

aDictionary = {'name':'chadi', 'game':'programming', 'fame':'tough'}
print(aDictionary)
print(aDictionary['name'])

compNum1 = 1 + 2j
compNum2 = 3 + 5j
compNumAdd = compNum1 + compNum2

print (compNumAdd)
print (type(compNumAdd))

unComp = 0
while (unComp < 10):
    print (unComp)
    unComp = unComp + 1