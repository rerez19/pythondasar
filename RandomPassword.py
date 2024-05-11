import numpy as np

def decrypt_password(encrypted_password, shift):
    decrypted_password = ""
    for char in encrypted_password:
        decrypted_password += chr(ord(char) - shift)
    return decrypted_password


encrypted_password = "ABCDF"
 
shift = 1

decrypted_password = decrypt_password(encrypted_password, shift)
print("Password descrypted:", decrypted_password)
