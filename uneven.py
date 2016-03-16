from Crypto.Util import number
import json
import random

def mod_inverse(a, m):
    a, i = a % m, 1
    while a > 1:
        q, a = m / a, m % a
        i = (-i * q) % m
    if a == 1:
        return i

# via https://stackoverflow.com/questions/15978781/how-to-find-integer-nth-roots
def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s

if __name__ == "__main__":
    # Key generation (takes a while)
    # print "p", number.getPrime(n)
    # print "#"*80
    # print "q", number.getPrime(10*n)
    # print "e", 5
    # print "d", mod_inverse(e, (p-1)*(q-1))

    # size of p (and 1/10th the size of q)
    n = 1024  

    # read in our pregenerated key
    with open("key.json", "r") as fin:
        keyd = json.load(fin)
    p, q, e, d = keyd["p"], keyd["q"], keyd["e"], keyd["d"]

    # compute the public modulus
    N = p*q

    # generate a message
    m = random.randint(0, 2**(n-1))
    print "Message is:", m
    print "#"*80

    # compute the encryption of the message
    c = pow(m, e, N)

    # check that the message decrypts correctly
    if m == pow(c, d, N):
        print "Message decrypted correctly!"
        print "#"*80
    else:
        print "You generated your key incorrectly."
        print "#"*80

    # check that this cryptosystem is broken
    broken = iroot(e, c)
    if m == broken:
        print "Yup, this system is broken >.<"
        print "We just took the eth root."
        print "#"*80
