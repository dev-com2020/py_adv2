from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()

descrypted = fernet.decrypt(encrypted)

with open('nba2.csv', 'wb') as dec_file:
    dec_file.write(descrypted)