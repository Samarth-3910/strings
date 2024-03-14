num_string = int(input("Enter the no of string : "))

for i in range(num_string):
    string = input(f"Enter the string {i+1} : ")
    vowels = 0
    consonants = 0
    for char in string:
        if char in 'aeiouAEIOU':
            vowels = vowels + 1
        elif char.isalpha():
            consonants = consonants + 1
    print("No of Vowels :", vowels, "No of consonants :", consonants)