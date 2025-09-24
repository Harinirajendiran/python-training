def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("===simple calculator===")
print("press 'q' to quit.\n")

op=''#initialise so loop runs at least once

while op !='q':
    op=input("enter operation(+,-,*,/or q to quit):")

    if op=='q':
        print("quit")
        break
    
    if op not in ('+','-','*','/'):
        print("invalid operator")
        
    if(op=='+'):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(add(a,b))
    
    if(op=='-'):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(sub(a,b))
        
    if(op=='*'):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(mul(a,b))
        
    if(op=='/'):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(div(a,b))
              
