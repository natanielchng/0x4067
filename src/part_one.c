#include <stdio.h>
#include <string.h>

/*
gcc -fno-stack-protector -o part_one part_one.c
*/

#define FLAG "You got the flag!"
#define SECRET "a4f53d"
#define BUFFER_SIZE 8

int main(int argc, char *argv[]) {
  struct ab { 
  	char b[BUFFER_SIZE];
    char a[BUFFER_SIZE];   
  } s;
  if(argc < 2) {
    return 1;
  }
  strcpy(s.a, SECRET);
  sscanf(argv[1], "%s", s.b);
  if(strcmp(s.a, SECRET) != 0) {
    printf("%s", FLAG);
  } else {
    return 1;
  }
  return 0;
}
