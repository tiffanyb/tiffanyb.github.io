#include <stdio.h>
#include <string.h>

int testme(char *buf, unsigned len);

int main(int argc, char *argv[])
{
  FILE *f;
  char buf[12];

  if(argc != 2){
    fprintf(stderr, "Must supply a text file\n");
    return -1;
  }
  f = fopen(argv[1], "r");
  if(f == NULL){
    fprintf(stderr, "Could not open %s\n", argv[1]);
    return -1;
  }
  if(fgets(buf, sizeof(buf), f) == NULL){
    fprintf(stderr, "Could not read from %s\n", argv[1]);
    return -1;
  }
  testme(buf, strlen(buf));
  return 0;
}
