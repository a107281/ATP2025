# TPC2: Jogo dos 21 fósforos

## Beatriz Maia Oliveira A107281

## Resumo
O TPC2 consistiu em desenvolver o código, em Python, para o jogo dos 21 fósforos.

### O jogo
* No início do jogo, há 21 fósforos;
* Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar;
* Os jogadores jogam alternadamente;
* **Quem tirar o último fósforo perde!**

### O programa 
* O jogo deverá ter dois modos: o jogador joga em primeiro lugar e o computador começa a jogar em segundo lugar e, no segundo modo, o computador começa em primeiro; 
* Quando o computador começa a jogar em segundo lugar, deve ganhar sempre o jogo;
* Quando o computador começa a jogar em primeiro lugar, se o utilizador cometer um erro de cálculo, o computador deverá passar para a posição de vencedor e ganhar o jogo.

## Resultados
```python
import random

def computador_1(fosforos):
    jogada = (fosforos-1) % 5

    if jogada == 0:
        jogada = random.randint(1,4)

    if jogada > fosforos:
        jogada = fosforos

    print(f"O Computador retirou {jogada} fósforos.")
    print(f"Restam {fosforos - jogada} fósforos.")
    return jogada

    

def jogador_1(fosforos):
    jogada = int(input("Escolha o número de fósforos que gostaria de tirar (1-4): "))

    if jogada < 1 or jogada > 4:
        print("Jogada inválida. Tente novamente.")
        return jogador_1(fosforos)
    
    if jogada > fosforos:
        print(f"Não podes tirar mais do que {fosforos} fósforos!")
        return jogador_1(fosforos)
    
    print(f"Retiraste {jogada} fósforos: Restam {fosforos - jogada} fósforos.") 
    return jogada



def modo_jogador_1():
    fosforos = 21

    while fosforos > 0:
        jogada_jogador = jogador_1(fosforos)
        fosforos = fosforos - jogada_jogador
        if fosforos == 0:
            print("Perdeste! O computador venceu.")
            return
        
        jogada_computador = computador_1(fosforos)
        fosforos = fosforos - jogada_computador
        if fosforos == 0:
            print("O computador perdeu! Ganhaste o jogo!")
            return


def modo_computador_1():
    fosforos = 21
    
    while fosforos > 0:
        jogada_computador = computador_1(fosforos)
        fosforos = fosforos - jogada_computador
        if fosforos == 0:
            print("O computador perdeu! Ganhaste o jogo!")
            return

        jogada_jogador = jogador_1(fosforos)
        fosforos = fosforos - jogada_jogador
        if fosforos == 0:
            print("Perdeste! O computador venceu.")
            return



def comecar_jogo():
    print("Bem-vindo ao Jogo dos 21 Fósforos!")
    print("Começa por escolher o modo que queres jogar:")
    print("(1) O Jogador começa primeiro")
    print("(2) O Computador começa primeiro")
    
    cond = True
    while cond:
        escolha = input("Escolhe o modo de jogo (1 ou 2): ")
        if escolha == "1":
            modo_jogador_1()
            cond = False
        elif escolha == "2":
            modo_computador_1()
            cond = False
        else:
            print("Escolha inválida. Por favor, escolhe 1 ou 2.")


comecar_jogo()
