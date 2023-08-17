fib=[0,1]
n=int(input("Enter the value: "))

for i in range(n-2):
   t3=fib[i]+fib[i+1]
   fib.append(t3)
   
print(fib)
