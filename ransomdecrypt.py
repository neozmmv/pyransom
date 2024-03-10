import os
import pyaes

file_name = "(encryptedFileName.extension)"
file = open(file_name, "rb")
file_data = file.read()
file.close()

key = "1234567812345678" #16 digit key (same as encryption)
aes = pyaes.AESModeOfOperationCTR(key.encode())
decrypt_data = aes.decrypt(file_data)

os.remove(file_name)

new_file_name = "(newDecryptedFileName.extension)"
new_file = open(new_file_name, "wb")
new_file.write(decrypt_data)
new_file.close()
