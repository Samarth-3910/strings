string = input("Enter the String: ")

while string and string[0] == '*':
    string = string[1:]

while string and string[-1] == '*':
    string = string[:-1]

print(string)
