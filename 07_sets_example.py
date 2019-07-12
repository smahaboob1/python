print "Create a Set:"
thisset = {"apple", "banana", "cherry"}
print(thisset)

print ""
print "Loop through the set, and print the values:"
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


print ""
print "Check if 'banana' is present in the set:"
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

print ""
print "Add an item to a set, using the add() method:"
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print ""
print "Add multiple items to a set, using the update() method:"
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

print ""
print "Get the number of items in a set:"
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

print ""
print "Remove 'banana' by using the remove() method:"
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


print ""
print "Remove 'banana' by using the discard() method:"
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

print ""
print "Remove the last item by using the pop() method:"
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

print ""
print "The clear() method empties the set:"
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

print ""
print "The del keyword will delete the set completely:"
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)


import os
os.