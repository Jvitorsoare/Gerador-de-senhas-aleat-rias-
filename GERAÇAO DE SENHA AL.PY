import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

tamanho_da_senha = int(input("Digite o tamanho da senha desejada: "))
senha_gerada = gerar_senha(tamanho_da_senha)
print("Sua nova senha é:", senha_gerada)