import gmpy
import sympy
from pwn import *
from functools import reduce

# NOPE

conn = remote("60.205.223.220", "9999")

p = 1461501637330902918203684832716283019655932542983
delta = 713623846352979940529142984724747568191373312

for _ in range(5):
	t = conn.recvuntil('\n').strip(']\n').strip('[').replace('L', "")
	t = list(map(int, t.split(', ')))

	u = conn.recvuntil('\n').strip(']\n').strip('[').replace('L', "")
	u = list(map(int, u.split(', ')))

	d = [int(sympy.invert(x, p)) for x in t]
	D = reduce(lambda x, y: x * y, d) % p
	U = reduce(lambda x, y: x * y, u) % p

	conn.recvuntil("Input your guess number: ")

	m = gmpy.root(U * D, 22)[0]

	conn.sendline(str(m))
conn.interactive()