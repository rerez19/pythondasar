try:
    # Blok kode yang mungkin menghasilkan kesalahan
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    # Blok except untuk menangani kesalahan ZeroDivisionError
    print("Error: Cannot divide by zero!")

except ValueError:
    # Blok except untuk menangani kesalahan ValueError (mis. input yang bukan angka)
    print("Error: Please enter valid numbers!")

finally:
    # Blok finally akan selalu dieksekusi, baik ada kesalahan maupun tidak
    print("End of program.")
