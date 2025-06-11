import random

TAMANHO = 5
NAVIOS = 3

def inicializa_tabuleiro():
    """Cria um tabuleiro vazio."""
    tabuleiro = [[0 for _ in range(TAMANHO)] for _ in range(TAMANHO)]
    return tabuleiro

def mostra_tabuleiro(tabuleiro):
    """Exibe o tabuleiro no console."""
    print("\nTabuleiro:")
    for linha in tabuleiro:
        for celula in linha:
            if celula == 0:
                print("~ ", end="")
            elif celula == 1:
                print("* ", end="")
            elif celula == 2:
                print("X ", end="")
        print()

def inicia_navios():
    """Posiciona os navios aleatoriamente no tabuleiro."""
    navios = []
    for _ in range(NAVIOS):
        navios.append([random.randint(0, TAMANHO - 1), random.randint(0, TAMANHO - 1)])
    return navios

def valida_tiro(tiro, tabuleiro):
    """Verifica se o tiro é válido (dentro dos limites e não atingiu uma célula já atingida)."""
    linha, coluna = tiro
    return 0 <= linha < TAMANHO and 0 <= coluna < TAMANHO and tabuleiro[linha][coluna] == 0

def dar_tiro(tabuleiro):
    """Solicita ao jogador as coordenadas do tiro e valida a entrada."""
    while True:
        try:
            linha = int(input(f"Digite a linha (0-{TAMANHO - 1}) do tiro: "))
            coluna = int(input(f"Digite a coluna (0-{TAMANHO - 1}) do tiro: "))
            tiro = [linha, coluna]
            if valida_tiro(tiro, tabuleiro):
                return tiro
            else:
                print("Tiro inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite números inteiros.")

def acertou(tiro, navios):
    """Verifica se o tiro atingiu um navio."""
    for navio in navios:
        if navio[0] == tiro[0] and navio[1] == tiro[1]:
            return True
    return False

def dica(tiro, navios, tentativa):
    """Fornece uma dica ao jogador a cada 3 tentativas."""
    print("\nDica: ", end="")
    if tentativa % 3 == 0:
        print(f"Tiro na linha {tiro[0]}, coluna {tiro[1]}.")
    else:
        print("Continue tentando!")

def altera_tabuleiro(tiro, navios, tabuleiro):
    """Atualiza o tabuleiro com o resultado do tiro."""
    linha, coluna = tiro
    if acertou(tiro, navios):
        tabuleiro[linha][coluna] = 2  # Marca como navio atingido
    else:
        tabuleiro[linha][coluna] = 1  # Marca como tiro na água

def main():
    """Função principal do jogo."""
    tabuleiro = inicializa_tabuleiro()
    navios = inicia_navios()

    tentativas = 0
    acertos = 0

    print("\n=== BATALHA NAVAL ===")
    print("Instruções:")
    print("~ = Água")
    print("* = Tiro na água")
    print("X = Navio atingido\n")

    while acertos != NAVIOS:
        mostra_tabuleiro(tabuleiro)
        tiro = dar_tiro(tabuleiro)
        tentativas += 1

        if acertou(tiro, navios):
            print("\n>>> VOCÊ ACERTOU! <<<\n")
            acertos += 1
        else:
            print("\n>>> ÁGUA! <<<\n")

        dica(tiro, navios, tentativas)
        altera_tabuleiro(tiro, navios, tabuleiro)

    print("\n\n=== FIM DE JOGO ===")
    print(f"Você acertou os {NAVIOS} navios em {tentativas} tentativas!\n")
    mostra_tabuleiro(tabuleiro)

if __name__ == "__main__":
    main()
