# Exercícios Resolvidos - Criptografia de Chave Pública e RSA

---

## 1. Quais são os principais elementos de um criptossistema de chave pública?

**Resposta:**
- **Algoritmo de geração de chaves:** produz um par de chaves: pública e privada.
- **Algoritmo de encriptação:** usa a chave pública para cifrar mensagens.
- **Algoritmo de decriptação:** usa a chave privada para decifrar mensagens.

---

## 2. Quais são os papéis da chave pública e da privada? Descreva-os com exemplos.

**Resposta:**
- **Chave pública:** usada por qualquer pessoa para cifrar uma mensagem. Ex: Alice usa a chave pública de Bob para enviar uma mensagem cifrada.
- **Chave privada:** usada pelo dono (Bob) para decifrar a mensagem recebida. A segurança depende de manter a chave privada secreta.

---

## 3. Quais requisitos os criptossistemas de chave pública precisam cumprir?

**Resposta:**
- Facilidade de geração de chaves.
- Facilidade de cifragem/decifragem.
- Dificuldade computacional de deduzir a chave privada a partir da chave pública.
- Dificuldade de quebrar a cifragem sem a chave apropriada.

---

## 4. Descreva um procedimento eficiente para se escolher um número primo.

**Resposta:**
- Gerar um número aleatório grande.
- Usar testes de primalidade probabilísticos, como Miller-Rabin.
- Confirmar a primalidade com múltiplas iterações para reduzir a probabilidade de erro.

---

## 5. Esquema teórico com M1, M2, M3

### (a) Descreva o uso do conjunto de tabelas

**Resposta:**
- M1 transforma `k` em `x = f1(k)`
- M2 transforma `(x, p)` em `z = f2(x, p)`
- M3 transforma `(z, k)` em `p = f3(z, k)`
- Para encriptar: use M1 e M2.
- Para decriptar: use M3.

### (b) Demonstre que esse é um esquema seguro

**Resposta:**
- A composição das funções garante que somente quem conhece M1, M2 e M3 pode reverter a operação.
- Como M1 e M2 são permutações aleatórias, o sistema não revela padrões facilmente.
- O uso de três tabelas impede inversão direta sem o conhecimento completo das funções.

---

## 6. RSA - Encriptação e Decriptação

### (a) p = 3, q = 11, e = 7, M = 5
- n = 33, φ = 20
- d = 3
- C = 5^7 mod 33 = 14
- M = 14^3 mod 33 = 5 ✅

### (b) p = 5, q = 11, e = 3, M = 9
- n = 55, φ = 40
- d = 27
- C = 9^3 mod 55 = 14
- M = 14^27 mod 55 = 9 ✅

### (c) p = 7, q = 11, e = 17, M = 8
- n = 77, φ = 60
- d = 53
- C = 8^17 mod 77 = 71
- M = 71^53 mod 77 = 8 ✅

### (d) p = 11, q = 13, e = 11, M = 7
- n = 143, φ = 120
- d = 11 (auto-inverso)
- C = 7^11 mod 143 = 137
- M = 137^11 mod 143 = 7 ✅

### (e) p = 17, q = 31, e = 7, M = 2
- n = 527, φ = 480
- d = 343
- C = 2^7 mod 527 = 128
- M = 128^343 mod 527 = 2 ✅

---

## 7. Decriptar C = 10 com chave pública (e = 5, n = 35)

**Resposta:**
- φ = (5-1)*(7-1) = 24
- d = 29 (inverso de 5 mod 24)
- M = 10^29 mod 35 = 10 ✅
(Como 10 e 35 são coprimos, a mensagem não se alterou pela exponenciação modular)

---
