// gcc ./stack.c -o stack -fno-stack-protector -no-pie
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>

int check(){
  printf("Welcome to CSE545 Week 6! Type your ASURITE to check Participation\n");
  char id[50] = {};
  gets(id);
  char *path;
  path = (char *)malloc(strlen(id) + 20);
  strncpy(path, "records/", 8);
  strncat(path, id, strlen(id));
  printf("checking %s\n", path);
  return(access(path, F_OK) != -1);
}


int main(){
	setbuf(stdout, NULL);
  if(check())
	  printf("Your participation is logged\n");
  else
	  printf("Your participation is NOT logged\n");
}
