all: testme
CFLAGS=-g 

testme: testme.c main.c
	$(CC) -o $@ $(CFLAGS) $^

clean:
	rm -f testme
