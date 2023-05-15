import string
from unidecode import unidecode

# Produz a sequência de chaves necessária para criptografar ou descriptografar.
def generatingKey(mensagem, chave):
    indice = 0
    msgTamanho = len(mensagem)
    tam_chave = len(chave)
    keystream = ''
    for i in range(msgTamanho):
        if mensagem[i].isalpha():
            if indice >= tam_chave:
                indice = 0
            keystream += chave[indice].upper()
            indice += 1
        else:
            keystream += ' '
    return keystream

# Aceita uma chave e um texto cifrado (decifra usando a técnica de Vigenère).
def decoder(msgCifrada, chave):
    keystream = generatingKey(msgCifrada, chave)
    msgTamanho = len(msgCifrada)
    msgDecifrada = ''
    for i in range(msgTamanho):
        # Caso seja uma letra, realiza a codificação; caso contrário, mantém o original.
        if msgCifrada[i].isalpha():
            msgDecifrada += chr(((ord(msgCifrada[i].upper()) - ord(keystream[i].upper()) + 26) % 26) + ord('A'))
        else:
            msgDecifrada += msgCifrada[i]
    return msgDecifrada

# Aceita uma chave e uma mensagem (codifica usando a técnica de Vigenère).
def cipher(mensagem, chave):
    mensagem = unidecode(mensagem) 
    keystream = generatingKey(mensagem, chave)
    msgTamanho = len(mensagem)
    msgCifrada = ''
    for i in range(msgTamanho):
        # Caso seja uma letra, realiza a codificação; caso contrário, mantém o original.
        if mensagem[i].isalpha():
            msgCifrada += chr(((ord(mensagem[i].upper()) + ord(keystream[i])) % 26) + ord('A'))
        else:
            msgCifrada += mensagem[i]
    return msgCifrada

mensagem = input("\nDigite qualquer mensagem: ")
chave = input("Digite qualquer chave: ")

msgCifrada = cipher(mensagem, chave)
msgDecifrada = decoder(msgCifrada, chave)

print("Msg criptografada aqui: {}".format(msgCifrada))
print("Msg descriptografada aqui: {}\n".format(msgDecifrada))
