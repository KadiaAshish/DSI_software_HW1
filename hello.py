import argparse

parser = argparse.ArgumentParser(description='say hello')
parser.add_argument('name')
parser.add_argument('-r', type=int, default=1, help='repeats')
args=parser.parse_args()

for i in range(args.r):
  print('Hello ' + args.name + '!')