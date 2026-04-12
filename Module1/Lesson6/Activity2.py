weight = float(input("Enter your weight"))
height = float(input("Enter your height"))
bmi = weight / (height/100)**2
bmi = round(bmi,2)
if bmi<=18.4:
    print(f"Your bmi is {bmi}. You are under weight")
elif bmi<=24.4:
    print(f"Your bmi is {bmi}. You are healthy")
elif bmi<=29.4:
    print(f"Your bmi is {bmi}. You are overweight")
elif bmi<=34.4:
    print(f"Your bmi is {bmi}. You are obese")
else:
    Print(f"Your bmi is {bmi}. You are severly obese")

