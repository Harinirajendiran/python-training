#write the calculator using def function,condition statement,user defined input
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def floordiv(a,b):
    return a//b
def mod(a,b):
    return a%b
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=input(" enter c symbol(+,-,*,/,%,//):")#get an input from the user
if(c=='+'):
    print(add(a,b))
elif(c=='-'):
    print(sub(a,b))
elif(c=='*'):
    print(mul(a,b))
elif(c=='/'):
    print(div(a,b))
elif(c=='//'):
    print(floordiv(a,b))
elif(c=='%'):
    print(mod(a,b))
else:
    print("invalid operators")#condition statement

    
    
