def fib():
    n1=0
    n2=1
   
    n=int(input("\nEnter the n: "))
    if(n<=0):
        print("Enter the valid!!!")
    
    elif n == 1:
       print("Fibonacci sequence upto",n,":")
       print(n1)

    else:
        print("Fibonacci series :")
        count=0
        while count<n:
            print(n1,end="+")
            nth = n1+ n2

            n1= n2
            n2= nth
            count += 1
            

fib()


