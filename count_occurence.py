A = input()
B = input()
count = 0

first_occurrence = A.find(B)

while first_occurrence != -1:
    count += 1
    first_occurrence = A.find(B, first_occurrence + 1)

if count > 0:
    print(f"Time of occurrence of '{B}' in '{A}': {count}")
else:
    print(f"The substring '{B}' does not exist in the string '{A}'.")
