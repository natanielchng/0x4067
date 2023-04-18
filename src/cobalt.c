#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

/*
gcc -o cobalt cobalt.c -Wno-format-security -z noexecstack -no-pie
*/

int main(int argc, char *argv[]) {

  char* flag = getenv("FLAG");
  char buf[100];
  
    if(argc < 2) {
      return 1;
    }

    printf("%p ", &flag);
    strncpy(buf, argv[1], 100);
    printf(buf);
  
    return 0;
}