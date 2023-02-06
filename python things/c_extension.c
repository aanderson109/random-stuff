/**
C extension meant to plug into a Python program
**/

// recommended to define this before other libraries
#define PY_SSIZE_T_CLEAN

// recommended to define the Python library before standard ones
//#include <Python.h>

// now we define standard libraries for C/C++
#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include <stdlib.h>

/** This code can be summarized as:
1. open a file called write.txt
2. write the string real python to the file
**/
int main() {
  FILE *fp = fopen("write.txt", "w");
  fputs("real python!", fp);
  fclose(fp);
  return 1;
}
