import random
import string
try:
    def random_password_generator(length,complexity):
        if length>=8:
            if complexity=="1":
                for  _ in range(length):
                    password=random.randrange(0,10)
                    print(password,end="")
            elif complexity=="2":
                for _ in range(length):
                    elements= string.ascii_letters+ string.digits
                    password=random.choice(elements)
                    print(password,end="")
            elif complexity=="3":
                for _ in range(length):
                    characters=string.ascii_letters +string.digits+string.punctuation
                    password=random.choice(characters)
                    print(password,end="")
            else:
                print('select only 1,2 or 3 for complexity level')
        else:
            print("The minimum length should be 8!")
    length=int(input("Enter the required length of the password:"))
    print("Select complexity level of the password, password should contain")
    print("1:Only Numbers\n2:Both numbers and alphabets\n3:numbers, alphabets and symbols")
    complexity=input("Enter 1,2 or 3:")
    random_password_generator(length,complexity)
    while True:
        choice=input("\n1:Generate more password\n2Exit\nEnter 1 or 2:")
        if choice=="1":
            length=int(input("Enter the required length of the password:"))
            print("Select complexity level of the password, password should contain")
            print("1:Only Numbers\n2:Both numbers and alphabets\n3:numbers, alphabets and symbols")
            complexity=input("Enter 1,2 or 3:")
            random_password_generator(length,complexity)
        elif choice=="2":
            print("exiting......")
            print("exited")
            break
        else:
            print("INVALID CHOICE, TRY AGAIN")
except:
    print("Try again and Recheck your inputs")
