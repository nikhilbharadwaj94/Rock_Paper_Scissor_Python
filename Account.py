print("###########################################################")
print("Rock Paper Scissors account setup")
print("Version 2.0")
print("###########################################################")
while True:
    username = input("Input your username   ")
    password = input("Input your password   ")
    confirm_password = input("re-enter your password   ")
    if password != confirm_password:
        print("Your passwords dont match. Please try again!!!")
    if password == confirm_password:
        print("Your account has been set up")
        text_file = open("acounts.txt", "a")
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
