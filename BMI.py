a=int(input("how old are you?:  "))
b=str(input("usa or uni: "))
w=float(input("Weight:  "))
m=float(input("height: "))
def bmi_can(m,w):
        if b=="uni":
            return w/(m**2)
        elif b=="usa":
            return (w/(m**2))*703
bmi=bmi_can(m,w)
if bmi < 18.5:
        print (bmi,"Underweight")
elif 18.5 <= bmi < 24.9:
       print (bmi, "Normal Weight")
elif 25 <= bmi < 29.9:
      print(bmi, "Overweight")
elif 30 <= bmi < 34.9:
      print(bmi, "Overweight")
elif 35 <= bmi < 39.9:
      print(bmi, "Overweight")
else:
        print (bmi, "Obese")

print (" Ответ:", bmi )
