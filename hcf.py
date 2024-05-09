def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

num1 = 60
num2 = 40

print("The HCF of", num1, "and", num2, "is", hcf(num1, num2))