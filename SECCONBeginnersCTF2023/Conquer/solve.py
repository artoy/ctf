from Crypto.Util.number import *

for l in range (1, 440):
    key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
    cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379
    length = l

    def ROL(bits, N):
        for _ in range(N):
            bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
        return bits

    for i in range(32):
        cipher ^= key
        key = ROL(key, length - pow(cipher, 3, length))

    m = cipher ^ key

    try:
        flag = long_to_bytes(m).decode(errors='ignore')
        if flag.startswith('ctf'):
            print(flag)
    except Exception:
        continue
