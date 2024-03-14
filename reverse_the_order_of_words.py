input_str = input("Enter the string: ")

words = input_str.split()
reversed_words = words[::-1]
reversed_str = ' '.join(reversed_words)
print(reversed_str)