input_string = input("Enter the String :")
input_string += input_string

output_string = ''
for char in input_string:
    if not char.isupper():
        if char in 'aeiouAEIOU':
            output_string += '#'
        else:
            output_string += char

print(output_string)
