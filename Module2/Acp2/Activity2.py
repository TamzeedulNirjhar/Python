num = int(input("Enter a number: "))

if num < 0:
    num = -num

count = 0

while num != 0:
    num = num // 10
    count += 1

print("Total digits:", count)
