def even_number():
    
    while True:
        print("WELCOME TO EVEN NUMBER DETECTOR\n")
        print("[1] DETECT A EVEN NUMBER\n[2] TEST MULTIPLE NUMBERS\n[3] EXIT\n")
        choice = (input("Enter your choice: "))
        
        if(choice == "1"):
            test_number = int(input("\nEnter a number: "))
            
            if ((test_number) % 2 == 0):
                print(f"\n{test_number} is an even number\n\n")
            
            else:
                print(f"\n{test_number} is an odd number\n\n")
            
        elif( choice == "2"):
            num = int(input("How many numbers you want to check: "))
            for i in range(num):
                test_number_series = int(input("\nEnter the number: "))
                if((test_number_series) % 2 == 0):
                    print(f"{test_number_series} is an even number\n")
                else:
                    print(f"{test_number_series} is an odd number\n")
                    
        elif(choice == "3"):
            break
        
        else:
            print("Invalid choice....\n")
        
            
even_number()