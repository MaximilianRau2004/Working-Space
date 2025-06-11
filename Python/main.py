username = input("Enter your name: ")

if len(username) > 12:
    print("invalid username")
elif username.find(" ") != -1:
    print("invalid username")
elif not username.isalpha():
    print("invalid username")
else:
    print("Valid username")
