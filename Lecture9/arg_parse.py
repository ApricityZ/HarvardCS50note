# import sys
#
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
# else:
#     print("Usage: {filename.py} [-n NUMBER]")

# %%
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("-n")
# args = parser.parse_args()
#
# for _ in range(int(args.n)):
#     print("meow")

# # %%
# import argparse
#
# parser = argparse.ArgumentParser(description="Meow like a cat")
# parser.add_argument("-n", help="number of times to meow")
# args = parser.parse_args()
#
# for _ in range(int(args.n)):

# %%
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-a", default=1, help="number of times to meow", type=int)
args = parser.parse_args()
print(type(args))
print(args)

for _ in range(int(args.a)):
    print("meow")