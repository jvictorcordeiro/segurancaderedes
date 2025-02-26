# Atividade 7 - Geração de número pseudoaleatório e cifras de fluxo  - Respostas

## 1. Responda, objetivamente, as letras:

### a) Qual é a diferença entre aleatoriedades estatísticas e imprevisibilidade?
#### Resposta:

Aleatoriedades Estatísticas: A sequência gerada possui distribuição uniforme e independência entre os bits, simulando uma verdadeira aleatoriedade em testes estatísticos.

Imprevisibilidade: Mesmo conhecendo parte da sequência, não é possível prever o próximo bit ou conjunto de bits.

### b) Liste considerações de projeto importantes para uma cifra de fluxo.

#### Resposta:

Geração de Chave Aleatória: Utilizar um método robusto para produzir chaves únicas e imprevisíveis.

Não Linearidade: Incorporar operações não lineares para aumentar a resistência contra ataques.

Período Longo: Garantir um período extenso para evitar repetições na sequência cifrada.

Distribuição Uniforme: Assegurar que os bits cifrados sejam distribuídos uniformemente.

Resistência a Ataques Conhecidos-Plaintext: Proteger o sistema mesmo quando parte do texto simples é conhecida.

###  c) Por que não é desejável reutilizar uma chave de cifra de fluxo?

#### Resposta:

Vulnerabilidade a Ataques de XOR: A reutilização permite cancelar bits correspondentes, facilitando a recuperação de informações.

Quebra do Segredo da Chave: Conhecer partes da sequência cifrada pode expor a chave.

Perda de Unicidade da Sequência Cifrada: A repetição da chave gera padrões previsíveis, comprometendo a segurança.

### d) Que operações primitivas são usadas no RC4?

#### Resposta:

Inicialização do Vetor de Estado: Criar um vetor (geralmente de 0 a 255).

Permutação do Vetor de Estado (Swap): Misturar o vetor com base na chave fornecida.
Geração de Pseudo-Random Bytes: Produzir uma sequência de bytes a partir do vetor permutado.

Operação de XOR (OU Exclusivo): Aplicar XOR entre os bytes gerados e os bytes do texto simples para cifragem.

# Pergunta

## 3. Se apanharmos um algoritmo de congruência linear com um componente aditivo de 0:
$$
X_{n+1} = (aX_n) \mod n
$$
## então, podemos mostrar que, se \(m\) é primo, e se determinado valor de \(a\) produz o período máximo de \(m - 1\), então \(a^k\) também produzirá o período máximo, desde que \(k\) seja menor que \(m\) e que \(m-1\) não seja divisível por \(k\). Demonstre isso usando \(X_0 = 1\) e \(m = 31\), produzindo as sequências para: - \(ak = 3, 3^2, 3^3 e 3^4\)


### Resposta
```py
m = 31  # Número primo dado
X0 = 1  # Valor inicial

# Função para gerar a sequência do algoritmo de congruência linear
def gerar_sequencia(a, m, X0):
    sequencia = [X0]
    Xn = X0
    for _ in range(m - 2):  # O período máximo é m-1
        Xn = (a * Xn) % m
        sequencia.append(Xn)
    return sequencia

# Valores de a^k
valores_a = [3, 3^2, 3^3, 3^4]

# Gerando e imprimindo as sequências
sequencias = {a: gerar_sequencia(a, m, X0) for a in valores_a}
for a, seq in sequencias.items():
    print(f"Sequência para a = {a}:")
    print(seq, "\n")

```




## 4.
### a) Qual é o período máximo que pode ser obtido do seguinte gerador? $$ X_{n+1} = (aX_n) \; mod \; 2^4 $$

### b) Qual deverá ser o valor de a?

### c) Que restrições são exigidas na semente?

#### a) Resposta:

O tempo máximo necessário depende de $a$ e de $X_0$. Para $m = 16$, o período máximo ocorre quando $a$ e $X_0$ são escolhidos de forma que $a - 1$ seja divisível por todos os fatores primos de $m$ e $a - 1$ seja múltiplo de 4 se $m$ também o for. Por exemplo, com $a = 5$ e $X0 = 3$, o período máximo é 16, repetindo-se a sequência após 16 termos.

#### b) Resposta:

Para garantir que $a$ atenda aos critérios mencionados na letra anterior, teremos o seguinte:

Para $m = 16$, os fatores primos são 2 e 4, e $m$ é múltiplo de 4.

Uma escolha comum para "a" é 5. Verificando:

- $X_0 = 1$ e $a = 5$ são primos entre si.
- $5 - 1 = 4$ é divisível por 2 e 4.
- $5 - 1 = 4$ é um múltiplo de 4.

Assim, $a = 5$ é uma escolha adequada para alcançar o período máximo no gerador linear congruente especificado.


#### c) Resposta:

- Coprimalidade com $m$: A semente $X_0$ deve ser coprima com o módulo $m$, ou seja, não deve ter fatores primos em comum com $m$, exceto 1. Por exemplo, se $m = 16$, então $X_0$ não deve ser divisível por 2.

- Não pode ser zero: $X_0$ não pode ser zero, a menos que o multiplicador $a$ seja escolhido de uma forma específica. Se $X_0$ for zero e $a$ for um múltiplo de 2, o gerador entrará em um ciclo curto.

- Escolha que não gera um ciclo curto: A semente $X_0$ deve ser escolhida de modo a não gerar um ciclo curto, o que pode ocorrer se $X_0$ for zero ou um múltiplo de $m$.

## 5.
```py
# Implementação do Blum Blum Shub em SageMath
p = 499
q = 503
n = p * q
s = 17  # Deve ser coprimo com n

# Cálculo de x0
x0 = (s^2) % n
sequence = [x0]

# Gerar 10 números aleatórios
for _ in range(9):
    sequence.append((sequence[-1]^2) % n)

print("Sequência gerada pelo Blum Blum Shub:", sequence)
```