input_str = input("Enter the string: ")

reversed_str =''
words = input_str.split()
for i in range(len(words)-1,-1,-1):
    reversed_str = reversed_str + words[i][::-1]
    if i > 0:
        reversed_str = reversed_str + ' '
print(reversed_str)