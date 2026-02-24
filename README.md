# Orbito_Fundamentos_da_Programacao_FP

**Orbito-n - Fundamentos da Programação**

Este projeto foi desenvolvido para a unidade curricular de Fundamentos da Programação (2024/25) no Instituto Superior Técnico. Trata-se de uma adaptação computacional do jogo de tabuleiro Orbito, expandida para suportar múltiplas órbitas (n).

**O que é o Orbito-n?**

O Orbito-n é um jogo de estratégia abstrata para dois jogadores (Preto 'X' e Branco 'O') num tabuleiro quadrangular que contém entre 2 a 5 órbitas concentrícas.

**As Regras Principais**

- Turno Dinâmico: Cada jogada consiste em colocar uma pedra numa posição vazia e, obrigatoriamente, rodar todas as pedras do tabuleiro uma posição em sentido anti-horário na sua respetiva órbita.
- Objetivo: Vence o primeiro jogador a obter k = 2 x n pedras seguidas (horizontal, vertical ou diagonal) após a rotação final do turno.
- Empate: Ocorre se o tabuleiro ficar cheio sem vencedores, ou se ambos os jogadores completarem a linha de k pedras ao mesmo tempo após uma rotação.

**Arquitetura do Projeto (TADs)**

O projeto foca-se na implementação de Tipos Abstratos de Dados para garantir a robustez e a barreira de abstração do código:
- TAD posicao: Representa uma coordenada no tabuleiro (coluna e linha). Inclui funções para calcular adjacências ortogonais e diagonais.
- TAD pedra: Gere a identidade das peças (Branca, Preta ou Neutra) e as suas representações externas.
- TAD tabuleiro: É a estrutura central que gere as órbitas, permite colocar/remover peças e executa a lógica de rotação anti-horária das pedras.

**Estratégias**

O jogo permite jogar contra o computador em dois modos de estratégia:
- Fácil: O computador procura jogar em posições que, após a rotação, fiquem adjacentes às suas peças já colocadas.
- Normal: Utiliza uma heurística que analisa o maior número de peças consecutivas (L <= k) que podem ser obtidas tanto pelo jogador como pelo adversário nas jogadas seguintes.

O enunciado deste projeto está explicado mais detalhadamente no ficheiro pdf. Para o conseguir ler é necessário baixá-lo.

Este foi o meu segundo contacto com a programação. Contém alguns erros de implementação.
