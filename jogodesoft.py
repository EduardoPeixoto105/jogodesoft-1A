#Eduardo Heitor
#Professor: Luciano Soares 
#projeto jogo Bacará 
import random
fichas=100
print("Seja bem vindo ao bacará!, pedimos apenas que suas apostas sejam valores inteiros :)")

while fichas>0:
    
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
    

    # condicoes da somatória das cartas
    if somacartasj >= 20:
        somacartasj = somacartasj - 20
    elif somacartasj >= 10:
        somacartasj = somacartasj - 10
    if somacartasb >= 20:
        somacartasb = somacartasb - 20       
    elif somacartasb >= 10:
        somacartasb = somacartasb - 10


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

    #condicao para o jogo acabar instantaneamente:    
    if somacartasj == 8 or somacartasj == 9 or somacartasb == 8 or somacartasj == 9:
        if somacartasj == 8 or somacartasj == 9 and somacartasb == 8 or somacartasj == 9:
            if aposta == 'empate':
                fichas = fichas + valor*8
                print('voce ganhou {} fichas'.format(valor*8))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fchas'.format(valor))            
        elif somacartasj == 8 or somacartasj == 9:
            if aposta == 'jogador':
                fichas = fichas + valor
                print('voce ganhou {} fichas'.format(valor))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fichas'.format(valor))
        elif somacartasb == 8 or somacartasj == 9:
            if aposta == 'banco':
                fichas = fichas + valor*0.95
                print('voce ganhou {} fichas'.format(valor*0.95))
            else:
                fichas = fichas - valor 
                print('voce perdeu {} fichas'.format(valor))                        
            
    #condicao para dar mais uma carta ou nao:
    if somacartasj <= 5:
        somacartasj = somacartasj + cartaj2
        print('o jogador recebeu mais uma carta: {}'.format(cartaj2))
    if somacartasb <= 5:
        somacartasb = somacartasb + cartab2
        print('o banco recebeu mais uma carta: {}'.format(cartab2))
    
    # quem ganhou o jogo?
    j = (somacartasj - 9)**2
    b = (somacartasb - 9)**2
          
    if j<b:
        if aposta == 'jogador':
            fichas = fichas + valor
            print('voce ganhou{} fichas'.format(valor))
        else:
            fichas = fichas - valor 
            print('voce perdeu {} fichas'.format(valor))
    elif j>b:
        if aposta == 'banco':
            fichas = fichas + valor*0.95
            print('voce ganhou {} fichas'.format(valor*0.95))
        else:
            fichas = fichas - valor 
            print('voce perdeu {} fichas'.format(valor))
    else:
        if aposta == 'empate':
            fichas = fichas + valor*8
            print('voce ganhou {} fichas'.format(valor*8))
        else:
            fichas = fichas - valor 
            print('voce perdeu {} fichas'.format(valor))

    
    
    