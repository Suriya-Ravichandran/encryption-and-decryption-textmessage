#importing library cryptography
from base64 import decode
from cryptography.fernet import Fernet

key=Fernet.generate_key()
print("this key value:",key)
A=str(input("Enter your message")).encode()
a_obj= Fernet(key)
encrpted_msg= a_obj.encrypt(A)
print("this is encrpted message:",encrpted_msg) 
decrpted_msg=a_obj.decrypt(encrpted_msg)
print("this is decrypted message : ",decrpted_msg)

