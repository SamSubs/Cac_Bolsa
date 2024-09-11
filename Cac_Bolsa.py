try:
    class Menu:
        '''def __init__(self, user_valor, user_dividendo, user_cotas):
            self.user_valor = user_valor
            self.user_dividendo = user_dividendo
            self.user_cotas = user_cotas'''

        '''def Calc(self):
            user_valor = float(input('Valor do FII: '))
            user_dividendo = float(input('Valor do ultimo Dividendo/Media: '))
            user_cotas = int(input('TOTAL DE COTAS: '))
    
            dias_uteis = 23
            dividendo_mes = user_cotas * user_dividendo
            investido = user_cotas * user_valor
            DY = (user_dividendo/user_cotas)*100
    
            print(f'\n  INVESTIDO R${investido}\n  TOTAL DE DIVIDENDOS NO MES R${dividendo_mes:.3}\n  DIAS UTEIS '
                  f'{dias_uteis}\n  DIVIDEND YIELD {DY:.3}% MES ANO {DY*12:.3}%')
    
            print(f'\n REFERENCIA RENDA FIXA [MERCADO PAGO]\n\n VALOR R${investido}\n RENDIMENTO R${dias_uteis*(0.04*investido)/100:.2} MES\n')
    
    #cod = fii()
    #cod.Calc()'''

        def Declara(self):
            while True:
                print('Declarar Ações FII [1] Sair [2]')
                user = int(input(': '))

                if user == 1:
                    user_ticket = input('Ticket do FII/Ação: ').upper()
                    texto_ticket = str(user_ticket).strip()
                    print(texto_ticket)

                    texto = str(user_ticket)
                    texto_ult = texto[-2:]

                    print(texto[-2:])

                    if '11' in texto_ult:
                        print('Sem')

                    # for c in texto[-2:]:
                    #    print(c)
                elif user == 2:
                    break

        # teste = decla()
        # teste.Declara()
        def Calc(self):
            tot = 0
            while True:
                Valor = 0
                Cotas = 0
                print('Calcule Seu Preço Medio')

                while True:
                    cotas = int(input(' Cotas: '))
                    #Cotas = Cotas + cotas
                    Cotas += cotas
                    teste = str(cotas)
                    if cotas != 0:
                        tot = tot + 1
                    if cotas == 0:
                        print(' \n Total de Cotas {}\n'.format(Cotas))
                        break
                while True:
                    valor = float(input(' Valor R$ '))
                    Valor = Valor + valor
                    tot = tot - 1
                    #if valor == 0:
                    if tot == 0:
                        print(f'\n Total R${Valor:.2f}')
                        print(f' Preço Medio R$ {Valor/Cotas:.2f}\n')
                        break
                user = str(input(' Continuar ?: ')).strip().upper()
                if user != 'S':
                    break
    try:
        while True:
            print('FII [1] DECLARAÇÃO [2] SAIR [3]')
            user = int(input(': '))
            if user == 1:
                cod = Menu()
                cod.Calc()

            elif user == 2:
                cod = Menu()
                cod.Declara()

            elif user == 3:
                print('Saindo...')
                break

            elif user != 1 and user != 2:
                print('Saindo...')
                break
    except ValueError as erro:
        print(f'Ocorreu Um Erro! [{erro}]')
        exit()
    #teste = fii()
    #teste.Calc()
except ValueError as erro:
    print('Digite O valor No Padrao Ex( R$ 1.5 )')
    exit()
