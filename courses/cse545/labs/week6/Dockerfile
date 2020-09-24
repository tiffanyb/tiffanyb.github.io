from ubuntu:20.04

copy ./stack /tmp/stack
copy ./stack.c /tmp/stack.c
run apt-get update
run apt-get install -y socat vim gdb gcc
copy ./entry.sh /tmp/entry.sh

run chmod 755 /tmp/stack
run chmod 755 /tmp/entry.sh
run mkdir /tmp/records && chmod -R 777 /tmp/records

user nobody
# cmd ["socat", "tcp4-listen:2000,reuseaddr,fork", "exec:./service"]
cmd "/tmp/entry.sh"
