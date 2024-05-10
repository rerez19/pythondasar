import numpy as np

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weights = np.array([70, 80, 90]) 
heights = np.array([1.75, 1.8, 1.65]) 

bmis = calculate_bmi(weights, heights)

categories = np.array([bmi_category(bmi) for bmi in bmis])

for i in range(len(weights)):
    print("Person", i+1, "=", "BMI:", bmis[i], ",", "Category:", categories[i])
