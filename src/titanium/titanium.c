#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 gcc -fno-stack-protector -o titanium titanium.c
*/

int main(int argc, char *argv[]) {
  char* flag = getenv("FLAG");
  char* secret = getenv("SECRET_KEY");
  struct ab { 
  	char b[8];
    char a[32];   
  } s;
  if(argc < 2) {
    return 1;
  }
  strcpy(s.a, secret);
  sscanf(argv[1], "%s", s.b);
  if(strcmp(s.a, secret) != 0) {
    printf("%s", flag);
  } else {
    printf("%s", s.b);
  }
  return 0;
}