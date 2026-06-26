#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{}".format(chr(ord('z') - i) if (25 - i) % 2 == 0
          else chr(ord('Z') - i)), end="")
