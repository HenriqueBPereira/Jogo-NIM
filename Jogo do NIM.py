def computador_escolhe_jogada(n, m):
    if n==1:
        jogada=1
        print("O computador tirou uma peça.")
        return jogada
    if n<=m:
        jogada=n
        if jogada==1:
            print("O computador tirou uma peça.")
        else:
            print("O computador tirou", jogada,"peças.")
        return jogada
    if n>m:
        retirada=m-1
        if (n-m)%(m+1)==0:
            jogada=m
            if jogada==1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", jogada,"peças.")
            return jogada
            
        if (n-m)%(m+1)!=0 and retirada>0:
            
            while (n-m)%(m+1)!=0 and retirada>0:
                if (n-retirada)%(m+1)==0:
                    jogada=retirada
                    if jogada==1:
                        print("O computador tirou uma peça.")
                    else:
                        print("O computador tirou", jogada,"peças.")
                    return jogada
                else:
                    retirada=retirada-1
                if retirada==0:
                    print("jogada:",jogada)
                    jogada=m
                    return jogada
        else:
            jogada=m
            return jogada

def usuario_escolhe_jogada(n, m):
    aux=False
    while aux==False:
        jogada=int(input("Quantas peças você vai tirar? "))
        if (n-jogada)<0 or jogada>m:
            print("Oops! Jogada inválida! Tente de novo.")
        else:
            aux=True
    if jogada == 1:
        print("Você tirou uma peça.")        
    if jogada >1:
        print("Você tirou ", jogada,"peças.")
    return jogada     

def NIM(n,m,comp):
    while n>0:
        if comp==True:
            jogada=computador_escolhe_jogada(n, m)
            n=n-jogada
            if n==0:
                print("Fim do jogo! O computador ganhou!")
                return 1
            else:
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam ", n," peças no tabuleiro.")
                comp=False
        if comp==False:
            jogada=usuario_escolhe_jogada(n, m)
            n=n-jogada
            if n==0:
                print("Fim do jogo! O usuario ganhou!")
                return 0
            else:
                if n==1:
                    print("Agora resta apenas uma peça no tabuleiro.")
                else:
                    print("Agora restam ", n," peças no tabuleiro.")
                comp=True            

print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

condicao=False
while condicao==False:
    tipo_de_jogo=int(input())
    if tipo_de_jogo==1 or tipo_de_jogo==2:
        condicao=True
    else:
        print("Oops! Opção inválida! Tente de novo.")

if tipo_de_jogo==1:
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada?"))
    if n%(m+1)==0:
        print("Você começa!")
        comp=False
    else:
        print("Computador começa!")
        comp=True
    aux1=NIM(n,m,comp)
if tipo_de_jogo==2:
    computador=0
    usuario=0
    rodada=1
    while rodada!=4:
        print("**** Rodada",rodada," ****")
        n=int(input("Quantas peças?"))
        m=int(input("Limite de peças por jogada?"))
        if n%(m+1)==0:
            print("Você começa!")
            comp=False
        else:
            print("Computador começa!")
            comp=True
        vencedor=NIM(n,m,comp)
        if vencedor==1:
            computador=computador+1
        else:
            usuario=usuario+1
        rodada=rodada+1
    print("**** Final do campeonato! ****")
    print("Placar: Você",usuario,"X",computador,"Computador")