# simple calculator using python 

print("This is a calculator,for any operation choose your option")
print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")
print("5.Square of a number")

def Add(a,b):
    return a+b

def Sub(c,d):
    return c-d

def Mul(e,f):
    return e*f

def div(g,h):
    return g/h

def Square(i):
    return i*i

j = int(input("Please choose your option: "" "))

if j == 1:
  print("so you want to perform addition")
  k =  int(input("please enter first number:"))
  l =  int(input("Enter second number:"))
  result = Add(k,l)
  print("The result is: """,result)

elif j==2:
    print("so you want to perform Subtraction")
    m = int(input("Enter first number:" ""))  
    n = int(input("Enter second number:"""))
    aayo = Sub(m,n)
    print("The result is: """,aayo)


elif j==3:
    print("so you want to perform Multiplication")
    o = int(input("Enter first Number"))
    p = int(input("Enter second number"))
    gayo = Mul(o,p)
    print("The result is: """,gayo)

elif j==4:
    print("so you want to perform Division")
    q = int(input("Enter first number:"))
    r = int(input("enter second number:"))
    apple = div(q,r)
    print("The result is: """,apple)

elif j==5:
    print("so you want a Square of a number")
    s = int(input("Enter a number:" ""))
    Fox = Square(s)
    print(Fox)

else:
    print("Please choose the valid option ")
   










    






    


        
















         


