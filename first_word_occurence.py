a = input()
b = input()

index = -1
for i in range(len(a) - len(b) + 1):
    if a[i:i+len(b)] == b:
        index = i
        break

print(index)