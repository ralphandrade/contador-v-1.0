# importa as bibliotecas
import os
import time 

# usuario informa um numero
contador = int(input('informe um numero inteiro: '))
os.system('cls')
# conta a partir do numero informado até 0
while contador >= 0:
    print(f'contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('BOOM!!!!!')