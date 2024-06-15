# srfbc: some random feistel-based cryptosystem

import copy
from random import randint

import helper
import commons as commons
from primes import primes
    

def block_encrypt(plaintext: list[int], key: list[int]) -> list[int]: 
    '''
        - len(plaintext) = commons.block_len
        - len(key) = commons.key_len
        - len(output) = commons.block_len
    '''
    subkeys = key_scheduler(key)
    result = plaintext
    for i in range(commons.round_count):
        result = round(result, subkeys[i])

    # last swap
    result = helper.listbin_cyshift(result, len(result) // 2)
    
    return result

def block_decrypt(ciphertext: list[int], key: list[int]) -> list[int]: 
    '''
        - len(plaintext) = commons.block_len
        - len(key) = commons.key_len
        - len(output) = commons.block_len
    '''
    subkeys = key_scheduler(key)
    rev_subkeys = subkeys[::-1]

    result = block_encrypt(ciphertext, helper.flatter(rev_subkeys))

    return result


def key_scheduler(key: list[int]) -> list[list[int]]:
    '''
        - len(key) = commons.key_len
        - len(output) = commons.round_count * (commons.block_len // 2)
    '''
    left_key = key
    right_key = copy.copy(key)
    helper.prime_swapper(right_key)

    subkeys = helper.splitter(left_key, len(key) // (commons.round_count//2))
    subkeys += helper.splitter(right_key, len(key) // (commons.round_count//2))

    return subkeys
    

def round(fin: list[int], subkey: list[int]) -> list[int]:
    '''
        - len(fin) = commons.block_len
        - len(subkey) = commons.block_len // 2
    '''
    left_half, right_half = helper.splitter(fin, len(fin)//2)
    right_result = f(right_half, subkey)
    right_result = helper.listbin_xor(right_result, left_half)

    return right_half + right_result

    
def f(fin: list[int], subkey: list[int]) -> list[int]:
    '''
        - len(fin) = commons.block_len // 2
        - len(subkey) = commons.block_len // 2
    '''
    working_fin = copy.copy(fin)
    for i in range(len(fin)):
        shift_and_xor(working_fin, subkey, primes[i % len(primes)])

    helper.prime_swapper(working_fin)

    return working_fin

def shift_and_xor(fin: list[int], subkey: list[int], prime: int) -> None:
    '''
        - len(fin) = commons.block_len // 2
        - len(subkey) = commons.block_len // 2
        - len(output) = commons.block_len // 2
    '''
    count = prime % len(fin)
    fin = helper.listbin_xor(fin, subkey)
    fin = helper.listbin_cyshift(fin, count)

    