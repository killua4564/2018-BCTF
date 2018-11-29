from pwn import *

conn = remote("39.96.8.114", "9999")

num = 1329227995784915872903807060280345027

for _ in range(10):
	conn.recvuntil("Please input your number to guess the coeff: ")

	conn.sendline(str(num))

	conn.recvuntil("This is the sum: ")

	data = int(conn.recvuntil("\n").strip("\n"))

	coe_list = []

	while data > 1:
		coe_list.append(data % num)
		data = data // num

	conn.recvuntil("It is your time to guess the coeff!")

	conn.sendline(' '.join(list(map(str, coe_list[::-1]))))

conn.interactive()