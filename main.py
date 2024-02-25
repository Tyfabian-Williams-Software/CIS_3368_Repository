read from console
value = input("Please enter a string: \n")

output this directly as part of the string 
print(f'You entered {value}')

output with placeholders
message = "You entered %s" %(value)
print(message)

output with +
print("You entered " + value)

dictionaries
mydict = {
    "firstname": "Jane",
    "lastname": "Doe",
    "birthyear": 2001
}

print(mydict)
print(mydict['firstname'])
print(mydict['birthyear'])

fname = mydict.get("firstname")
print(fname)

mydict = {
    "firstname": "Jane",
    "lastname": "Doe",
    "birthyear": 2001,
    "children": ["Jack", "John", "James"]
}
print(mydict)

mydict["birthyear"] = 2000
print(mydict)

mydict.update({"birthyear": 1900})
print(mydict)

if "children" in mydict:
    print("This person has children")

mydict["father"] = "jeff"
print(mydict)

mydict.pop("father")
print(mydict)

mydict["father"] = "jeff"
del mydict["father"]

print(mydict)

mydict.clear()
print(mydict)

lists
ordered, changeable, allow duplicates, allow different data types
mylist = ['apple', 'kiwi', "pear"]
print(mylist)

mylist = ['apple', 'kiwi', "pear", "apple", "apple"]
print(mylist)

print(len(mylist))

mylist = [100, 15, 77, 99, 300]
print(mylist)

mylist = [False, False, False, True]
print(mylist)
mylist = ["Apple", 300, True, 400, "alex", [1,2,34,5,6]]
print(mylist)

print(mylist[1])
print(mylist[-1]) #item at the end of the list

print(mylist[2:5]) #range
print(mylist[:5]) #range from the start
print(mylist[-4:-1]) 

if "alex" in mylist:
    print("alex is part of the list")

if "monica" in mylist:
    print("monica is part of the list")
else:
    print("monica is not in the list")

mylist[1] = 500
print(mylist)

mylist.insert(2, "Totally unrelated string")
print(mylist)

mylist.append("YELLOW")
print(mylist)

more_colors = ["red", "blue", "green"]
mylist.extend(more_colors)
print(mylist)

mylist.pop(0) #removes item at index
print(mylist)

del mylist[-1]
print(mylist)

for x in mylist: #loop through the list
    print(x)

#mylist.sort() this will error, cannot sort with different data types
    
mylist = ["red","orange", "blue","green","black"]
print(mylist)

mylist.sort()
print(mylist)

mylist.clear()
print(mylist)

tuple & set
