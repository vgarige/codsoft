import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*(){}[]<>")

def generate_password():
    password_length = int(input("Length of the password: "))

    random.shuffle(characters)
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a password? (Yes/No):")
if option =="yes":
    generate_password()

elif option =="no":
    print("Program ended")
                        
        


