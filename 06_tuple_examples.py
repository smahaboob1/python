tuple=("red","black","white","blue","orange")
print tuple

print ""
print "Display tuple values using for loop using range"
for i in range (len(tuple)):
    print "Value of {} entry is: {}".format(i, tuple[i])


print ""
print "Display tuple values using for loop"
for i in tuple:
    print "value of tuple is: {}".format(i)

print ""
print "Display tuple values using while loop"
i=0
while(i<len(tuple)):
    print "Value of {} entry is: {}".format(i, tuple[i])
    i+=1
    if (tuple[i] == 'white'):
        break;

print ""
print "Display tuple values using while loop continue"
j=-1
while(j<(len(tuple)-1)):
    j += 1
    if (tuple[j] == 'white'):
        continue;
    print "Value of {} entry is: {}".format(j, tuple[j])

print ""
print "Check if Item Exists "
if "red" in tuple:
    print "Yes red in is tuple"
else:
    print "No red is not in the tuple"

