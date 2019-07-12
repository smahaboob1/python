#!/usr/bin/python
print "Create and Print list"
list1=["Honda","Toyota","Tesla","BMW"]
print "printing list",list1
print "print list length",len(list1)

print ""
print "Accessing list items"
print list1[0]
print list1[1]
print list1[2]
print list1[3]


print ""
print "Updating list"
print "list before update",list1
list1[0]="Suzuki"
print "list after upate  ",list1


print ""
print "List though using for loop"
for i in list1:
    print "Values of list",i

print ""
print "List though for loop using and index"
for i in range(len(list1)):
    print "Values of list: ",list1[i]

print ""
print "Check if Item Exists using for loop"
for i in list1:
    if (i == 'BMW'):
        print "BMW is exists"
        break;
else:
    print "All other items",list1

print ""
print "Check if Item Exists using if condition"
if 'BMW' in list1:
    print "BMW is available in list"
else:
    print "BMW is not available in list"

print(list1)

print ""
print "Add new items to list"
list1.append("ABCD")
for i in list1:
    print(i)

print ""
print "Remove List Items"
list1.remove("ABCD")
print "list after removing ABCD",list1
list1.append("ABCD")
print "list after adding ABCD",list1
print ""
print "Removing using pop"
list1.pop()
print "list after removing ABCD",list1
list1.append("ABCD")
print "list after adding ABCD",list1
print ""
print "Removing using del"
del list1[0]
print "list after removing ABCD",list1
list1.append("ABCD")
print "list after adding ABCD",list1


