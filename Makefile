CC     = gcc
CFLAGS = -Wall -O2 -I/usr/local/include
LIBS   = -L/usr/local/lib -lraylib -lGL -lm -lpthread -ldl -lX11

all: output

output: main.c
	$(CC) main.c -o output $(CFLAGS) $(LIBS)

run: output
	./output

clean:
	rm -f output

run: output
	./output