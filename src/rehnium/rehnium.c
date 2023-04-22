/*
  emcc rehnium.c -o rehnium.js
*/
#include <stdlib.h>
#include <stdio.h>
#include <emscripten.h>

EMSCRIPTEN_KEEPALIVE
int flag(int index) {
  static int flag_arr[] = {48, 120, 52, 48, 54, 55, 123, 119, 51, 56, 95, 52, 53, 53, 95, 100, 49, 53, 52, 53, 125};
  int flag_decimal = flag_arr[index];
  return 0;
}