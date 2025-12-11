thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") 

#Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)


#Add Lists

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#insert items

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove List

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove specific Item

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#using del keyword to remove

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#clearing the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)