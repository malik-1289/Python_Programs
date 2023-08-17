while True:

    n=int(input("\nFind factorial for the number: "))
    fact=1
    
    for i in range(1,n):
        fact =fact*(1+i)

    print(f'{fact:,}')

