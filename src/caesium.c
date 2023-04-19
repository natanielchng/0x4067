#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdarg.h>
#include <unistd.h>
#include <time.h>

/*
gcc -o caesium caesium.c
*/

int main(int argc, char *argv[]) {

  clock_t start_time, end_time;
  double time_taken;
  int wrong_flag = 1;
  int show_time = 1;
  char* flag = getenv("FLAG");
  char* secret_key = getenv("SECRET_KEY");
  //char flag[] = "yass";
  //char secret_key[] = "CARR0T12";
  
  if(argc < 2) {
    return 1;
  }
  
  start_time = clock();

  for(int i = 0; i < strlen(argv[1]); i++) {
    if(argv[1][i] == secret_key[i]) {
      wrong_flag = 0;
      if(i == strlen(secret_key) - 1) {
        printf("%s\n", flag);
        show_time = 0;
      }
    }
    else {
     sleep(3); 
    }
    wrong_flag = 1;
  }

  end_time = clock();

  time_taken = ((double)(end_time - start_time)) / CLOCKS_PER_SEC; // Calculate the time taken in seconds

  if(show_time == 1){
    printf("Time taken: %f seconds\n", time_taken);
  }
  
  return 0;
}