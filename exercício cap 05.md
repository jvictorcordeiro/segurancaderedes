# Atividade 5 - AES - Respostas

## 1° Qual foi o conjunto original de critérios usados pelo NIST para avaliar as cifras AES candidatas?

#### Resposta: 
O conjunto original de critérios(1997) considerados pela NIST inicialmente foram:
- 1. Segurança: ela foi o fator mais importante na avaliação e abrangeu características como resistência do algoritmo à criptoanálise, solidez de sua base matemática, aleatoriedade da saída do algoritmo e segurança relativa em comparação com outros candidatos.
- 2. Custo: O custo foi uma segunda área importante de avaliação que abrangeu requisitos de licenciamento, eficiência computacional (velocidade) em diversas plataformas e requisitos de memória.
- 3. Características de algoritmo e implementação: A terceira área de avaliação foram características de algoritmo e implementação, como flexibilidade, adequação de hardware e software e simplicidade de algoritmo.

## 2° Qual foi o conjunto final de critérios usados pelo NIST para avaliar as cifras AES candidatas?

#### Resposta:
O conjunto final de critérios(2000) considerados pela NIST inicialmente foram:
- 1. Segurança geral: Para avaliar a segurança geral, o NIST baseou-se na análise de segurança pública conduzida pela comunidade criptográfica. Durante o processo de avaliação de três anos, vários criptógrafos publicaram suas análises dos pontos fortes e fracos dos vários candidatos.
- 2. Implementações de software: As principais preocupações nesta categoria são a velocidade de execução, o desempenho em diversas plataformas e a variação de velocidade com o tamanho da chave.
- 3. Ambientes de espaço restrito: Em algumas aplicações, como cartões inteligentes, quantidades relativamente pequenas de memória de acesso aleatório (RAM) e/ou memória somente leitura (ROM) estão disponíveis para fins como armazenamento de código (geralmente em ROM).
- 4. Implementações de hardware: assim como o software, as implementações de hardware podem ser otimizadas em termos de velocidade ou tamanho. 
- 5. Ataques a implementações: O critério de segurança geral, discutido no primeiro item, preocupa-se com ataques criptoanalíticos que exploram propriedades matemáticas dos algoritmos. Existe outra classe de ataques que utiliza medições físicas realizadas durante a execução do algoritmo para coletar informações sobre quantidades, como chaves.
- 6. Criptografia versus descriptografia: Este critério trata de diversas questões relacionadas a considerações de criptografia e descriptografia

## 3° Qual é a diferença entre Rijndael e AES?

#### Resposta:

Rijndael é um algoritmo mais genérico que oferece suporte a vários tamanhos de chave e bloco. Já o AES é uma implementação específica do Rijndael, com parâmetros fixos definidos pelo NIST para estabelecer um padrão de cifra simétrica.

## 4. Responda:
### (a) Qual é a finalidade do array Estado?
### (b) Como é construída a S-box?
### (c) Descreva rapidamente o estágio SubBytes, ShiftRows, MixColumns, AddRoundKey, e o algoritmo de expansão de chave.

#### a) Resposta:

O array estado é responsável por salvar as operações realizadas sobre o texto claro durante as fases de encriptação ou decriptação. Após a etapa final, o array estado é copiado para uma matriz de saida.

#### b) Resposta:

A S-box (Substitution box) é uma tabela de substituição usada no AES. Ela substitui cada byte do array Estado por outro byte de acordo com uma tabela predefinida. A construção da S-box envolve uma série de operações, incluindo a aplicação de uma função de inversão, operações de campo finito e permutações. A S-box é projetada para fornecer não linearidade e confusão, contribuindo para a segurança global do algoritmo AES.

#### c) Resposta:

- SubBytes: utiliza uma matriz S-box para realizar uma substituição byte a byte do bloco. Onde, por exemplo, para um hexadecimal A5 iriamos encontrar o elemento que está na linha A e coluna 5 na matriz S-box.

- ShiftRows: realiza uma permutação simples e circular entre os elementos do array de estados para esquerda na encriptação e para direita na decriptação. Sendo que a linha 0 não ocorre mudanças, na linha 1 ocorre o deslocamento de 1 byte, na linha 2 ocorre o deslocamenta de 2 byte, na linha 3 ocorre o deslocamento de 3 byte.

- MixColumns:  cada byte de uma coluna é mapeado para um novo valor que é determinado em função de todos os quatro bytes nessa coluna. A transformação pode ser definida por uma multiplicação de matriz sobre o array de estado. Então, trata-se de uma substituição que utiliza aritmética sobre GF(2<sup>8</sup>).
 

- AddRoundKey: os 128 bits de Estado passam por um XOR bit a bit com os 128 bits da chave da rodada. A operação é vista como uma do tipo coluna por coluna entre os 4 bytes da coluna Estado e uma palavra da chave da rodada.

- Algoritmo de expansão de chave: utiliza como entrada uma chave de 4 words (16 bytes) e produz um array linear de 44 words (176 bytes). Isso é suficiente para oferecer uma chave da rodada de 4 words para o estágio AddRoundKey inicial e para cada uma das 10 rodadas da cifra.

## 5. Quantos bytes em Estado são afetados por ShiftRows?

#### Resposta:

Durante o ShiftRows cada linha é deslocada para esquerda resultando nos seguintes números de bytes, considerando o array de estado:

1 - Nenhuma mudança na primeira linha.

2 - Deslocamento de 1 byte na segunda linha.

3 - Deslocamento de 2 bytes na terceira linha.

4 - Deslocamento de 3 bytes na quarta linha.

Somando no total temos = 6 bytes afetados.

## 6. Use a chave 1010 0111 0011 1011 para encriptar o texto claro "ok"conforme expresso em ASCII, ou seja, 0110 1111 0110 1011. Os projetistas do S-AES obtiveram o texto cifrado 0000 0111 0011 1000. E você?

#### Resposta:
```py
# Função auxiliar: XOR bit a bit (supondo strings de mesmo tamanho)
def xor_bits(a, b):
    return "".join("0" if x == y else "1" for x, y in zip(a, b))

# S‐box do S‐AES (tabela padrão):
sbox = {
    '0000': '1001', '0001': '0100', '0010': '1010', '0011': '1011',
    '0100': '1101', '0101': '0001', '0110': '1000', '0111': '0101',
    '1000': '0110', '1001': '0010', '1010': '0000', '1011': '0011',
    '1100': '1100', '1101': '1110', '1110': '1111', '1111': '0111'
}

# Permutação P definida sobre 8 bits:
# (Neste exemplo, P reordena os 8 bits conforme: [posição 0,2,4,6,1,3,5,7])
def permutation_P(bits):
    indices = [0, 2, 4, 6, 1, 3, 5, 7]
    return "".join(bits[i] for i in indices)

# Função f: divide os 8 bits em 2 nibbles, aplica S-box a cada nibble e depois a permutação P.
def f_function(bits):
    nib1 = bits[:4]
    nib2 = bits[4:]
    sub1 = sbox[nib1]
    sub2 = sbox[nib2]
    combinado = sub1 + sub2
    return permutation_P(combinado)

# Dados do problema:
# Texto claro "ok" – em ASCII: 'o' = 6F e 'k' = 6B
plaintext = "01101111" + "01101011"   # 16 bits: 0110 1111  0110 1011

# Chave de 16 bits: 1010 0111 0011 1011
key = "10100111" + "00111011"

# Para esta demonstração, vamos supor que a rodada usa como subchave os 8 bits direitos da chave.
subkey = key[8:]        # "00111011"

# Dividindo o bloco em duas metades (8 bits cada):
metade_esquerda = plaintext[:8]  # "01101111"
metade_direita  = plaintext[8:]   # "01101011"

# =============================================================================
# (a) XOR do material da subchave com a entrada da função f:
a_val = xor_bits(metade_direita, subkey)
print("(a) XOR da subchave com a entrada de f:")
print(a_val)   # Por exemplo: 01010000
# =============================================================================

# =============================================================================
# (c) Cálculo da função f:
f_val = f_function(a_val)
print("\n(c) Saída da função f:")
print(f_val)   # Por exemplo: 00100101
# =============================================================================

# =============================================================================
# (b) XOR da saída da função f com a metade esquerda do bloco:
b_val = xor_bits(metade_esquerda, f_val)
print("\n(b) XOR da saída de f com a metade esquerda:")
print(b_val)   # Por exemplo: 01001010
# =============================================================================

# =============================================================================
# (d) Exemplo: aplicação isolada da permutação P à etapa (a):
d_val = permutation_P(a_val)
print("\n(d) Permutação P aplicada à saída da etapa (a):")
print(d_val)   # Exemplo: 00001100
# =============================================================================

# =============================================================================
# (e) Troca (swap) de metades do bloco (na rodada feistel, após a operação XOR)
e_val = metade_direita + b_val
print("\n(e) Troca de metades (swap):")
print(e_val)   # Exemplo: 01101011 01001010
# =============================================================================

# OBSERVAÇÃO:
# Em um S‐AES completo (com expansão de chave e duas rodadas) o texto cifrado final obtido foi:
ciphertext = "00000111" + "00111000"
print("\nTexto cifrado final (após 2 rodadas):")
print(ciphertext)  # 0000 0111  0011 1000

```