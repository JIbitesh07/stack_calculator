stack=[]
top=-1
val=""

def push():
    global top
    value=str(input("which value to add? "))
    stack.append(value)
    top+=1
    print(stack)
def pop():

    global val
    for i in range(len(stack)):
        val=val+stack.pop()
    print(val)
    print()
    
ch='y'
while(ch=='y'):
    choice=int(input("choose 1 for push choose 2 for pull: "))
    if choice==1:
        push()
    elif choice==2:
        pop()
    ch=input("do you want to continue: y or n ")
    if ch=="n":
        print("The final  answer: ",eval(str(val)))
