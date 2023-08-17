n=int(input("Enter the number of integer to be multiplied: "))

list=[]

for i in range(n):
    a=int(input('Enter integer: '))
    list.append(a)

print(list)

product=1
for i in list:
    product= product*i
    
print(product)

