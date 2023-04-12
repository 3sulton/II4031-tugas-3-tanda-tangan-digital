from random import randrange, getrandbits
from math import gcd as bltin_gcd
import gmpy2

def is_prime(n):
    # big prime numbers are hard to find
    # use Miller-Rabin algorithm as famous probablistic algorithm
    # to check whether the number is prime or not
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    k = 128
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime():
    length = 1024
    while(True):
        # generate random number
        p = getrandbits(length)
        # apply a mask to set MSB and LSB to 1
        p |= (1 << length - 1) | 1
        if is_prime(p):
            return p

def is_coprime(a, b):
    return bltin_gcd(a, b) == 1

def rsa_sign(hash, n, key):
    pt = (hash**key) % n
    result = hex(pt)[2:]
    return result

#masukin hasil hash konten, trs di cek sm digital sign
def rsa_verify(ds, hash, n, key):
    ct = gmpy2.mpz(int(ds, 16))
    result = pow(ct, key, n)
    return result == hash

def signing(ds):
    return '''
    *** Begin of digital signature ***\n
    %s\n
    *** End of digital signature ***
    ''' % ds

class rsa:
    def __init__(self):
        pass

    def generate_e(self):
        length = 1024
        while(True):
            # generate random number
            e = getrandbits(length)
            # apply a mask to set MSB to 1
            e |= (1 << length - 1)
            if is_coprime(e, 1):
                return e

    def key_generator(self):
        p = generate_prime()
        q = generate_prime()
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self.generate_e()
        print(len(str(self.e)))
        print(self.e)


rsa = rsa()
rsa.key_generator()
