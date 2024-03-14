string = input("Enter the string :")

while string and string[-1] == '*':
    string = string[:-1]

print(string)
