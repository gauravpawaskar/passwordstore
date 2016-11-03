from Crypto.Cipher import AES
import base64

key = raw_input("Enter Key (16 char MUST*): ")
menu = raw_input("1. Enter to DB\n2. Read from DB\nPress your selection: ")

def encrypt(key, message):
  target = open('data.pass','r')
  file_data = target.read()
  #print file_data
  # Encryption
  encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
  cipher_text = encryption_suite.encrypt(message)
  encoded = base64.b64encode(cipher_text)
  target = open('data.pass','a')
  target.write(encoded + '\n')
  print encoded

def decrypt(key):
  target = open('data.pass','r')
  #file_data = target.read()
  for encoded in target:
    # Decryption
    print(encoded)
    cipher_text = base64.b64decode(encoded)
    decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher_text)
    print plain_text

if menu == '1':
  message = raw_input("Enter data to encrypt: \n")
  pad = 16 - len(message)%16
  encrypt(key, message + (" " * pad))
elif menu == '2':
  decrypt(key)
