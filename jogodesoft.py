#Eduardo Heitor
#Professor: Luciano Soares 
#projeto jogo Bacará 

import random
continuar = True
baralho1 = 52
baralho2 = 312
baralho3 = 416
fichas=100

#contador de cartas já usadas 
i = 0

print("Seja bem vindo ao bacará!, pedimos apenas que suas apostas sejam valores inteiros :)")

# definindo quantidade de cartas
x = int(input('quantos baralhos deseja: 1, 6 ou 8?'))
if x == 1:
    quantidadecartas = baralho1
elif x == 6:
    quantidadecartas = baralho2
else:
    quantidadecartas = baralho3 

#comissao da casa 
if quantidadecartas == baralho1:
    comissaoj = 0.0129
    comissaob = 0.0101
    comissaoe = 0.1575
elif quantidadecartas == baralho2:
    comissaoj = 0.0124
    comissaob = 0.0106
    comissaoe = 0.1444
else:
    comissaoj = 0.0124
    comissaob = 0.0106
    comissaoe = 0.1436

while quantidadecartas > i:

    while continuar == True:
        
        print('Você tem {} fichas'.format (fichas))
        valor = int(input('Quanto deseja apostar ?'))
        aposta = input('Em quem deseja apostar? ( suas opções de aposta são: jogador, banco, empate)')
        
        #valores das cartas
        cartaj = random.randint(1,13)
        if cartaj > 9:
            cartaj = 0
        cartaj1 = random.randint(1,13)
        if cartaj1 > 9:
            cartaj1 = 0
        cartaj2 = random.randint(1,13)
        if cartaj2 > 9:
            cartaj2 = 0
        cartab = random.randint(1,13)
        if cartab > 9:
            cartab = 0
        cartab1 = random.randint(1,13)
        if cartab1 > 9:
            cartab1 = 0
        cartab2 = random.randint(1,13)
        if cartab2 > 9:
            cartab2 = 0
        somacartasj  = cartaj + cartaj1
        somacartasb = cartab + cartab1
        
        #cartas recebidas pelo jogador:
        if cartaj == 1 and cartaj1 == 1:
            print('o jogador recebeu um A e um outro A')
        elif cartaj == 1:
            print('o jogador recebeu um A e um {}'.format(cartaj1))
        elif cartaj1 == 1:
            print('o jogador recebeu um A e um {}'.format(cartaj)) 
        else:
            print('o jogador recebeu um {} e um {}'.format(cartaj, cartaj1))

        #cartas recebida pelo banco:
        if cartab == 1 and cartab1 == 1:
            print('o banco recebeu um A e um outro A')
        elif cartab == 1:
            print('o banco recebeu um A e um {}'.format(cartab1))
        elif cartab1 == 1:
            print('o banco recebeu um A e um {}'.format(cartab)) 
        else:
            print('o banco recebeu um {} e um {}'.format(cartab, cartab1))

         
        
        # condicoes da somatória das cartas
        if somacartasj >= 20:
            somacartasj = somacartasj - 20
        elif somacartasj >= 10:
            somacartasj = somacartasj - 10
        if somacartasb >= 20:
            somacartasb = somacartasb - 20       
        elif somacartasb >= 10:
            somacartasb = somacartasb - 10

        #condicao para o jogo acabar instantaneamente:    
        if somacartasj == 8 or somacartasj == 9 or somacartasb == 8 or somacartasj == 9:
            if somacartasj == 8 or somacartasj == 9 and somacartasb == 8 or somacartasb == 9:
                if aposta == 'empate':
                    fichas = fichas + valor*8 - (valor*8)*comissaoe
                    print('voce ganhou {} fichas'.format(valor*8 - (valor*8)*comissaoe))
                    continuar = False
                else:
                    fichas = fichas - valor 
                    print('voce perdeu {} fchas'.format(valor)) 
                    continuar = False           
            elif somacartasj == 8 or somacartasj == 9:
                if aposta == 'jogador':
                    fichas = fichas + valor - valor*comissaoj
                    print('voce ganhou {} fichas'.format(valor - valor*comissaoj))
                    continuar = False
                else:
                    fichas = fichas - valor 
                    print('voce perdeu {} fichas'.format(valor))
                    continuar = False
            else:
                if aposta == 'banco':
                    fichas = fichas + valor*0.95 - (valor*0.95)*comissaob
                    print('voce ganhou {} fichas'.format(valor*0.95 - (valor*0.95)*comissaob))
                    continuar = False
                else:
                    fichas = fichas - valor 
                    print('voce perdeu {} fichas'.format(valor)) 
                    continuar = False   
                            
                
        #condicao para dar mais uma carta ou nao:
        if somacartasj <= 5:
            somacartasj = somacartasj + cartaj2
            print('o jogador recebeu mais uma carta: {}'.format(cartaj2))
            i +=1
        if somacartasb <= 5:
            somacartasb = somacartasb + cartab2
            print('o banco recebeu mais uma carta: {}'.format(cartab2))
            i +=1

        # condicoes para nova somatória das cartas
        if somacartasj >= 20:
            somacartasj = somacartasj - 20
        elif somacartasj >= 10:
            somacartasj = somacartasj - 10
        if somacartasb >= 20:
            somacartasb = somacartasb - 20       
        elif somacartasb >= 10:
            somacartasb = somacartasb - 10
        
        # quem ganhou o jogo?
        j = (somacartasj - 9)**2
        b = (somacartasb - 9)**2
            
        if j<b:
            if aposta == 'jogador':
                fichas = fichas + valor - valor*comissaoj
                print('voce ganhou {} fichas'.format(valor - valor*comissaoj))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fichas'.format(valor))
        elif j>b:
            if aposta == 'banco':
                fichas = fichas + valor*0.95 - (valor*0.95)*comissaob
                print('voce ganhou {} fichas'.format(valor*0.95))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fichas'.format(valor))
        else:
            if aposta == 'empate':
                fichas = fichas + valor*8 - (valor*8)*comissaoe
                print('voce ganhou {} fichas'.format(valor*8 - (valor*8)*comissaoe))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fichas'.format(valor))

        i += 4
        
        prosseguir2 = input('deseja continuar?') 
        if prosseguir2 == 'nao' or prosseguir2 == 'não':
            print('voce acabou terminando o jogo com {} fichas'.format(fichas))
            continuar = False
        else:
            continuar = True                 

    
    
    