# Demonstrates own module

import sys

from sayings2 import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
elif len(sys.argv) > 2:
    print("Too many command-line arguments")
else:
    print("Too few command-line arguments")