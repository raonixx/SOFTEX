#
#
#


print('calculadora')

op = int(input('Escolha uma opcao:[1] SOMA [2] SUBTRACAO [3] MULTIPLICACAO [4] DIVISAO [5] SAIR \n'))

while (op != 5):
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))

    if (op == 1):
        res = n1 + n2
        print('O resultado é ',res)
    elif (op == 2):
        res = n1 - n2
        print('O resultado é ',res)
    elif (op == 3):
        res = n1 * n2
        print('O resultado é ',res)
    elif (op == 4) and (n2 != 0):
        res == n1/n2z
        print('O resultado é ',res)
    else:    
        print("ERRO - O segundo número deve ser diferente de zero!")
        
    
else :
    print('voce encerrou o programa')
