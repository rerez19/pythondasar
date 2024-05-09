import numpy as np

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi


weights = np.array([70, 80, 90])  
heights = np.array([1.75, 1.8, 1.65])


bmis = calculate_bmi(weights, heights)

print("BMI for each person:", bmis)
