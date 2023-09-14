#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>

/*
gcc -z execstack -fno-stack-protector -no-pie -o hexhunt hexhunt.c 
*/

void returnToTarget() {
    char buffer1[16];
    gets(buffer1);
 }

void returnAFlag() {
    printf("\n\n");
    printf("Seems like something else was returned instead... ");
    puts("0x4067{h3xhun7_r37urn_70_fl46}");
    printf("\n\n");
} 

int main(int argc, char *argv[]) {
  
  char* flag = "0x4067{h3xhun7_7h3_f0rm47_57r1n6}";
  char buf[100];
  char* flag2 = "0x4067{h3xhun7_74r637_0v3rfl0w3d}";
  
  struct ab { 
  	char b[1024];
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
    printf("    -d : DDOS TARGET\n");
    printf("    -r : Return data to TARGET");
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
  
  else if(strcmp(argv[1], "-d") == 0) {
    int maxPackets = 16;
    int numPackets;
    char inputBuffer[100];
    char* tierMessage = "Please subscribe to Premium tier for higher payload quota!";
    printf("\n\n");
    printf("Entering DDOS Session");
    printf("\n\n");
    
    while(1) {
        printf("You have %d payloads left. %s", maxPackets, tierMessage);
        printf("\n\n");
        
        printf("Please enter the number of payloads to send: ");
        fgets(inputBuffer, sizeof(inputBuffer), stdin);
        if (sscanf(inputBuffer, "%d", &numPackets) == 1) {
            printf("Sent %d packets!", numPackets);
            maxPackets = maxPackets - numPackets;
        } else {
            printf("Please enter a valid number.");
        }
        
        if(maxPackets > 16) {
            tierMessage = "Your Premium tier account is: 0x4067{h3xhun7_1n7363r_wr4p_4r0und}";
        }
        
        printf("\n\n");
    } 
  }
  
  else if(strcmp(argv[1], "-r") == 0) {
    printf("\n\n");
    printf("Enter data (in bytes) to return to the target: ");
    returnToTarget();
    printf("\nData has been returned!");
    printf("\n\n");
  }
  
  else {
    useMessage();
  }
  
  
  return 0;
}