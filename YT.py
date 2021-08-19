#!/usr/bin/env python3
from pytube import YouTube
import os
import sys

try:
   FILE = sys.argv[1]
   NUM = sys.argv[2]
   file3 = open(FILE)
   lines = int(NUM)

   for i in range(lines):
       line = file3.readline()
       os.system(f"pytube {line}")
except IndexError:
    print("USAGE: python3 YT.py <file with video links> <number of lines ex.: 10, will download first 10 lines>")
