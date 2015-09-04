#!/usr/bin/python

# quick test to determine speed of searching lists vs searching strings
# turns out searching a list is quicker... from profiler.log:
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#  42000000   13.991    0.000   13.991    0.000 ListVsString.py:17(IsColorInList)
#  42000000   10.294    0.000   10.294    0.000 ListVsString.py:13(IsColorInString)


import os.path
import sys
import time
import cProfile
import pstats

colorsString = "red green blue black white yellow maroon purple brown grey orange peach aquamarine cobalt navy rust ltgreen dkgreen royal straw amithest"
colorsList = colorsString.split()

def IsColorInString(searchColor):
    global colorsString
    return searchColor in colorsString

def IsColorInList(searchColor):
    global colorsList
    return searchColor in colorsList

def main():
    for z in range(0, 2000000):
        for searchColor in colorsList:
            x = IsColorInString(searchColor)
            x = IsColorInList(searchColor)

cProfile.run('main()', "profiler.raw", "tottime")
output_handle = open("profiler.log", 'a')
p = pstats.Stats('profiler.raw', stream=output_handle)
p.strip_dirs().sort_stats("tottime").print_stats(18)
output_handle.close()
