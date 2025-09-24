def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.exit")
    c=int(input("enter the choice(1-5):"))
    
    if(c==1):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(add(a,b))
    elif(c==2):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(sub(a,b))
    elif(c==3):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(mul(a,b))
    elif(c==4):
        a=int(input("enter a value:"))
        b=int(input("enter b value:"))
        print(div(a,b))
    else:
        print("quit")

    
