# Definição das tabelas S-Box e inversa do S-Box usadas no S-AES
SBOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}

SBOX_INV = {v: k for k, v in SBOX.items()}  # Inversa da S-Box

# Função para aplicar a substituição de Nibbles
def sub_nib(nibble):
    return (SBOX[nibble >> 4] << 4) | SBOX[nibble & 0xF]

# Função de expansão de chave no S-AES
def key_expansion(key):
    # Separando os 8 bits superiores e inferiores
    w0 = key >> 8
    w1 = key & 0xFF

    # Aplicando substituição e XOR com a constante Rcon1
    w2 = w0 ^ 0b10000000 ^ sub_nib(w1)
    w3 = w2 ^ w1

    # Aplicando substituição e XOR com a constante Rcon2
    w4 = w2 ^ 0b00110000 ^ sub_nib(w3)
    w5 = w4 ^ w3

    return [w0, w1, w2, w3, w4, w5]

# Função para aplicar a operação AddRoundKey
def add_round_key(state, key):
    return state ^ key

# Função para a operação ShiftRows no S-AES
def shift_rows(state):
    # Como temos apenas uma matriz 2x2, o ShiftRows troca os nibbles da segunda coluna
    return ((state & 0xF0F0) | ((state & 0x000F) << 4) | ((state & 0x00F0) >> 4))

# Função MixColumns do S-AES
def mix_columns(state):
    # Separando os nibbles
    s0 = (state >> 12) & 0xF
    s1 = (state >> 8) & 0xF
    s2 = (state >> 4) & 0xF
    s3 = state & 0xF

    # Aplicando a multiplicação no campo GF(2^4)
    s0_new = s0 ^ (s1 << 1) ^ (0x3 * s1 if s1 >= 0x8 else 0)
    s1_new = (s0 << 1) ^ (0x3 * s0 if s0 >= 0x8 else 0) ^ s1
    s2_new = s2 ^ (s3 << 1) ^ (0x3 * s3 if s3 >= 0x8 else 0)
    s3_new = (s2 << 1) ^ (0x3 * s2 if s2 >= 0x8 else 0) ^ s3

    return (s0_new << 12) | (s1_new << 8) | (s2_new << 4) | s3_new

# Entrada inicial
plaintext = 0b0110111101101011  # "ok" em ASCII
key = 0b1010011100111011  # Chave de entrada

# Expansão de chave
keys = key_expansion(key)

# Rodada inicial: AddRoundKey com K0
state = add_round_key(plaintext, (keys[0] << 8) | keys[1])

# Substituição de Nibbles (SubNib)
state = (sub_nib(state >> 8) << 8) | sub_nib(state & 0xFF)

# ShiftRows
state = shift_rows(state)

# MixColumns
state = mix_columns(state)

# AddRoundKey com K1
state = add_round_key(state, (keys[2] << 8) | keys[3])

# Segunda rodada: SubNib
state = (sub_nib(state >> 8) << 8) | sub_nib(state & 0xFF)

# ShiftRows
state = shift_rows(state)

# AddRoundKey com K2
ciphertext = add_round_key(state, (keys[4] << 8) | keys[5])

# Resultado final
bin(ciphertext)