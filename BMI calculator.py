
print("Welcome to BMI calculator!")
      
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

a = float(height)
b = float(weight)


bmi = int(b/(a**2))

bmi1 = round(bmi, 1)

if bmi1 < 18.5:
    print("Your bmi is " + f"{bmi1}" + ", you are underweight.")

elif bmi1 < 18.5:
    print("Your bmi is " + f"{bmi1}" + ", you have a normal weight.")
elif bmi1 < 25:
    print("Your bmi is " + f"{bmi1}" + ", you have a normal weight.")
elif bmi1 < 25:
    print("Your bmi is " + f"{bmi1}" + ", you are slightly overweight.")
elif bmi1 < 30:
    print("Your bmi is " + f"{bmi1}" + ", you are slightly overweight.")
elif bmi1 < 30:
    print("Your bmi is " + f"{bmi1}" + ", you are obese.")
elif bmi1 < 35:
    print("Your bmi is " + f"{bmi1}" + ", you are obese.")


else:
    print("Your bmi is " + f"{bmi1}" + ", you are clinically obese.")