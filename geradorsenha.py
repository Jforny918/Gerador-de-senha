import random
import string

def gerar_senha(tamanho=12, usar_maiusculas=True, usar_minusculas=True, usar_numeros=True, usar_caracteres=True):
    # Cria uma lista de caracteres com base nas escolhas do usuário
    caracteres = ''
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres:
        caracteres += string.punctuation

    # Verifica se há caracteres disponíveis
    if not caracteres:
        raise ValueError("Pelo menos uma opção de caracteres deve ser selecionada.")

    # Gera uma senha aleatória
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    
    return senha

# Interação com o usuário
def interacao_usuario():
    print("Bem-vindo ao gerador de senhas!")

    # Solicita o tamanho da senha
    tamanho = int(input("Digite o tamanho da senha desejada (mínimo 8): "))
    if tamanho < 8:
        print("O tamanho mínimo da senha é 8. Usando 8 como padrão.")
        tamanho = 8

    # Solicita opções de caracteres
    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    usar_minusculas = input("Incluir letras minúsculas? (s/n): ").strip().lower() == 's'
    usar_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    usar_caracteres = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'

    # Gera a senha
    senha_gerada = gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_caracteres)
    print("Senha gerada:", senha_gerada)

# Chama a função de interação com o usuário
interacao_usuario()