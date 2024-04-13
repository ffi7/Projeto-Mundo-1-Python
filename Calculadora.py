from os import _exit
from time import sleep
from numexpr import evaluate

nome = str(input('Seja bem vindo(a), qual seu nome? ')).strip()

while nome == '':
   nome = input('\033[31mVOCÊ NÃO DIGITOU SEU NOME!\033[m\nPor favor digite o seu nome ').strip()

Sim = str(input(f'Olá \033[4m{nome}\033[m, e um imenso prazer ter sua presença aqui. Bom então vamos começar? ')).strip().lower()

while Sim == '':
   Sim = input('\033[34mPor favor coloque a sua resposta\033[m ').strip().lower()

if Sim == 'sim':
    print('\033[1;30mLENDO A RESPOSTA...\033[m')
    sleep(1)

else:
    print('Que pena seria tão legal \033[33m:(\033[m')
    sleep(1)
    _exit(0)

explicação = print('Certo, porém antes do inicio gostaria que você usasse os seguintes simbolos na calculadora: \n\033[30m+\033[m \033[33mpara adição \n\033[30m- \033[33mpara subtração \n\033[30mx \033[33mpara vezes \n\033[30m^ \033[33mpara expoenciação \n\033[30m() \033[33mpara () \n\033[30mr \033[33mpara raiz quadrada\033[m (exemplo: 4r)')

while True:
   operação_1 = input('Com isto em mente por favor digite a primeira operação \033[0;32mVALIDA! \033[m')
   if operação_1.find('x') >= 0 or operação_1.find('r') >= 0 or operação_1.find('^') >= 0 or operação_1.find('+') >= 0 or operação_1.find('-') >= 0:
    operação_corrigida_1 = operação_1.replace('x', '*').replace('^', '**').replace('r', '**1/2')

    resultado_1 = evaluate(operação_corrigida_1)
    resultado_Final_1 = float(resultado_1)

    if isinstance(resultado_Final_1, float):
        break
print('\033[1;30mREALIZANDO OS CALCULOS...\033[m')
if len(operação_1) >= 7:
   sleep(3)
else:
   sleep(1)

print(f'O resultado da sua operação será \033[35m{resultado_Final_1:.2f}\033[m.')
print('Então, vamos para a proxima operação!')
while True:
   operação_2 = input('Digite a segunda operação \033[32mVALIDA!\033[m ')
   if operação_2.find('x') >= 0 or operação_2.find('r') >= 0 or operação_2.find('^') >= 0 or operação_2.find('+') >= 0 or operação_2.find('-') >= 0 :
      operação_corrigida_2 = operação_2.replace('x', '*').replace('^', '**').replace('r', '**1/2')

      resultado_2 = evaluate(operação_corrigida_2)
      resultado_Final_2 = float(resultado_2)
      if isinstance(resultado_Final_2, float):
         break

print('\033[1;30mEFETUANDO OS CALCULOS...\033[m')
if len(operação_2) >= 7:
   sleep(3)
else:
   sleep(1)
print(f'O resultado da sua segunda operação será \033[35m{resultado_Final_2:.2f}\033[m')
print('Vamos para a ultima operação!')

while True:
   operação_3 = input('Digite a ultima operação \033[32mVALIDA!\033[m ')
   if operação_3.find('x') >= 0 or operação_3.find('r') >= 0 or operação_3.find('^') >= 0 or operação_3.find('+') >=0 or operação_3('-') >= 0:
      operação_corrigida_3 = operação_3.replace('x', '*').replace('^', '**').replace('r', '**1/2')

      resultado_3 = evaluate(operação_corrigida_3)
      resultado_final_3 = float(resultado_3)
      if isinstance(resultado_final_3, float):
         break
print('\033[30mEXECULTANDO OS CALCULOS...\033[m')
if len(operação_3) >= 7:
   sleep(3)
else:
   sleep(1)
print(f'O resultado da operação é \033[35m{resultado_final_3}!\033[m')
continuação = input('Otimo, gostaria de continuar e fazer uma relação desses resultados com o seu nome? ').strip().lower()
while continuação == '':
   continuação = input('\033[34mPor favor, coloque uma resposta\033[m ')
if continuação == 'sim':
   print('\033[30mPROCESSANDO...\033[m')
   sleep(5)
else:
   print('Então, eu so posso te ajudar ate aqui, tenha uma otima semana. \033[34mTchau\033[m')
   _exit(0)
print(f'Já que esta foi sua escolha, vamos começar do simples. Seu nome tem \033[35m{len(nome)}\033[m letras')
resultado_Final_inteiro_1 = int(resultado_Final_1)
if len(nome) >= resultado_Final_inteiro_1:
   print(f'O resultado da primeira operação é \033[35m{resultado_Final_inteiro_1}\033[m então ele equivale a letra \033[32m{nome[resultado_Final_inteiro_1 - 1]}\033[m do seu nome')
   print(f'Do inicio do seu nome ate o resultado da primeira operação fica \033[32m{nome[0: resultado_Final_inteiro_1]}\033[m')
   print(f'Seguindo essa logica, do resultado da primeira operação ate o fim do seu nome fica \033[32m{nome[-1 + resultado_Final_inteiro_1:]}\033[m')
else:
   print('\033[33mInfelizmente a primeira operação não possui nenhuma relação com seu nome\033[m')
resulrado_Final_str1 = str(resultado_Final_inteiro_1)
if resulrado_Final_str1 in nome:
   print(f'\033[36mQue estranho!\ntem\033[m \033[1;30mnúmeros\033[m \033[36mno seu nome!\033[m\nbom o resultado da primeira operação(\033[35m{resultado_Final_inteiro_1}\033[m) faz parte do seu nome')
resultado_Final_inteiro_2 = int(resultado_Final_2)
if len(nome) >= resultado_Final_inteiro_2:
   print(f'O resultado da segunda operação é \033[35m{resultado_Final_inteiro_2}\033[m então ele equivale a letra \033[32m{nome[resultado_Final_inteiro_2 - 1]}\033[m do seu nome')
   print(f'Do inicio do seu nome ate o resultado da segunda operação fica \033[32m{nome[0: resultado_Final_inteiro_2]}\033[m')
   print(f'Seguindo essa logica, do resultado da segunda operação ate o fim do seu nome fica \033[32m{nome[-1 + resultado_Final_inteiro_2:]}\033[m')
else:
   print('Infelizmente a segunda operação não possui nenhuma relação com seu nome')
resulrado_Final_str2 = str(resultado_Final_inteiro_2)
if resulrado_Final_str2 in nome:
   print(f'\033[36mQue estranho!\ntem\033[m \033[1;30mnúmeros\033[m \033[36mno seu nome!\033[m\nbom o resultado da primeira operação(\033[35m{resultado_Final_inteiro_2}\033[m) faz parte do seu nomee')
resultado_Final_inteiro_3 = int(resultado_final_3)
if len(nome) >= resultado_Final_inteiro_3:
   print(f'O resultado da terceira operação é \033[35m{resultado_Final_inteiro_3}\033[m então ele equivale a letra \033[32m{nome[resultado_Final_inteiro_3 - 1]}\033[m do seu nome')
   print(f'Do inicio do seu nome ate o resultado da terceira operação fica \033[32m{nome[0: resultado_Final_inteiro_3]}\033[m')
   print(f'Seguindo essa logica, do resultado da terceira operação ate o fim do seu nome fica \033[32m{nome[-1 + resultado_Final_inteiro_3:]}\033[m')
else:
   print('Infelizmente a terceira operação não possui nenhuma relação com seu nome')
resulrado_Final_str3 = str(resultado_Final_inteiro_3)
if resulrado_Final_str3 in nome:
   print(f'\033[36mQue estranho!\ntem\033[m \033[1;30mnúmeros\033[m \033[36mno seu nome!\033[m\nbom o resultado da primeira operação(\033[35m{resultado_Final_inteiro_3}\033[m) faz parte do seu nome')
print('Obrigado por ter participado desse projeto, \033[33mtchau\033[m.')
