Sbox = [0x9, 0x4, 0xA, 0xB,
        0xD, 0x1, 0x8, 0x5,
        0x6, 0x2, 0x0, 0x3,
        0xC, 0xE, 0xF, 0x7]

InvSbox = [0xA, 0x5, 0x9, 0xB,
           0x1, 0x7, 0x8, 0xF,
           0x6, 0x0, 0x2, 0x3,
           0xC, 0x4, 0xD, 0xE]

def gf_mult(a, b):
    result = 0
    for i in range(4):  # realiza 4 iterações
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x10:  # se o termo exceder 4 bits, reduz modulo 0x13
            a ^= 0x13
        b >>= 1
    return result & 0xF


def int_to_state(word):
    p0 = (word >> 12) & 0xF
    p1 = (word >> 8)  & 0xF
    p2 = (word >> 4)  & 0xF
    p3 = word         & 0xF
    return [[p0, p2],
            [p1, p3]]

def state_to_int(state):
    p0 = state[0][0]
    p1 = state[1][0]
    p2 = state[0][1]
    p3 = state[1][1]
    return (p0 << 12) | (p1 << 8) | (p2 << 4) | p3

def add_round_key(state, round_key):
    word = state_to_int(state)
    word ^= round_key
    return int_to_state(word)

def sub_nib(state):
    new_state = []
    for row in state:
        new_row = []
        for nib in row:
            new_row.append(Sbox[nib])
        new_state.append(new_row)
    return new_state

def inv_sub_nib(state):
    new_state = []
    for row in state:
        new_row = []
        for nib in row:
            new_row.append(InvSbox[nib])
        new_state.append(new_row)
    return new_state

def shift_row(state):

    new_state = [state[0][:], state[1][:]]
    new_state[1][0], new_state[1][1] = new_state[1][1], new_state[1][0]
    return new_state

inv_shift_row = shift_row

def mix_columns(state):
    new_state = [[], []]

    for j in range(2):
        a = state[0][j]
        b = state[1][j]
        new_top = (a) ^ (gf_mult(4, b))
        new_bot = (gf_mult(4, a)) ^ (b)
        new_state[0].append(new_top)
        new_state[1].append(new_bot)
    return new_state

def inv_mix_columns(state):

    new_state = [[], []]
    for j in range(2):
        a = state[0][j]
        b = state[1][j]
        new_top = gf_mult(9, a) ^ gf_mult(2, b)
        new_bot = gf_mult(2, a) ^ gf_mult(9, b)
        new_state[0].append(new_top)
        new_state[1].append(new_bot)
    return new_state

def g(word):

    rotated = ((word & 0xF) << 4) | ((word >> 4) & 0xF)
    return ((Sbox[rotated >> 4]) << 4) | Sbox[rotated & 0xF]

def key_expansion(key):

    w0 = (key >> 8) & 0xFF
    w1 = key & 0xFF
    Rcon1 = 0x80
    Rcon2 = 0x30
    w2 = w0 ^ g(w1) ^ Rcon1
    w3 = w2 ^ w1
    w4 = w2 ^ g(w3) ^ Rcon2
    w5 = w4 ^ w3
    K0 = (w0 << 8) | w1
    K1 = (w2 << 8) | w3
    K2 = (w4 << 8) | w5
    return K0, K1, K2

def encrypt(plaintext, key):

    K0, K1, K2 = key_expansion(key)
    # etapa 0: estado inicial
    state = int_to_state(plaintext)
    # etapa inicial: AddRoundKey com K0
    state = add_round_key(state, K0)
    # Ronda 1:
    state = sub_nib(state)
    state = shift_row(state)
    state = mix_columns(state)
    state = add_round_key(state, K1)
    # Ronda 2 (final):
    state = sub_nib(state)
    state = shift_row(state)
    state = add_round_key(state, K2)
    return state_to_int(state)

def decrypt(ciphertext, key):
    K0, K1, K2 = key_expansion(key)
    # Inverte a última ronda:
    state = int_to_state(ciphertext)
    state = add_round_key(state, K2)
    state = inv_shift_row(state)
    state = inv_sub_nib(state)
    # Ronda 1 inversa:
    state = add_round_key(state, K1)
    state = inv_mix_columns(state)
    state = inv_shift_row(state)
    state = inv_sub_nib(state)
    # Ronda inicial:
    state = add_round_key(state, K0)
    return state_to_int(state)



if __name__ == '__main__':
    plaintext  = int("0110111101101011", 2)
    key        = int("1010011100111011", 2)
    expected   = int("0000011100111000", 2)
    
    ct = encrypt(plaintext, key)
    pt = decrypt(ct, key)
    
    print("Texto claro:     0x{:04X}".format(plaintext))
    print("Chave:           0x{:04X}".format(key))
    print("Texto cifrado:   0x{:04X}".format(ct))
    print("Texto cifrado (esperado): 0x{:04X}".format(expected))
    print("Decriptação:     0x{:04X}".format(pt))
    
    if ct == expected:
        print("\nTeste de encriptação OK!")
    else:
        print("\nProblema na encriptação!")