from telas.mostra_forca import forca
from telas.remove_acentos import transformacao
from telas.menu import menu_principal
from telas.personalizacao import cores

jogo = True
while jogo:
    nao_descobriu = True
    pontos_desafiador = None
    pontos_desafiado = None
    letras_descobertas = []
    letras_escolhidas = []
    erros = 0
    menu_principal()
# Define os nomes dos jogadores
    cores('ciano')
    jogador1 = input('Informe o nome do primeiro jogador: ')
    jogador2 = input('Informe o nome do segundo jogador: ')
    if jogador1 == '':
        jogador1 = 'jogador1'
    if jogador2 == '':
        jogador2 = 'jogador2'
# Define o jogador desafiador e o desafiado
    while True:
        cores('ciano')
        jogador_desafiador = input('Defina quem sera o desafiador: jogador1 ou jogador2 ')
        if jogador_desafiador == 'jogador1' or jogador_desafiador == '1':
            jogador_desafiador = jogador1
            jogador_desafiado = jogador2
            break
        elif jogador_desafiador == 'jogador2' or jogador_desafiador == '2':
            jogador_desafiador = jogador2
            jogador_desafiado = jogador1
            break
        else:
            cores('vermelho')
            print('Apenas jogador1/1, ou jogador2/2 são validos')
            cores('limpa')
# Define a palavra do jogo
    while True:
        cores('ciano')
        palavra = transformacao(input(f'{jogador_desafiador} escolha a palavra do jogo, cuidado para que ninguém veja!! '))
        if palavra.isalpha():
            palavra_escolhida = list(palavra)
            for i in palavra_escolhida:
                letras_descobertas.append('_')
            break
        else:
            cores('vermelho')
            print('Escolha uma palavra válida, sem acentuação e números!!')
            cores('limpa')
# Adivinha as letras 
    while nao_descobriu:
        cores('ciano')
        escolha_desafiador = transformacao(input(f'{jogador_desafiado} escolha uma letra para tentar advinhar ou chute a palavra: '))
        cores('limpa')
        if escolha_desafiador.isalpha():
            if len(list(escolha_desafiador)) == 1:
                if escolha_desafiador in letras_escolhidas:
                    cores('vermelho')
                    print('Letra ja escolhida ! ')
                    cores('limpa')
                else:
                    letras_escolhidas.append(escolha_desafiador)
                    if escolha_desafiador not in palavra_escolhida:
                        erros += 1
                    for i in range(0, len(palavra_escolhida)):
                        if escolha_desafiador == palavra_escolhida[i]:
                            letras_descobertas[i] = escolha_desafiador                
            else:
                if list(escolha_desafiador) == palavra_escolhida:
                    cores('verde')
                    print('Parabéns voçe acertou a palavra !!!')
                    cores('limpa')
                    cores('amarelo')
                    print(palavra_escolhida)
                    cores('limpa')
                    break
                else:
                    cores('vermelho')
                    print('Voçe errou a palavra !!!')
                    cores('limpa')
                    erros += 1
            cores('amarelo')
            print(f'Letras digitadas {letras_escolhidas}')
            cores('ciano')
            forca(erros)
            cores('amarelo')
            print(letras_descobertas)
            cores('limpa')
            if erros == 6:
                nao_descobriu = False
            if letras_descobertas == list(palavra_escolhida):
                cores('verde')
                print('Voçe descobriu a palavra !!!')
                cores('limpa')
                nao_descobriu = False   
        else:
            cores('vermelho')
            print('Apenas letras são permitidas !!')
            cores('limpa')