user_msg1 = input(">>>")
if ((user_msg1) == "hello"):
        print("Hello Anup")

user_msg2 = int(input(">>>"))

try:
    num = user_msg2 % 2
    if (num == 0):
        print(f"{user_msg2} is even.")
            
    else:
        print(f"{user_msg2} is odd")
except ValueError:
    print("This is not a number")
        
        
user_msg3 = int(input(">>>"))
for i in range(user_msg3):
    print(i)