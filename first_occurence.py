A = input("Enter the String:")
B = int(input("Enter the Integer: "))

found = False

for i in range(len(A)):
    char = A[i]
    if char == chr(B):
        print(f"{i}")
        found = True
        break

if not found:
    print("It does not exist")
