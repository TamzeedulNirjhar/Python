amount = int(input("Enter the amount: "))
note_100 = amount//100
note_50 = (amount%100)//50
note_10 = ((amount%100)%50)//10
print("Notes of 100 taka: ",note_100)
print("Notes of 50 taka: ",note_50)
print("Notes of 10 taka: ",note_10)