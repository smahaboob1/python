a=20
b=10
c=62
d=30.33

x=True
y=False

#Arithmetic Operators
print "Example of Arithmetic Operators Examples"
print "########################################"
print "a+b = ", a+b
print "a-b = ", a-b
print "a*b = ", a*b
print "a%b = ", a%b
print "a/b = ", a/b
print "a**b = ", a**b
print "c//d = ", c//d

print ""
print "Example for Comparision Operators"
print "##################################"
print "a is greater than b              : ", (a > b)
print "a is less than b                 : ", (a < b)
print "a is equal to b                  : ", (a == b)
print "a is greater than equal to b     : ", (a >= b)
print "a is less than equal to b        : ", (a <= b)
print "a is not equal to b              : ", (a <> b)

print ""
print "Example for Logical Operators"
print "##############################"
print "x and y = ", (x and y)
print "x or y  = ", (x or y)
print "x not y = ", not(x and y)
print "x not y = ", not(x or y)

print ""
print "Example for Assignment Operators"
print "################################"
c += a
print "c += a =  : ", c
c -= a
print "c -= a =  : ", c
c *= a
print "c *= a =  : ", c
c /= a
print "c /= a =  : ", c
c %= a
print "c %= a =  : ", c
c **= a
print "c **= a = : ", c
c //= a
print "c //= a = : ", c

print ""
print "Example for Membership Operators"
print "################################"
a=11
b=22
list=[1,2,3,4,5]
if (a in list):
    print "line1 - a is available in list"
else:
    print "line1 - a is not available in the list"

if (b not in list ):
    print "line2 - b is not available in the list"
else:
    print "line2 - b is available in the list"
a=1
if (a in list):
    print "line3 - a is available in the list"
else:
    print "line3 - a is not available in the list"

print ""
print "Example for Identity Operators"
print "################################"
a=20
b=20
if (a is b):
    print "line1 - a and b have same identity"
else:
    print "line1 - a and b have different identity"

if (id(a) == id(b)):
    print "line2 - a and b have same identity"
else:
    print "line2 - a and b have different identity"

if ( a is not b):
    print "line3 - a and b have different identity"
else:
    print "line3 - a and b have same identity"

b = 30
print "b = : ", b
print "a = : ", a
if (a is b):
    print "line1 - a and b have same identity"
else:
    print "line1 - a and b have different identity"

if (id(a) == id(b)):
    print "line2 - a and b have same identity"
else:
    print "line2 - a and b have different identity"

if ( a is not b):
    print "line3 - a and b have different identity"
else:
    print "line3 - a and b have same identity"