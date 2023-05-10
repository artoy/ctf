LOWER_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def decrypt(encrypted, key):
    result = ""
    for i in range(len(encrypted)):
        if encrypted[i] not in LOWER_ALPHABET:
            result += encrypted[i]
        else:
            result += LOWER_ALPHABET[(LOWER_ALPHABET.index(encrypted[i]) - LOWER_ALPHABET.index(key[i])) % 26]

    return result

key = "thequickbrownfoxjumpsoverthelazydog"
encrypted = "RpgSyk{qsvop_dcr_wmc_rj_rgfxsime!}"

print(decrypt(encrypted, key))