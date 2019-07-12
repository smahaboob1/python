print "Print 0-5 using while loop"
print "##########################"
i = 0
while (i <= 5):
    print "value of i is = : {}".format(i)
    i += 1;

print ""
print "Print first three values from 1-10 using while loop and break"
print "#############################################################"
i = 1
while (i <= 10):
    print "value of i is: {}".format(i)
    if(i == 3):
        break;
    i += 1;

print ""
print "Print 1-3 and 5-7 values from 1-10 using while loop and continue"
print "#################################################################"
j = 0
while (j <= 10):
    j += 1;
    if (j == 4):
       continue;
    print "value of j is : {}".format(j)
