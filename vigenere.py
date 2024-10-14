import random

class VigenereCipher:
    def __init__(self, key):
        self.key = key

    def generate_key(self, text):
        key = self.key
        while len(key) < len(text):
            key += self.key
        return key[:len(text)]

    def encrypt(self, plaintext):
        key = self.generate_key(plaintext)
        result = ''
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                shift = (ord(plaintext[i].lower()) + ord(key[i].lower()) - 2 * 97) % 26
                new_char = chr(shift + 97)
                result += new_char.upper() if plaintext[i].isupper() else new_char
            else:
                result += plaintext[i]
        return result

    def decrypt(self, ciphertext):
        key = self.generate_key(ciphertext)
        result = ''
        for i in range(len(ciphertext)):
            if ciphertext[i].isalpha():
                shift = (ord(ciphertext[i].lower()) - ord(key[i].lower()) + 26) % 26
                new_char = chr(shift + 97)
                result += new_char.upper() if ciphertext[i].isupper() else new_char
            else:
                result += ciphertext[i]
        return result

def generate_verification_code():
    """Genera un código de verificación aleatorio de 6 dígitos"""
    return str(random.randint(100000, 999999))

def login():
    # Primera fase de autenticación: Usuario y contraseña
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Puedes cambiar las credenciales por las que prefieras
    if username == "sofiaalu" and password == "galletas":
        print("Login successful!")

        # Segunda fase de autenticación: Código de verificación
        verification_code = generate_verification_code()
        print(f"A verification code has been sent: {verification_code}")
        user_code = input("Enter the verification code: ")

        if user_code == verification_code:
            print("Two-step verification successful!")
            return True
        else:
            print("Invalid verification code. Access denied.")
            return False
    else:
        print("Invalid username or password.")
        return False

def vigenere_menu():
    key = input("Enter the key for Vigenere Cipher: ")
    vigenere = VigenereCipher(key)

    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice == 'e':
        plaintext = input("Enter the text to encrypt: ")
        print(f"Encrypted Text: {vigenere.encrypt(plaintext)}")
    elif choice == 'd':
        ciphertext = input("Enter the text to decrypt: ")
        print(f"Decrypted Text: {vigenere.decrypt(ciphertext)}")
    else:
        print("Invalid option!")

if __name__ == "__main__":
    if login():  # Solo accede al menú si pasa las dos fases de autenticación
        vigenere_menu()
