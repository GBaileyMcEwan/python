#!/usr/bin/python3

import sys,argparse

#basic stuff with sys.argv
#print(f"All arguements: {sys.argv[0:]}")
#print(f"First arguement: {sys.argv[1]}")


#build a parser with argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
#optional arguements must start with --
parser.add_argument('--limit', '-l', type=int, help='the amount of lines you want to read')
#show the version of your code
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()
#print(args)

with open(args.filename) as f:
   lines = f.readlines()
   lines.reverse()

   if args.limit:
      lines = lines[:args.limit]

   for line in lines:
      print(line.strip()[::-1])

#parse the arguements


#read the file, reverse the contents and print
