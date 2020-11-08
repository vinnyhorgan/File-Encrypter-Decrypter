from cryptography.fernet import Fernet

def encrypt(filename, key):
  f = Fernet(key)

  with open(filename, "rb") as file:
    file_data = file.read()

  encrypted_data = f.encrypt(file_data)

  with open(filename, "wb") as file:
    file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)

    with open(filename, "rb") as file:
      encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
      file.write(decrypted_data)

def main():
  print("FILE ENCRYPTER/DECRYPTER\n- ENCRYPT (E)\n- DECRYPT (D)\n- GENERATE KEY (G)\n")
  mode = input("> ")

  if mode == "E":
    file = input("Enter the name of the file you want to encrypt in the same directory of this program\n> ")
    key = input("Enter encryption key\n> ")

    encrypt(file, key)
    print("The file was encrypted successfully")

  elif mode == "D":
    file = input("Enter the name of the file you want to decrypt in the same directory of this program\n> ")
    key = input("Enter decryption key\n> ")

    decrypt(file, key)
    print("The file was decrypted successfully")

  elif mode == "G":
    new_key = Fernet.generate_key()
    print("This is your key " + str(new_key.decode()) + "\n")
    main()

  else:
    print("Please insert a valid answer\n")
    main()

main()
