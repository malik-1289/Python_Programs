
def checkpal():
    print("\n\t-----------CHECK PALINDROME PROGRAM-----------")
    a=input("\nEnter text : ")
    
    print("reversed text: ",a[-1::-1])

    if a== a[-1::-1]:
        print("It is PALINDROME\n")

    else:
        print("Not a PALINDROME\n")

checkpal()