# This is the Python script for your project

# Segundo projeto- Orbito-n

# 2.1.1- construtor
def cria_posicao(col, lin, verifica=True):
    """
    Devolve a posição correspondente a um caracter e a um inteiro, validando
    os argumentos.

    Argumentos: str, int
    Return: tuple
    """
    if verifica:
        if type(col) != str or col not in \
            ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j") or \
                type(lin) != int or not 1 <= lin <= 10:
            raise ValueError("cria_posicao: argumentos invalidos")

    return col, lin

# 2.1.1- seletores
def obtem_pos_col(p):
    """
    Determina a coluna da posição p.

    Argumento: tuple
    Return: str
    """
    return p[0]

def obtem_pos_lin(p):
    """
    Determina a linha da posição p.

    Argumento: tuple
    Return: int
    """
    return p[1]

# 2.1.1- reconhecedor
def eh_posicao(arg):
    """
    Verifica se arg é uma posição dentro dos limites do tabuleiro através da         ttttttttttttttttt
    verificação da coluna e da linha.

    Argumento:

    """

    if type(arg) != tuple or len(arg) != 2:
        return False

    col, lin = obtem_pos_col(arg), obtem_pos_lin(arg)

    if not type(col) == str and col in "abcdefghij" and \
        type(lin) == int and 1 <= lin <= 10:
        return False

    else:
        return True

# 2.1.1- teste
def posicoes_iguais(p1, p2):
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False

    if obtem_pos_col(p1) == obtem_pos_col(p2) and \
        obtem_pos_lin(p1) == obtem_pos_lin(p2):
        return True

    return False

# 2.1.1- transformadores
def posicao_para_str(p):
    return obtem_pos_col(p) + str(obtem_pos_lin(p))

def str_para_posicao(s):
    return cria_posicao(s[0], int(s[1]))

# 2.1.1- funções de alto nível
def eh_posicao_valida(p, n):
    if not eh_posicao(p):
        return False
    
    col, lin = obtem_pos_col(p), obtem_pos_lin(p)

    return 1 <= lin <= 2 * n and col in "abcdefghij"

def operações_adjacentes(deslocamentos_pos_adjacentes, p, n): #função auxiliar
    adjacentes = []
    col, lin = obtem_pos_col(p), obtem_pos_lin(p)

    for deslocamento in deslocamentos_pos_adjacentes:
        deslocamento_col = chr(ord(col) + deslocamento[0])
        deslocamento_lin = lin + deslocamento[1]
        nova_pos = (deslocamento_col, deslocamento_lin)

        if eh_posicao_valida(nova_pos, n):
            adjacentes.append(nova_pos)

    return adjacentes

def obtem_posicoes_adjacentes(p, n, d):
    """
    Função de alto nível que devolve um tuplo com as posições adjacentes de p se
    d for True ou as posições adjacentes ortogonais se d for False.
    Em ambos os casos, para as posições ficarem em sentido horário e começarem
    na pos por cima de p, cria-se um ciclo que itera pelas posições na ordem
    pretendida e descarta aquelas que não pertencem ao tabuleiro. Para as
    adjacentes englobas as posições verticais, horizontais e diagonais. O outro
    caso não engloba as diagonais.

    {tuple, int, bool} --> {tuple}
    """
    #posições adjacentes
    if d == True:
        deslocamentos_pos_adjacentes = \
        [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        adjacentes = operações_adjacentes(deslocamentos_pos_adjacentes, p, n)

    #posições adjacentes ortogonais
    else:
        deslocamentos_pos_adjacentes = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        adjacentes = operações_adjacentes(deslocamentos_pos_adjacentes, p, n)

    return tuple(reversed(adjacentes))


def calcula_orbita_posicao(pos, n): #função auxiliar
    #valor minimo entre a distância à órbita mais exterior e à órbita mais
    #interior, tanto para as linhas como para as colunas

    lin = obtem_pos_lin(pos)
    col = ord(obtem_pos_col(pos)) - ord("a") + 1
    dist = min(lin - 1, 2 * n - lin, col - 1, 2 * n - col)

    return n - dist  #obter a órbita da posição

def ordena_posicoes(t, n):
    def prioridade_ordem(pos):
        orbita = calcula_orbita_posicao(pos, n)
        lin = obtem_pos_lin(pos)
        col = obtem_pos_col(pos)

        return (orbita, lin, col)

    #cada posição de t é chamada e ordenada consoante prioridade_ordem
    return tuple(sorted(t, key=prioridade_ordem))

#2.1.2- construtores
def cria_pedra_branca():
    return ("O",)

def cria_pedra_preta():
    return ("X",)

def cria_pedra_neutra():
    return (" ",)

#2.1.2- reconhecedor
def eh_pedra(arg):
    return type(arg) == tuple and len(arg) == 1 and arg[0] in \
        (cria_pedra_branca()[0], cria_pedra_preta()[0], cria_pedra_neutra()[0])

def eh_pedra_branca(p):
    return eh_pedra(p) and p == cria_pedra_branca()

def eh_pedra_preta(p):
    return eh_pedra(p) and p == cria_pedra_preta()

#2.1.2- teste
def pedras_iguais(p1, p2):
    if not eh_pedra(p1) or not eh_pedra(p2):
        return False

    return p1 == p2

#2.1.2- transformador
def pedra_para_str(p):
    return p[0]

#2.1.2- funções de alto nível
def eh_pedra_jogador(p):
    """
    Devolve True caso a pedra seja de um jogador e False caso contrário.
    Utiliza as operações básicas eh_pedra_branca e eh_pedra_preta.

    {tuple} --> {bool}
    """
    return eh_pedra_branca(p) or eh_pedra_preta(p)

def pedra_para_int(p):
    """
    Devolve 1, -1 ou 0 dependendo se a pedra é preta, branca ou neutra.
    Utiliza as operações básicas eh_pedra_branca e eh_pedra_preta.

    {tuple} --> {int}
    """
    if eh_pedra_preta(p):
        return 1

    elif eh_pedra_branca(p):
        return -1

    else:
        return 0

# 2.1.3- construtor
def cria_tabuleiro_vazio(n):
    if type(n) != int or not 2 <= n <= 5:
        raise ValueError("cria_tabuleiro_vazio: argumento invalido")

    colunas, linhas = [], []
    tab = {}

    for coluna in range(0, 2 * n):
        colunas.append(chr(coluna + ord("a")))

    for linha in range(1, 2 * n + 1):
        linhas.append(linha)

    for linha in linhas:
        for coluna in colunas:
            pos = cria_posicao(coluna, linha)
            tab[pos] = cria_pedra_neutra()

    return tab

def cria_tabuleiro(n, tp, tb):
    if not 2 <= n <= 5 or type(tp) != tuple or type(tb) != tuple:
        raise ValueError("cria_tabuleiro: argumentos invalidos")

    tab = cria_tabuleiro_vazio(n)

    # quando a chave em tab for igual às posições de tp ou tb, substituir o seu
    # valor pelo símbolo que respresenta a cor das pedras
    for pos_preta in tp:
        if not eh_posicao(pos_preta) or not eh_posicao_valida(pos_preta, n):
            raise ValueError("cria_tabuleiro: argumentos invalidos")
        tab[pos_preta] = cria_pedra_preta()

    for pos_branca in tb:
        if not eh_posicao(pos_branca) or not eh_posicao_valida(pos_branca, n):
            ValueError("cria_tabuleiro: argumentos invalidos")
        tab[pos_branca] = cria_pedra_branca()

    return tab

def cria_copia_tabuleiro(t):
    return t.copy()

#2.1.3- seletores
def obtem_numero_orbitas(t):
    return int(len(t) ** 0.5 / 2)

def obtem_pedra(t, p):
    for pos in t:
        if pos == p:
            return t[pos]  # alterar, não usar diretamente

def obtem_linha_horizontal(t, p):
    linha = []
    lin = obtem_pos_lin(p)

    for pos in t:
        #garantir que todas as pos da mesma linha pertençam à lista
        if lin == obtem_pos_lin(pos):
            linha.append((pos, t[pos]))

    return tuple(linha)

def obtem_linha_vertical(t, p):
    coluna = []
    col = obtem_pos_col(p)

    for pos in t:
        if col == obtem_pos_col(pos):
            coluna.append((pos, t[pos]))

    return tuple(coluna)

def obtem_linhas_diagonais(t, p):
    linha, coluna = obtem_pos_lin(p), obtem_pos_col(p)
    n = obtem_numero_orbitas(t)
    coluna_em_num = ord(coluna) - ord("a") + 1

    def diagonais(t, p):
        x1, y1 = coluna_em_num, linha
        x2, y2 = coluna_em_num + 1, linha + 1
        diagonais = []

        #posições da diagonal antes de p
        while x1 > 0 and y1 > 0:
            diagonais.append((chr(ord("a") + x1 - 1), y1))
            x1 -= 1
            y1 -= 1

        #posições da diagonal depois de p
        while x2 <= (n * 2) and y2 <= (n * 2):
            diagonais.append((chr(ord("a") + x2 - 1), y2))
            x2 += 1
            y2 += 1

        return tuple(sorted(diagonais))

    def antidiagonais(t, p):
        x3, y3 = coluna_em_num, linha
        x4, y4 = coluna_em_num - 1, linha + 1
        antidiagonais = []

        #posições da diagonal depois de p
        while x3 <= (n * 2) and y3 > 0:
            antidiagonais.append((chr(ord("a") + x3 - 1), y3))
            x3 += 1
            y3 -= 1

        #posições da diagonal antes de p
        while x4 > 0 and y4 <= (n * 2):
            antidiagonais.append((chr(ord("a") + x4 - 1), y4))
            x4 -= 1
            y4 += 1

        return tuple(sorted(antidiagonais))

    #determinar as pedras nas pos da diagonal e antidiagonal
    diagonal, antidiagonal = diagonais(t, p), antidiagonais(t, p)
    diagonal_pedra, antidiagonal_pedra = [], []

    for pos in diagonal:
        posicao = cria_posicao(pos[0], pos[1])
        diagonal_pedra.append((posicao, obtem_pedra(t, posicao)))

    for pos in antidiagonal:
        posicao = cria_posicao(pos[0], pos[1])
        antidiagonal_pedra.append((posicao, obtem_pedra(t, posicao)))

    return tuple(diagonal_pedra), tuple(antidiagonal_pedra)

def obtem_posicoes_pedra(t, j):
    pos_com_pedra = []

    for pos in t:
        if t[pos] == j:
            pos_com_pedra.append(pos)

    pos_ordenadas_com_pedra = \
        ordena_posicoes(tuple(pos_com_pedra), obtem_numero_orbitas(t))

    return tuple(pos_ordenadas_com_pedra)

#2.1.3- modificadores
def coloca_pedra(t, p, j):
    t[p] = j
    return t

def remove_pedra(t, p):
    t[p] = cria_pedra_neutra()
    return t

#2.1.3- reconhecedor
def eh_tabuleiro(arg):
    for pos in arg:
        if not eh_pedra(arg[pos]) or not \
            eh_posicao_valida(pos, obtem_numero_orbitas(arg)):
            return False

    return True

#2.1.3- teste
def tabuleiros_iguais(t1, t2):
    if not eh_tabuleiro(t1) or not eh_tabuleiro(t2):
        return False

    elif any(not pedras_iguais(t1[pos], t2[pos]) for pos in t1):
        return False

    #usar zip para agrupar as chaves de t1 e t2; utilização de um ciclo para
    #percorrer os pares; usar posicoes_iguais para comparar as chaves de t1 e t2
    elif any(not posicoes_iguais(pos1, pos2) \
             for pos1, pos2 in zip(t1.keys(), t2.keys())):
        return False

    return True

#2.1.3- transformador
def tabuleiro_para_str(t):
    n = obtem_numero_orbitas(t)
    #tab_coordenadas = posicoes_para_coordenadas(t)
    num_linhas, num_colunas = n * 2, n * 2

    col = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    lin = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]

    #obter primeira linha
    linha_inicial = "    " + "   ".join(col[:num_colunas]) + "\n"
    tab_str = linha_inicial

    for linha in range(1, num_linhas + 1):
        linha_tab = lin[linha - 1] + " "

        for coluna in range(num_colunas):
            pos = (col[coluna], linha)

            #determinar qual é a pedra na posição (assumindo t dicionário)
            pedra = t.get(pos, (" ",))

            #adiciona a str correspondente à pedra
            linha_tab += f"[{pedra_para_str(pedra[0])}]"

            if not coluna == num_colunas - 1:
                linha_tab += "-"

        #mudar de linha depois de percorrer todas as colunas
        tab_str += linha_tab + "\n"

        if not linha == num_linhas:
            tab_str += ("    |" + "   |" * (num_colunas - 1)) + "\n"

    return tab_str.rstrip()  #retirar \n adicionados desnecessariamente


#2.1.3- funções de alto nível
def move_pedra(t, p1, p2):
    tab_remove_p1 = remove_pedra(t, p1)
    tab_coloca_p2 = coloca_pedra(tab_remove_p1, p2, obtem_pedra(t, p1))

    return tab_coloca_p2

def obtem_posicao_seguinte(t, p, s):
    n = obtem_numero_orbitas(t)
    col = ord(obtem_pos_col(p)) - ord("a") + 1
    lin = obtem_pos_lin(p)
    orbita_pos = calcula_orbita_posicao(p, n)

    if s:  #sentido-horario
        if lin == orbita_pos and col < (n * 2) - orbita_pos + 1:  # Direita
            prox_lin = lin
            prox_col = col + 1

        elif col == (n * 2) - orbita_pos + 1 and lin < (n * 2) - orbita_pos + 1:
            prox_lin = lin + 1
            prox_col = col

        elif lin == (n * 2) - orbita_pos + 1 and col > orbita_pos:
            prox_lin = lin - 1
            prox_col = col

        elif col == orbita_pos and lin > orbita_pos:
            prox_lin = lin - 1
            prox_col = col

    else:  #sentido anti-horario
        if lin == orbita_pos and col > orbita_pos:  # Esquerda
            prox_lin = lin
            prox_col = col - 1

        elif col == orbita_pos and lin < (n * 2) - orbita_pos + 1:  # Baixo
            prox_lin = lin + 1
            prox_col = col

        elif lin == (n * 2) - orbita_pos + 1 and col < (n * 2) - orbita_pos + 1:  # Direita
            prox_lin = lin
            prox_col = col + 1

        elif col == (n * 2) - orbita_pos + 1 and lin > orbita_pos:
            prox_lin = lin - 1
            prox_col = col

    prox_pos = cria_posicao(chr(ord("a") + prox_col - 1), prox_lin)

    return prox_pos

def verifica_linha_pedras(t, p, j, k):
    # if obtem_pedra(t, p) != j:
    #     return False

    #Tuplos de linhas contendo posições horizontais, verticais e diagonais
    tuplo_linhas = (obtem_linha_vertical(t, p), obtem_linha_horizontal(t, p),\
        obtem_linhas_diagonais(t, p)[0], obtem_linhas_diagonais(t, p)[1])               #veeeeeeeeeeeeeeeeer

    for tuplo in tuplo_linhas:
        idx = tuplo.index(p)
        contar1 = 1
        contar2 = -1

        #Verifica à direita/abaixo
        for i in range(len(tuplo[idx:]) - 1):
            contar2 += 1
            if pedras_iguais(obtem_pedra(t, tuplo[idx]), \
                             obtem_pedra(t, tuplo[idx + 1 + contar2])):
                contar1 += 1
            else:
                break

        if contar1 >= k:
            return True

        contar2 = -1

        #Verifica à esquerda/acima
        for i in range(len(tuplo[: idx + 1]) - 1):
            contar2 += 1
            if pedras_iguais(obtem_pedra(t, tuplo[idx]), \
                             obtem_pedra(t, tuplo[idx - 1 - contar2])):
                contar1 += 1
            else:
                break

        if contar1 >= k:
            return True

    return False






# 01 02 03 04
# 05 06 07 08
# 09 10 11 12
# 13 14 15 16

# pos_inicial
# pos = obtem_posicao_seguinte(t, pos_inicial, s)

# while pos != pos_inicial:
    # positions.append(pos)
    # pos = obtem_posicao_seguinte(t, pos, s)

# obtem_pedra... > tuplo pedras
# tuplo_pedras = tuplo_pedras[1:] + tuplo_pedras[:1]



