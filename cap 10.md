# Exercícios - Criptossistemas de Chave Pública

---

## 1. Diffie-Hellman

**Dados:**
- Primo comum `q = 71`
- Raiz primitiva `alpha = 7`

### (a) Calcule a chave pública de A, com `XA = 5`

**Código:**
```python
q = 71
alpha = 7
XA = 5
YA = power_mod(alpha, XA, q)
YA
```

**Resposta:**
`YA = 7^5 mod 71 = 17`

---

### (b) Calcule a chave pública de B, com `XB = 12`

**Código:**
```python
XB = 12
YB = power_mod(alpha, XB, q)
YB
```

**Resposta:**
`YB = 7^12 mod 71 = 64`

---

### (c) Calcule a chave secreta compartilhada `K`

**Código:**
```python
K1 = power_mod(YB, XA, q)
K2 = power_mod(YA, XB, q)
K1 == K2  # deve ser True
K1
```

**Resposta:**
`K = 64^5 mod 71 = 63`  
(ou `K = 17^12 mod 71 = 63`)

---

## 2. ElGamal

**Dados:**
- Primo `q = 71`
- Raiz primitiva `alpha = 7`
- Chave pública de B: `YB = 3`
- Mensagem `M = 30`

### (a) Calcule o texto cifrado usando `k = 2`

**Código:**
```python
k = 2
M = 30
C1 = power_mod(alpha, k, q)
C2 = mod(M * power_mod(YB, k, q), q)
(C1, C2)
```

**Resposta:**
- `C1 = 7^2 mod 71 = 49`
- `C2 = 30 * 3^2 mod 71 = 47`  
**Texto cifrado:** `C = (49, 47)`

---

### (b) Sabendo que `C1 = 59`, encontre `C2`

**Código:**
```python
for k in range(1, q):
    if power_mod(alpha, k, q) == 59:
        break
C2 = mod(M * power_mod(YB, k, q), q)
C2
```

**Resposta:**
- Encontrado `k = 10`, pois `7^10 mod 71 = 59`
- `C2 = 30 * 3^10 mod 71 = 24`  
**Texto cifrado:** `C = (59, 24)`

---

## 3. Verificação de grupo em curvas elípticas

**Enunciado:**  
Verifique se as curvas elípticas da Figura 10.4 formam grupos sobre os números reais.

**Requisitos:**
- A curva está na forma reduzida de Weierstrass: `y^2 = x^3 + ax + b`
- O discriminante `Δ = 4a^3 + 27b^2 ≠ 0`
- A adição de pontos obedece às leis do grupo (associatividade, elemento neutro, inverso)

**Exemplo de verificação em SageMath (substituir a, b pelos valores da curva):**
```python
a = -5
b = 5
Delta = 4 * a^3 + 27 * b^2
Delta != 0  # True se for grupo
```

**Resposta:**
- `Δ = 4*(-5)^3 + 27*5^2 = -500 + 675 = 175 ≠ 0`  
Logo, a curva **define um grupo abeliano** sob adição de pontos.

---

## 4. Verificar se o ponto `(4, 7)` pertence à curva `y^2 = x^3 - 5x + 5`

**Código:**
```python
x = 4
y = 7
lhs = y^2
rhs = x^3 - 5*x + 5
lhs == rhs
```

**Resposta:**
- `lhs = 7^2 = 49`
- `rhs = 4^3 - 5*4 + 5 = 64 - 20 + 5 = 49`  
Como `lhs == rhs`, o ponto **(4, 7) pertence à curva**.

---
