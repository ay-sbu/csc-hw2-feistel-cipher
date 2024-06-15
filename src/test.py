from random import randint

import srfbc
import commons as commons
import helper

def test_encrypt_decrypt_eval(plaintext: list[int], key: list[int]):
    print('plaintext:', plaintext)
    print('key:', key)
    
    encrypted = srfbc.block_encrypt(plaintext, key)
    decrypted = srfbc.block_decrypt(encrypted, key)

    print('encrypted:', encrypted)
    print('decrypted:', decrypted)
    print('result:', decrypted == plaintext)
    print()

def test_by_random():
    plaintext = helper.get_random_listbin(commons.block_len)
    key = helper.get_random_listbin(commons.key_len)

    test_encrypt_decrypt_eval(plaintext, key)

def test_by_input():
    p = input('plaintext: ')
    k = input('key: ')

    plaintext = helper.str_to_listbin(p, commons.block_len)
    key = helper.str_to_listbin(k, commons.key_len)

    test_encrypt_decrypt_eval(plaintext, key)


if __name__ == "__main__":
    # test_by_random()
    test_by_input()
    