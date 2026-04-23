def sum_of_two_numbers():
    while True:
        print("\nWELCOME TO ADDITION SUBTRACTION MACHINE")
        
        print("\n[1] Add\n[2] Sub\n[3] Exit\n")
        choice = input("\nEnter your choice: ")
        
        if(choice == "1"):
            try:
                a = int(input("\nEnter 1st number: "))
                b = int(input("\nEnter 2nd number: "))
                print(f"\nThe sum of {a} and {b} is: ", a+b)
                
            except ValueError:
                print("\nPlease numbers only")
                
        elif(choice == "2"):
            try:
                a = int(input("\nEnter 1st number: "))
                b = int(input("\nEnter 2nd number: "))
                print(f"\nThe subtraction of {a} and {b} is: ", a-b)
                
            except ValueError:
                print("\nPlease numbers only")
            
        elif (choice == "3"):
            print("\nExiting....")
            break
          
        else:
            print("\nInvalid choice!! Try again")
        
sum_of_two_numbers()