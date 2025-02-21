def Calculator():
    print("Welcome to the calculator")

    loop = True


    while loop:
        total = 0.0
        while loop:
            try:
                no_input = input("Please enter a number or 'q' to quit: ")
                if no_input == 'q':
                    print("Total: ", total)
                    cont = input("Do you want to calculate again? 'y' or 'n': ")
                    if cont == 'y':
                        print("Your last total: ", total)
                        break
                    elif cont == 'n':
                        print("Thank you for using this calculator!")
                        return 
                    else:
                        print("Invalid! Thank you for using this calculator!")
                else:
                    float_no =  float(no_input)
                    operations = ['+','-','*','/']
                    operation = input("What operation would you like to execute +,-,*,/  :  ")
                    if operation in operations:
                        if operation == '+':
                            total += float_no
                            print("Current result: ", total)
                        elif operation == '-':
                            total -= float_no
                            print("Current result: ", total)
                        elif operation == '*':
                            total *= float_no
                            print("Current result: ", total)
                        elif operation == '/':
                            if float_no == 0:
                                print("Error: Division by zero is not allowed.")
                            else:
                                total /= float_no
                                print("Current result: ", total)
                        else:
                            print("Use a valid operation")
                    else:
                        print("The only supported values by this calculator are: +,-,*,/ ")
            except ValueError as e:
                print(e, "Enter a valid number!")   
  
    
Calculator()