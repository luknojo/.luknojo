import random
import string

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho_senha = int(input("Digite o tamanho da senha: "))
    senha_segura = gerar_senha(tamanho_senha)
    print(f"A senha gerada é: {senha_segura}")
