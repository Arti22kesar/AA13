#Ques1.

#Exception occured is ZeroDivisionError

try:
    a=3
    a=a/(a-3)
except ZeroDivisionError:
    print("error")
else:
    print(a)
finally:
    print("handeled")

#Ques2.

#IndexError

try:
    l=[1,2,3]
    a=l[3]
except IndexError:
    print("list index is out boundes")
else:
    print(l)
finally:
    print("handeled")

#Ques3.

print("output is : an exception")

#Ques4.

print(" AbyB(2.0,3.0), output is : -5")
print(" AbyB (3.0,3.0) , output is a/bresult in 0")

#Ques5.

#import error
try:
    import Arti
except ImportError:
    print("error")

#value error
try:
    n=int(input("enter"))
except ValueError:
    print("please enter the value")

#index error

try:
    l=[1,2]
    n=l[3]
except IndexError:
    print("Index out of bounds")

#Ques6.

i=0
class Agetosma11(Exception):
    pass
while(i<18):
    try:
        i=int(input("E:"))
        if (i<18):
            raise Agetosma11

    except Agetosma11:
        print("age is less than 18")
else:
    while(False):
        pass