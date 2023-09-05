all: myapp

myapp: driver.o mylib.o
	gcc -Wall -o myapp driver.o mylib.o

driver.o: driver.c
	gcc -c -Wall driver.c

mylib.o: mylib.c
	gcc -c -Wall mylib.c

clean:
	rm driver.o
	rm mylib.o