from telas.personalizacao import separacao, cores

def menu_principal():
    menu = True
    while menu:
        cores('roxo')
        separacao(40)
        cores('limpa')
        cores('ciano')
        print('                         BEM VINDO AO JOGO DA FORCA')
        cores('roxo')
        separacao(40)
        cores('limpa')
        try:
            cores('ciano')
            decisao_menu = int(input('''
                                    MENU PRINCIPAL
            1- Iniciar jogo             2-Regras             3-Sair
            '''))
            cores('limpa')
        except:
            cores('vermelho')
            print('Digite um valor valido !!')
            cores('limpa')
        else:
            if decisao_menu == 1:
                cores('roxo')
                print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-BOM JOGO-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
                cores('limpa')
                menu = False
            elif decisao_menu == 2:
                cores('ciano')
                print('O objetivo deste jogo é descobrir uma palavra adivinhando as letras que ela possui. A cada rodada, um jogador ira escolher uma letra que suspeite fazer parte da palavra. Caso a palavra contenha esta letra, será mostrado em que posição(ões) ela está. Entretanto, caso esta letra não exista na palavra, será desenhada uma parte do corpo do boneco do jogador. Se todas as 6 partes do corpo do boneco estiverem desenhadas, o jogador estará fora da partida.')
                cores('limpa')                
            elif decisao_menu == 3:
                exit() 
            else:
                cores('vermelho')
                print('Digite um valor valido !!')
                cores('limpa')





 
