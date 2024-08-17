from PIL import Image
from cryptography.fernet import Fernet
import io

# Função para gerar uma chave e salvá-la
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Função para carregar a chave
def load_key():
    return open("secret.key", "rb").read()

# Função para criptografar a imagem
def encrypt_image(image_path, output_path):
    key = load_key()
    cipher_suite = Fernet(key)

    with open(image_path, "rb") as image_file:
        image_data = image_file.read()

    encrypted_data = cipher_suite.encrypt(image_data)

    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print("Imagem criptografada e salva em", output_path)

# Função para descriptografar a imagem
def decrypt_image(encrypted_image_path, output_path):
    key = load_key()
    cipher_suite = Fernet(key)

    with open(encrypted_image_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print("Imagem descriptografada e salva em", output_path)

# Exemplo de uso
if __name__ == "__main__":
    # Gera e salva uma chave (faça isso uma vez e reutilize a chave gerada)
    # generate_key()

    # Criptografa a imagem
    encrypt_image("example_image.jpg", "encrypted_image.enc")

    # Descriptografa a imagem
    decrypt_image("encrypted_image.enc", "decrypted_image.jpg")
