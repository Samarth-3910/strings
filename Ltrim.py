string = input("Enter the string :")

while string and string[0] == '*':
    string = string[1:]

print(string)
