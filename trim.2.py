input_str = input("Enter the String : ")

while input_str.startswith("*"):
    input_str = input_str[1:]

while input_str.endswith("*"):
    input_str = input_str[:-1]

print("Trimmed string:", input_str)
