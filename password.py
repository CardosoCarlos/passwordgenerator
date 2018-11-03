from random import choice
import hashlib 

def encrypt_password(password):
    sha_password = \
        hashlib.sha256(password.encode()).hexdigest()   
    return sha_password

print('Gerador de senha segura ...')

tam_senha = int(input('Qual tamanho de senha deseja?'))

if tam_senha > 10:
    print('Insira um valor menor ou igual a 10!')
    tam_senha = int(input('Qual tamanho de senha deseja?'))

caracteres = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")"]

password = ""
for i in range(0, tam_senha):
    password = password + choice(caracteres)
    i = i+1

sha_password = encrypt_password(password)

print('Senha gerada: ' +password )

print('Senha gerada hash: ' +sha_password )