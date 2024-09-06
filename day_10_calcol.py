def add(n1,n2):
    return (n1+n2)

def sub(n1,n2):
    return (n1-n2)

def div(n1,n2):
    return (n1/n2)

def mult(n1,n2):
    return (n1*n2)

dude={
    "+":add,
    "-":sub,
    "/":div,
    "*":mult,

    }

def cal():
    num1=float(input("Enter 1st number: "))
    con="y"
    for key in dude:
        print(key)
    
    while(con=="y"):
        duder=input("Pick operations symbol: ")
        num2=float(input("Enter another number: "))
        man =dude[duder]
        ans=man(num1,num2)
        print(f"{num1} {duder} {num2} = {ans}")
        con=input(f"Type y to continue calculating with {ans}, or type anyting else to exit: ")
        if(con=="y"):
            num1=ans
        else:
            cal()
        
cal()

    
