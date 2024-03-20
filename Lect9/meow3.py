import sys

if len(sys.argv) ==1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py")

"""
-n -后面是字母
--version --后面是单词

argparse python 库
"""