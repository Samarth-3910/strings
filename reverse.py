input_str = input("Enter the string: ")

reversed_str = ""

for i in range(len(input_str)-1, -1, -1):
    reversed_str =reversed_str + input_str[i]

print("Reversed Strings :", reversed_str)