def greet():
    user_name = input("Enter your name: ")

    for i in range(3):
        print("Hello", user_name)

# greet()

def greet_Tony():
    user_name_1 = input("Enter your name: ").lower().replace(" ", "").strip()    # .upper() will conver the input to upper case words, and .lower() will conver them into samller case letters
    
    if (user_name_1 == "tony"):
        for i in range(3):
            print("Welcome back, Boss")
    else:
        for i in range(3):
            print("Hello", user_name_1)
greet_Tony()