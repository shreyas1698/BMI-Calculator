height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
weight = int(weight)
BMI = weight/(height**2)
BMI1 = round(weight//(height**2))
print(str(weight) + ' ÷ ' + '(' + str(height) + ' x ' +  str(height) + ')' + ' = ' + str(BMI))
if BMI < 18.5:
  print('Your BMI is ' + str(BMI1) + ', you are underweight.')
elif 18.5 < BMI < 25:
  print('Your BMI is ' + str(BMI1) + ', you have a normal weight.')
elif 25 < BMI < 30:
  print('Your BMI is ' + str(BMI1) + ', you are slightly overweight.')
elif 30 < BMI < 35:
  print('Your BMI is ' + str(BMI1) + ', you are obese.')
else:
  print('Your BMI is ' + str(BMI1) + ', you are clinically obese.')