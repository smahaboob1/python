a=10
b=20
c=30

# If condition example
print "If condition example"
if (a == 10):
    print "a is equal to 10"

print ""
print "Example for if-else"
if (a > b):
    print "{} is greater than {}".format(a,b)
else:
    print "{} is greater than {}".format(b,a)

print ""
print "Example for nested if"
if (a > b) and (a > c):
    print "{} is greater than {} and {}".format(a,b,c)
elif (b > c):
    print "{} is greater than {} and {}".format(b,a,c)
else:
    print "{} is greater than {} and {}".format(c,a,b)
