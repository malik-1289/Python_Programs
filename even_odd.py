def even():
    a= int(input("\nEnter the nth term:"))
    for i in range(1,a+1):
        if i%2==0 :
            print(i,end=" ")
    if a%2!=0:
        print("\n",a," is not an Even Number.")

def odd():
    a= int(input("\nEnter the nth term:"))
    for i in range(1,a+1):
        if i%2!=0:
            print(i, end=" ")
    if a%2==0:
        print("\n",a," is not an Odd Number.")

def choice():
    print("\n\n[Press 1] For finding Even Numbers. ")
    print("[Press 2] For finding Odd Numbers. ")
    print("[Press 3] To Exit. ")

    a=int(input("\nEnter your Choice: "))
    if (a== 1):
        even()
        choice()
    elif (a==2):
        odd()
        choice()
    elif(a==3):
        exit()
    else:
        print("\nInvalid Input")
        choice()

choice()
