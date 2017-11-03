w = float(input("nhap can nang cua ban :"))
h1 = int(input(" nhap chieu cao cua ban:"))
h2 = h1 / 100
BMI = w / (h2 ** 2)
if BMI < 16:
    print ("severly underweight")
elif BMI < 18.5 :
    print ("underweight")
elif BMI < 25 :
    print ("normal")
elif BMI < 30:
    print ("overweight")
else :
    print ("obese")
