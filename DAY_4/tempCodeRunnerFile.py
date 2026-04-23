def code1():
    try:
        number = int(input("Enter a number: "))
        print(number , "\n")
    except:
        print("This was not a number\n")
        
# code1()
    
def code2():
    try:
        number = int(input("Enter a number: "))
        print(number)    
    except ValueError:
        print("This is not a number")

# code2()  

def age_check():
    while True:     
        try: 
            age = int(input("Enter your age: "))
            if(age > 18):
                print("You are eligible...")
                break
            else:
                print("You are not eligible")
                break
        except ValueError:
            print("Numbers only please")
        
age_check()

