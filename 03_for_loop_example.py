#!/usr/bin/python
for letter in "Python":
    print "letters in python", letter

print ""
list=["windows","mac","mobile","tab"]
for device in list:
    print "the device is : ", device

print ""
for device in range(len(list)):
    print "the device is : ", list[device]

print ""
for num in range(10,20):
    for i in range(2,num):
        #print "All available numbers are: ", i, num
        if (num%i == 0):
            j=num/i
            print "{} num is dividable by {} * {}".format(num,i,j)
            break;
    else:
        print "{} is prime number".format(num)

print ""
adj=["red","green","yellow"]
fruits=["apple","banana","watermelon"]
for i in adj:
    for j in fruits:
        print "{} {}".format(i,j)
    print ""

print ""
print "Using Break"
for i in fruits:
    print i
    if (i == 'banana'):
        break;

print ""
print "Using Continue"
for i in fruits:
    if (i == 'banana'):
        continue;
    print i


for x in range(2, 30, 3):
  print(x)
