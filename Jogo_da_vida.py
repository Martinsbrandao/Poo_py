class Celula:
    def __init__(self, x, y, estado):
        self.x = x
        self.y = y
        self.estado = estado


class Tabuleiro:
    def __init__(self, abix=6, ordey=6):
        self.abix = abix
        self.ordey = ordey

    def colocar_cel_no_tabuleiro(self, tabuleiro, lista_cel):
        for celula in lista_cel:
            if celula.estado == True:
                tabuleiro[celula.x][celula.y] = 1
            else:
                tabuleiro[celula.x][celula.y] = 2

        return tabuleiro

    def criar(self):
        tabuleiro = \
            [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

        return tabuleiro

    def realizar_jogada(self, lista_cel, tabuleiro):
        controle_x = 0
        lista_aux = []

        for indice_x in tabuleiro:
            controle_y = 0
            for indice_y in indice_x:
                '''print(controle_x, controle_y, indice_y)'''
                if indice_y == 1 or indice_y == 2:
                    lista_aux.append([controle_x, controle_y, indice_y])
                controle_y += 1
            controle_x += 1

        '''print(f" essa é a diposiçao das celulas anteriores \n {lista_aux}")'''
        lista_aux_2 = []
        for xx, yy, vida in lista_aux:
            contadorr = 0

            for indicee in lista_aux:
                if xx + 1 == indicee[0] and yy == indicee[1] and indicee[2] == 1:
                    contadorr += 1
                elif xx - 1 == indicee[0] and yy == indicee[1] and indicee[2] == 1:
                    contadorr += 1
                elif xx == indicee[0] and yy + 1 == indicee[1] and indicee[2] == 1:
                    contadorr += 1
                elif xx == indicee[0] and yy - 1 == indicee[1] and indicee[2] == 1:
                    contadorr += 1
            '''print(contadorr)'''

            if vida == 1 and contadorr < 2:
                lista_aux_2.append([xx, yy, 2])
            elif vida == 1 and contadorr == 4:
                lista_aux_2.append([xx, yy, 2])
            elif vida == 1 and contadorr > 3:
                lista_aux_2.append([xx, yy, 2])
            elif vida == 2 and contadorr == 3:
                lista_aux_2.append([xx, yy, 1])
            else:
                lista_aux_2.append([xx, yy, 1])

        '''print(lista_aux_2)'''
        return lista_aux_2

    '''
    estado 0 sem celula
    estado 1 celula viva
    estado 2 celula morta
    '''


area = Tabuleiro()

area_jogo = area.criar()

celulas_jogo = [Celula(3, 3, True), Celula(2, 5, True), Celula(2, 6, True), Celula(2, 4, True),
                Celula(1, 5, True), Celula(3, 5, True), Celula(5, 5, False), Celula(5, 4, True), Celula(5, 6, True),
                Celula(4, 5, True), Celula(0, 5, True)]
area_preenchida_com_celulas = area.colocar_cel_no_tabuleiro(area_jogo, celulas_jogo)
'''print(area_preenchida_com_celulas)'''

pos_1rodada = area.realizar_jogada(celulas_jogo, area_preenchida_com_celulas)


print(" Essa e a area original ja incrementada as celulas 0 sem celula 1 cel viva 2 cel morta \n")
for xiz in range(7):
    for yip in range(7):
        print(area_preenchida_com_celulas[yip][xiz], end='')
    print()

'''print(pos_1rodada)'''
'''print(area_jogo)'''

for xxx,yyy,estado in pos_1rodada:
    if estado == 1:
        area_jogo[xxx][yyy] = 1
    else:
        area_jogo[xxx][yyy] = 2
'''print(area_jogo)'''
print()
print("Essa é a area de jogo dpz da primera jogada")
for xizz in range(7):
    for yipp in range(7):
        print(area_jogo[yipp][xizz], end='')
    print()