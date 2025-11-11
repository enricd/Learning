# Default rule to build the target
all: random_c

# Link object files to create the executable
random_c: random_c.c 
	gcc -o random_c random_c.c random.c -lm

# Clean up build files
clean:
	rm -f random_c