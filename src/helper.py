import commons
from random import randint
import copy
from primes import primes

def get_random_listbin(binlen):
    result = []
    for i in range(binlen):
        result.append(randint(0, 1))
    return result

def prime_swapper(fin: list[int]) -> None:
    '''
        - len(fin) = commons.fin_len
        - len(output) = commons.fin_len
    '''
    for i in range(len(fin)):
        fin[i], fin[primes[i % len(primes)] % len(fin)] = fin[primes[i % len(primes)] % len(fin)], fin[i]

def splitter(fin: list, sublen: int):
    l = []
    count = len(fin) // sublen
    for i in range(count):
        l.append(copy.copy(fin[i*sublen: (i+1)*sublen]))
    return l

def flatter(fin: list[list[int]]):
    l = []
    for i in range(len(fin)):
        for j in range(len(fin[i])):
            l.append(fin[i][j])
    return l

def is_prime(n: int):
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

def prime_list_generator(count: int):
    ps = []
    i = 2
    while len(ps) < count:
        if is_prime(i):
            ps.append(i)
        i += 1
    return ps

def ciphertext_packer(cs: list[list[int]]):
    result = []
    for i in range(len(cs)):
        for j in range(len(cs[i])):
            result.append(cs[i][j])
    return result
    
def listbin_cyshift(p: list[int], count: int, dir='left'):
    if dir == 'left':
        return p[count:] + p[:count]
    else:
        return p[:count] + p[count:]

def listbin_to_str(l: list[int]):
    return ''.join(map(str, l))

def listbin_to_int(l: list[int]):
    return int(listbin_to_str(l), 2)

def int_to_strbin(n: int, strlen: int):
    return bin(n)[2:].zfill(strlen)

def int_to_listbin(n: int, listlen: int):
    return list(map(int, list(int_to_strbin(n, listlen))))

def str_to_listbin(s: str, outlen: int):
    result = []
    for i in s:
        result += int_to_listbin(ord(i), 8)
    result += ([0] * (outlen - len(result)))
    return result

def mod_add(a: int, b: int):
    return (a + b) % commons.add_module

def mod_mul(a: int, b: int):
    return (a * b) % commons.mul_module

def listbin_add(a: list[int], b: list[int]):
    a_num = listbin_to_int(a)
    b_num = listbin_to_int(b)
    
    mul = mod_add(a_num, b_num)

    return int_to_listbin(mul, len(a))

def listbin_xor(a: list[int], b: list[int]):
    result = []
    for i in range(len(a)):
        result.append(a[i] ^ b[i])
    return result

def listbin_mul(a: list[int], b: list[int]):
    a_num = listbin_to_int(a)
    b_num = listbin_to_int(b)
    
    mul = mod_mul(a_num, b_num)

    return int_to_listbin(mul, len(a))