import os
import pyaes

file_name = "JET.png.neozransom"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = "123456789peste12"
aes = pyaes.AESModeOfOperationCTR(key.encode())
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file_name = "JET.png"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()