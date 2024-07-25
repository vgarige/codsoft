print("Enter numbers calculate:")
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
choice=0
while choice<5:
    print("====Calculator====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit..")
    choice=int(input("Enter your choice: "))

    if choice==1:
        c=a+b
        print('Sum of the given number is: ',c)
    elif choice==2:
        c=a-b
        print('Difference between the given numbers is: ',c)
    elif choice==3:
        c=a*b
        print('Product:', c)
    elif choice==4:
        c=a/b
        print('Quotient: ',c)
    elif choice==5:
        break
    else:
        print('Invalid Choice. Please enter valid choice')
