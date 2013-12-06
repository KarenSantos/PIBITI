import os
import random
from inspect import getfile

print "hello world"

paisagem1 = open("static/paisagem1.txt", "r")

if paisagem1.read() == "":
    print "vazia"
else:
    print "tem coisa"

texto = paisagem1.read()

print texto

