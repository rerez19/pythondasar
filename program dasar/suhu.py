import numpy as np

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius_temperatures = np.array([0, 10, 20, 30, 40])

fahrenheit_temperatures = celsius_to_fahrenheit(celsius_temperatures)
print("Celsius:", celsius_temperatures)
print("Fahrenheit:", fahrenheit_temperatures)

celsius_temperatures_back = fahrenheit_to_celsius(fahrenheit_temperatures)
print("Fahrenheit:", fahrenheit_temperatures)
print("Celsius:", celsius_temperatures_back)
