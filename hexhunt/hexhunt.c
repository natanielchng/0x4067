#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

/*
gcc -z execstack -fno-stack-protector -o hexhunt hexhunt.c 
*/

int main(int argc, char *argv[]) {
  
  char* flag = "0x4067{h3xhun7_7h3_f0rm47_57r1n6}";
  char buf[100];
  char* flag2 = "0x4067{h3xhun7_74r637_0v3rfl0w3d}";
  
  struct ab { 
  	char b[8];
    char a[32];   
  } s;
  
  printf("  _    ____    _            ____ \n");
  printf(" | |_ |__ /_ _| |_ _  _ _ _|__  |\n");
  printf(" | ' \\ |_ \\ \\ / ' \\ || | ' \\ / / \n");
  printf(" |_||_|___/_\\_\\_||_\\_,_|_||_/_/\n");
  printf("  Hexhunt -- a not so dangerous application");
  
  void useMessage() {
    printf("\n\n");
    printf("Usage: ./hexhunt <OPTION> <TARGET>\n\n");
    printf("++ OPTIONs ++\n");
    printf("    -p : Reformat TARGET\n");
    printf("    -o : Overwhelm TARGET\n");
    printf("\n\n");
  }

  if(argc < 3) {
    useMessage();
    return 1;
  }
  
  if(strcmp(argv[1], "-p") == 0) {
      printf("\n\n");
      printf("Sending payload to ");
      strncpy(buf, argv[2], 100);
      printf(buf);
      printf("\n\n");
      printf("Target formatted!");
      printf("\n\n");
  }
  
  else if(strcmp(argv[1], "-o") == 0) {
    printf("\n\n");
    strcpy(s.a, "secret");
    sscanf(argv[2], "%s", s.b);
    printf("Sending payload to ");
    if(strcmp(s.a, "secret") != 0) {
        printf("%s", flag2);
    } else {
        printf("%s", s.b);
    }
    printf("\n\n");
    printf("Target overflowed!");
    printf("\n\n");
  }
  
  else {
    useMessage();
  }

  return 0;
}