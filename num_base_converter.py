def binary():
    print(format(n,'b'))

def hex():
    print(format(n,'x'))

def octal():
    print(format(n,'o'))

while True:
    print("\nX-X-X-X-X-X-X-X-NUMBER BASE CONVERTER-X-X-X-X-X-X-X-X")
    print("\nConvert into: ")
    print("[Press 1]: Binary format \n[Press 2]: Hexadecimal \n[Press 3]: Octal Format \n[Press 4]: Exit ")
    choice=(int(input("\nEnter choice: ")))
    
    if choice==4:
        break

    n=int(input("\nEnter number: "))
    
    if choice== 1:
        binary()
    elif choice ==  2 :
        hex()
    elif choice==3:
        octal()
    else:
        print("Invalid choice")

    