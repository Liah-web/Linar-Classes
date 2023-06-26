#ADDITION
def addition(a,b):
    '''This function takes
    two parameters which are always
    in intergers
    '''


#SUBTRACTION
def subtraction(a,b):
    '''This function takes
    two parameters which are always
    in intergers
    '''

#DIVISION
def division(a,b):
    '''This function takes
    two parameters which are always
    in intergers
    '''

#MULTIPLICATION
def multiplication(a,b):
    '''This function takes
    two parameters which are always
    in intergers
    '''

    #MODULUS
def modulus(a,b):
    '''This function takes
    two parameters which are always
    in intergers
    '''
 
   #BINARY
def binary(a,b):
    '''This function takes two parameters in integers
    '''

    #TO CALCULATE POWER
def power(a,b):
    '''This function takes two parameters in integers 

    '''
    #TO SOLVE QUADRATIC EQUATION
def quadraticEquation(a,b,c):
 '''This function takes three parameters in integers.
 '''
 

#TO CALCULATE SIMPLE INTEREST
def simpleinterest(p,r,t):
 '''This function takes three parameter, where p and r are in floats and time(t) in integers.
 '''

 #TO CALCULATE THE AREA OF A TRIANGLE
def areaofaTriangle(b,h):
 '''This function takes two parameters as integers where b is the base and h is the height.

 '''
 #TO CALCULATE THE AREA OF A RECTANGLE
def areaofaRectangle(l,b):
 '''This function takes two parameters in intergers where l is the length and b is the breath
 '''

 #TO CALCULATE THE VOLUME OF A CUBOID
def volumeofaCuboid(l,b,h):
 '''This function takes three parameters in intergers where l is the length, b is the breath and h is the height

 '''
 #TO AREA OF A TRAPEZIUM
def volumeofaCuboid(a,b,h):
 '''This function takes three parameters in intergers where l is the length, b is the breath and h is the height
'''
 #TO ROUND OFF
def roundoff(a):
 '''This function takes one parameter in integer.
'''
 
 #TO CALCULATE THE AREA OF A CIRCLE
def Areaofacircle(r):
 '''This function takes one parameter in integer.
'''
 
    #The fifteen functions available
print("For addition, Enter 1")
print("For subtraction, Enter 2")
print("For division, Enter 3")
print("For multiplication, Enter 4")
print("For addition, Enter 5")
print("For calculate modulus, Enter 6")
print("To calculate power, Enter 7")
print("To solve a quadratic equation, Enter 8 ")
print("To calculate simple interest, Enter 9")
print("To calculate the area of a Triangle, Enter 10")
print("To calculate the area of a Rectangle, Enter 11")
print("To calculate the volume of a cuboid,  Enter 12")
print("To calculate the area of a Trapezium, Enter 13")
print("To round off a number, Enter 14")
print("To calculate area of a circle, Enter 15")



youroperation=int(input("Enter the number for the operation you want to perform:"))
#THE CONDITIONAL STATEMENTS
if youroperation==1:
    a=float(input("Enter value for a:"))
    b=float(input("Enter value for b:"))
    print(a+b)
elif youroperation==2:
    a=float(input("Enter value for a:"))
    b=float(input("Enter value for b:"))
    print(a-b)
elif youroperation==3:
    a=float(input("Enter value for a:"))
    b=float(input("Enter value for b:"))
    print(a/b)
elif youroperation==4:
    a=float(input("Enter value for a:"))
    b=float(input("Enter value for b:"))
    print(a*b)
elif youroperation==5:
    a=float(input("Enter value for a:"))
    b=float(input("Enter value for b:"))
    print(a%b)
elif youroperation==6:
    a=float(input("Enter value for a:"))
    print(bin((a)))
elif youroperation==7:
    a=float(input("Enter value for a:"))
    b=float(input("Enter the base, b:"))
    print(pow(a,b))
elif youroperation==8:
    a=float(input("enter value for a:"))
    b=float(input("enter value for b:"))
    c=float(input("enter value for c:"))
    d=((b*b)-(4*a*c))**0.5
    P1=(-b+d)/2*a
    P2=(-b-d)/2*a
    print("The answer is "+ str(P1)+ " or " + str(P2))
elif youroperation==9:
     p=float(input("Enter the amount for principal:\n"))
     r=float(input("Enter the rate given:\n"))
     t=int(input("Enter the value for time:\n"))
     SimpleInterest=((p*r)*float(t)/100.0)
     print(SimpleInterest)
elif youroperation==10:
     b=float(input("Enter value for base, b:"))
     h=float(input("Enter value for height, h:"))
     print((b*h)/2)
elif youroperation==11:
     l=float(input("Enter value for length, l:"))
     b=float(input("Enter value for breath, b:"))
     print(2*(l+b))
elif youroperation==12:
     l=float(input("Enter value for length, l:"))
     b=float(input("Enter value for breath, b:"))
     h=float(input("Enter value for height, h"))
     print(l*b*h)
elif youroperation==13:
     a=float(input("Enter value for  a:"))
     b=float(input("Enter value for  b:"))
     h=float(input("Enter value for height, h"))
     print((a+b)*h)/2
elif youroperation==14:
     a=float(input("Enter number to round off:"))  
     print(round(a))
elif youroperation==15:
     r=float(input("Enter the value for radius, r:"))  
     print((r**2)*3.142)

 

 
