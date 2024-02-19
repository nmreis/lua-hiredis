#! /bin/bash
set -e

gcc -O2 -fPIC -I/usr/include/lua5.3 -c src/lua-hiredis.c -Isrc/ -Ilib/ --pedantic -Wno-implicit-function-declaration --std=c99
gcc -shared -o hiredis.so lua-hiredis.o -llua5.3
