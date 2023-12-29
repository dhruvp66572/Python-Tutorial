while True:
    print("\n Calculator")
    print("Select Opration:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulo Division")
    print("6. Terminate")

    a  = input('Enter A : \n')
    b  = input('Enter B : \n')
    
    choice = int(input("\nEnter your choice To Opration(1/2/3/4/5/6/7): "))
    ans = 0

    if 1 <= choice <= 7:
        if choice == 1:
            print("Addition (A+B )is ",a+b)
        elif choice == 2:
            print("Subttraction (A-B )is ",a-b)
        elif choice == 3:
            print("Multiplication (A*B )is ",a*b)
        elif choice == 4:
            print("Division (A/B )is ",a/b)
        elif choice == 5:
            print("Modulo Division (A%B )is ",a%b)
        elif choice == 6:
            break
    else:
        print("\nInvalid choice. Please select a valid option (1/2/3/4/5/6/7).")