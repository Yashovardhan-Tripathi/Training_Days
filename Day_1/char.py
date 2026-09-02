'''WAP to accept any one character and check the entered character is in UPPERCASE, LOWERCASE, DIGIT, any special character
and according to that display appropriate message.'''

Input=(input("Enteer a character "))

if Input.isupper():
    print("The Entered number is UPPERCASE ")
elif Input.islower():
    print("The Entered number is LOWERCASE ")
elif Input.isdigit():
    print("The Entered number is DIGIT ")
else:
    print("The Entered number is SPECIAL CHARACTER ")

Input=ord(Input)

if Input in range(65,91):
    print("The Entered number is UPPERCASE ")
elif Input in range (97,123):
    print("The Entered number is LOWERCASE ")
elif Input in range(48,59):
    print("The Entered number is DIGIT ")
else:
    print("The Entered number is SPECIAL CHARACTER ")
