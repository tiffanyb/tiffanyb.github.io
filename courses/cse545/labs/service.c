#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define LOG 1
#define EXIT 2

char menu[2][20] = {"Log Participation", "Exit"};

void print_greeting(){
  printf("Welcome to CSE545 In-class Lab 1\n");
}

void print_menu(){
  for (int i = 0; i < 2; i++)
    printf("%d. %s\n", i + 1, menu[i]);
  printf("Please select from menu: ");
  fflush(stdout);
}


int validate(){
  time_t t;
  int a, b, c, result = 1;
  char *buf = NULL;
  size_t size = 0;
  srand((unsigned)time(&t));

  for(int i = 0; i < 100; i++){
    a = rand() % 50;
    b = rand() % 50;
    printf("What's the sum of %d and %d? ", a, b);
    fflush(stdout);
    getline(&buf, &size, stdin);
    c = atoi(buf);
    result &= (a + b == c);
  }
  return result;
}


void record(char id[15]){
  char command[50] = {};
  sprintf(command, "touch records/%s", id);
  system(command);
}


void interaction(){
  int n;
  char *buf = NULL;
  size_t size = 0;
  char asuid[15] = {};
  while(1){
    print_menu();
    getline(&buf, &size, stdin);
    n = atoi(buf);

    switch(n){
      case LOG:
        if (validate() == 1){
          printf("Your ASUID: ");
          fflush(stdout);
          scanf("%s", asuid);
          record(asuid);
          printf("You got it!\n");
        }
        else{
          printf("Verification error\n");
          return;
        }
        break;
      case EXIT:
        printf("Bye!\n");
        return;
      default:
        printf("Wrong menu selection\n");
    }
  }
}


int main(){
  print_greeting();
  interaction();
  return 0;
}
