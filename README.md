# Batalha Naval em Python

Este é um jogo de Batalha Naval implementado em Python. O objetivo do jogo é afundar todos os navios do computador antes que ele afunde os seus.

## Como Jogar

1.  **Início do Jogo:**
    *   Ao iniciar o jogo, o tabuleiro será exibido no console.
    *   O tabuleiro mostra o estado atual do jogo:
        *   `~`: Água (célula não atingida)
        *   `*`: Tiro na água
        *   `X`: Navio atingido

2.  **Dando um Tiro:**
    *   O jogo solicitará que você insira as coordenadas (linha e coluna) do seu tiro.
    *   As coordenadas devem ser números inteiros dentro dos limites do tabuleiro (0 a 4, neste caso).
    *   Se você inserir coordenadas inválidas (fora dos limites ou não numéricas), o jogo solicitará que você tente novamente.

3.  **Resultado do Tiro:**
    *   Após dar um tiro, o jogo informará se você acertou um navio ou atingiu a água.
    *   O tabuleiro será atualizado para refletir o resultado do tiro.

4.  **Dicas:**
    *   A cada 3 tentativas, o jogo fornecerá uma dica, mostrando as coordenadas do seu último tiro.

5.  **Fim do Jogo:**
    *   O jogo continua até que você acerte todos os navios.
    *   Ao final, o jogo exibirá uma mensagem de parabéns e mostrará o número de tentativas que você precisou para afundar todos os navios.

## Como Rodar a Aplicação

### Pré-requisitos

*   **Python:** Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/).  Recomenda-se usar Python 3.6 ou superior.

### Passos para Executar

1.  **Baixe o Código:**
    *   Baixe o arquivo `batalha_naval.py` contendo o código do jogo.

2.  **Abra o Terminal ou Prompt de Comando:**
    *   Abra o terminal (Linux/macOS) ou o prompt de comando (Windows).

3.  **Navegue até o Diretório:**
    *   Use o comando `cd` para navegar até o diretório onde você salvou o arquivo `batalha_naval.py`.  Por exemplo:

        ```bash
        cd /caminho/para/o/seu/diretorio
        ```

4.  **Execute o Jogo:**
    *   Execute o jogo usando o comando:

        ```bash
        python batalha_naval.py
        ```

5.  **Divirta-se!**
    *   O jogo será iniciado no seu terminal. Siga as instruções na tela para jogar.

## Controles

*   **Linha:** Insira o número da linha (0 a 4) e pressione Enter.
*   **Coluna:** Insira o número da coluna (0 a 4) e pressione Enter.

## Exemplo de Jogo

```markdown
# Batalha Naval em Python

Este é um jogo de Batalha Naval implementado em Python. O objetivo do jogo é afundar todos os navios do computador antes que ele afunde os seus.

## Como Jogar

1.  **Início do Jogo:**
    *   Ao iniciar o jogo, o tabuleiro será exibido no console.
    *   O tabuleiro mostra o estado atual do jogo:
        *   `~`: Água (célula não atingida)
        *   `*`: Tiro na água
        *   `X`: Navio atingido

2.  **Dando um Tiro:**
    *   O jogo solicitará que você insira as coordenadas (linha e coluna) do seu tiro.
    *   As coordenadas devem ser números inteiros dentro dos limites do tabuleiro (0 a 4, neste caso).
    *   Se você inserir coordenadas inválidas (fora dos limites ou não numéricas), o jogo solicitará que você tente novamente.

3.  **Resultado do Tiro:**
    *   Após dar um tiro, o jogo informará se você acertou um navio ou atingiu a água.
    *   O tabuleiro será atualizado para refletir o resultado do tiro.

4.  **Dicas:**
    *   A cada 3 tentativas, o jogo fornecerá uma dica, mostrando as coordenadas do seu último tiro.

5.  **Fim do Jogo:**
    *   O jogo continua até que você acerte todos os navios.
    *   Ao final, o jogo exibirá uma mensagem de parabéns e mostrará o número de tentativas que você precisou para afundar todos os navios.

## Como Rodar a Aplicação

### Pré-requisitos

*   **Python:** Certifique-se de ter o Python instalado em seu sistema. Você pode baixar o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/).  Recomenda-se usar Python 3.6 ou superior.

### Passos para Executar

1.  **Baixe o Código:**
    *   Baixe o arquivo `batalha_naval.py` contendo o código do jogo.

2.  **Abra o Terminal ou Prompt de Comando:**
    *   Abra o terminal (Linux/macOS) ou o prompt de comando (Windows).

3.  **Navegue até o Diretório:**
    *   Use o comando `cd` para navegar até o diretório onde você salvou o arquivo `batalha_naval.py`.  Por exemplo:

        ```bash
        cd /caminho/para/o/seu/diretorio
        ```

4.  **Execute o Jogo:**
    *   Execute o jogo usando o comando:

        ```bash
        python batalha_naval.py
        ```

5.  **Divirta-se!**
    *   O jogo será iniciado no seu terminal. Siga as instruções na tela para jogar.

## Controles

*   **Linha:** Insira o número da linha (0 a 4) e pressione Enter.
*   **Coluna:** Insira o número da coluna (0 a 4) e pressione Enter.

## Exemplo de Jogo

```
=== BATALHA NAVAL ===
Instruções:
~ = Água
* = Tiro na água
X = Navio atingido

Tabuleiro:
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 1
Digite a coluna (0-4) do tiro: 2

>>> ÁGUA! <<<

Dica: Continue tentando!

Tabuleiro:
~ ~ ~ ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 0
Digite a coluna (0-4) do tiro: 0

>>> VOCÊ ACERTOU! <<<

Dica: Continue tentando!

Tabuleiro:
X ~ ~ ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 2
Digite a coluna (0-4) do tiro: 2

>>> ÁGUA! <<<

Dica: Tiro na linha 2, coluna 2.

Tabuleiro:
X ~ ~ ~ ~
~ ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 0
Digite a coluna (0-4) do tiro: 1

>>> ÁGUA! <<<

Dica: Continue tentando!

Tabuleiro:
X * ~ ~ ~
~ ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 0
Digite a coluna (0-4) do tiro: 2

>>> ÁGUA! <<<

Dica: Continue tentando!

Tabuleiro:
X * * ~ ~
~ ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 0
Digite a coluna (0-4) do tiro: 3

>>> ÁGUA! <<<

Dica: Tiro na linha 0, coluna 3.

Tabuleiro:
X * * * ~
~ ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 0
Digite a coluna (0-4) do tiro: 4

>>> ÁGUA! <<<

Dica: Continue tentando!

Tabuleiro:
X * * * *
~ ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 1
Digite a coluna (0-4) do tiro: 0

>>> ÁGUA! <<<

Dica: Continue tentando!

Tabuleiro:
X * * * *
* ~ * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
Digite a linha (0-4) do tiro: 1
Digite a coluna (0-4) do tiro: 1

>>> VOCÊ ACERTOU! <<<

Dica: Tiro na linha 1, coluna 1.

Tabuleiro:
X * * * *
* X * ~ ~
~ ~ * ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~ ~
... (Continua até acertar todos os navios)
```

## Notas

*   Este jogo é uma versão simplificada da Batalha Naval.
*   O posicionamento dos navios é aleatório.
*   A dica fornecida é básica e pode não ser muito útil.

Divirta-se jogando Batalha Naval!
```
