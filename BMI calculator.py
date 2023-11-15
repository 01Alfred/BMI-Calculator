height = float(input("What is your height in m: "))
weight = int(input("What is your weight in kg: "))

bmi = weight / height ** 2
round_bmi = round(bmi)

if round_bmi < 18.5:
    print(f"You BMI is {round_bmi}, you're underweight")
elif round_bmi < 25:
    print(f"You BMI is {round_bmi}, you have a normal weight")
elif round_bmi < 30:
    print(f"You BMI is {round_bmi}, you're overweight")
elif round_bmi < 35:
    print(f"You BMI is {round_bmi}, you are obese")
else:
    print(f"You BMI is {round_bmi}, you are clinically obese")
