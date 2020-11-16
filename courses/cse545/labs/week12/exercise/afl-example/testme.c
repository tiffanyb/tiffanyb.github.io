int testme(char *buf, unsigned len)
{
  unsigned ok;

  if(!ok) // Defect: uninitialized use of ok.
    ok = len;

  if(buf[0] == 'b')
    if(buf[1] == 'a')
      if(buf[2] == 'd') {
        __builtin_trap(); // Bug!
      }
  return 0;
}
