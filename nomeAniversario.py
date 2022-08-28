#Nome completo e idade atual
#Atividade 12
nome = input('Digite seu nome completo: ')
dados = True
while dados:
    try:
        anoNascimento = int(input('Digite o ano que você nasceu: '))
        if (1922 <= anoNascimento < 2022):
            idadeAtual = 2022 - anoNascimento
            print(f'{nome} completou ou completará {idadeAtual} anos em 2022.')
        else:
            raise Exception ('Erro!')
    except:
        print('Voce digitou um valor invalido!')
else:
    dados = False
