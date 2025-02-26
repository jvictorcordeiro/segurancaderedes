# Atividade 6 - Operação de Cifra de Bloco  - Respostas

## 1. O que é encriptação tripla?

### Resposta: 

A encriptação tripla (Triple DES ou 3DES) é um método de criptografia que aplica o algoritmo de encriptação DES (Data Encryption Standard) três vezes consecutivas em uma sequência de dados. O DES utiliza chaves de 56 bits, e a encriptação tripla aumenta a segurança ao aplicar o algoritmo três vezes com três chaves diferentes. O processo envolve geralmente a aplicação de uma encriptação, seguida por uma desencriptação e, finalmente, outra encriptação.

## 2. O que é ataque meet-in-the-middle?

### Resposta:

O ataque meet-in-the-middle é um tipo de ataque criptoanalítico que explora a fraqueza de certos esquemas de criptografia que utilizam duas operações de sentido único em etapas separadas. No contexto da encriptação dupla ou tripla, esse ataque é relevante. O atacante executa a encriptação e a desencriptação de forma independente em um grande conjunto de chaves possíveis e, em seguida, procura por uma correspondência no meio. Se a encriptação e a desencriptação coincidirem, o atacante identifica a chave correta.

## 3. Quantas chaves são usadas na encriptação tripla?

### Resposta:

Na encriptação tripla (3DES), são usadas três chaves diferentes. Cada chave é usada em uma etapa separada do processo de encriptação/desencriptação. Portanto, se cada chave é de 56 bits (como no DES padrão), a encriptação tripla resulta em uma chave efetiva de 168 bits (3 * 56 bits). Esse aumento no tamanho da chave em comparação com o DES padrão aumenta a resistência da encriptação contra ataques de força bruta e outras formas de criptoanálise.

## 4. Por que a parte do meio do 3DES é decriptação, em vez de encriptação?

### Resposta:

Os dados são encriptados com a primeira chave, decriptados com a segunda chave e finalmente encriptados novamente com uma terceira chave. Isto faz o 3DES ser mais lento que o DES original, porém em contrapartida oferece maior segurança.

## 5. Por que alguns modos de operação de cifra de bloco só utilizam a encriptação, enquanto outros empregam encriptação e decriptação?

### Resposta:

Alguns modos usam apenas a encriptação porque a principal função é proteger a confidencialidade dos dados. Outros modos, que envolvem tanto a encriptação quanto a decriptação, podem oferecer funcionalidades adicionais, como autenticação de integridade e autenticação de origem.

## 6. Você deseja construir um dispositivo de hardware para realizar encriptação de bloco no modo cipher block chaining (CBC) usando um algoritmo mais forte do que DES. 3DES é um bom candidato. A Figura 1 mostra duas possibilidades, ambas acompanhando a definição do CBC. Qual das duas você escolheria:

### a) Por segurança?

### b) Por desempenho?

#### a) Resposta:
Chaves Independentes: Se uma das opções permitir o uso de três chaves independentes (uma para cada etapa do 3DES), isso aumentaria a segurança em relação ao uso de uma única chave para todas as etapas.

#### b) Resposta:
Já para um maior desempenho, a primeira opção é preferível porque consiste em apenas um loop.