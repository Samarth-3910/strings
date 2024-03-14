num_string = int(input("Enter the number of string : "))

for i in range(num_string):
    string = input(f"Enter the string {i+1} :")
    revstr = string[::-1]

    if string == revstr:
        print("Palindrome")
    else:
        print("Not A Palindrome")