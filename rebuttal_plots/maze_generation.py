# !/usr/bin/python
# -*- coding: utf-8 -*-

# Maze Generator using unicode line drawing chars
# by Vidar 'koala_man' Holen
# www.vidarholen.net

# See the online demo on
# http://www.vidarholen.net/~vidar/generatemaze.py

from random import *
from sys import *

picwidth = 20
picheight = 20
if len(argv) > 1:
    picwidth = int(argv[1])
    if len(argv) > 2:
        picheight = int(argv[2])

width = picwidth  # (picwidth)/2+1
height = picheight  # (picheight)/2+1

# print "Generating %dx%d maze" % (width,height)

map = []  # map[x][y]
for i in range(width):
    n = []
    for j in range(height):
        n.append([1, 1, 0, 0, 0])  # right, bottom, captured, backtrack, color
    map.append(n)

for y in range(height):
    map[0][y] = [1, 0, 1, 0, 0]
    map[width - 1][y] = [1, 0, 1, 0, 0]

for x in range(width):
    map[x][0] = [0, 1, 1, 0, 0]
    map[x][height - 1] = [0, 1, 1, 0, 0]

map[0][0] = [0, 0, 1, 0, 0]
map[width - 1][0] = [0, 0, 1, 0, 0]

playerstart = (1, 1)
playerexit = (width - 1, height - 1)
mazestart = playerstart

x, y = mazestart
backtrack = 1
captures = 0
solutiontrack = 0

while 1:
    if (x, y) == playerexit:
        solutiontrack = backtrack

    if solutiontrack > 0 and solutiontrack == map[x][y][3]:
        solutiontrack = solutiontrack - 1
        map[x][y][4] = 2

    if map[x][y][2] == 0:
        map[x][y][2] = 1
        captures = captures + 1
        if captures % 10000 == 0:
            print(100 * captures / (width * height), file=stderr)

        #    map[x][y][2]=1
    map[x][y][3] = backtrack
    possibilities = []
    for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if a >= 0 and a < width and b >= 0 and b < height:
            if map[a][b][2] == 0:
                possibilities.append((a, b))

    if len(possibilities) == 0:
        map[x][y][3] = 0
        backtrack = backtrack - 1
        if backtrack == 0:
            break
        for a, b in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (-1, -1)]:
            if a >= 0 and a < width and b >= 0 and b < height:
                if map[a][b][3] == backtrack:
                    break

        x = a
        y = b
        continue

    pos = randint(0, len(possibilities) - 1)
    a, b = possibilities[pos]
    if a < x: map[a][b][0] = 0
    if a > x: map[x][y][0] = 0
    if b < y: map[a][b][1] = 0
    if b > y: map[x][y][1] = 0
    x = a
    y = b
    backtrack = backtrack + 1

print(f"Maze {picwidth} x {picheight}", file=stderr)
# print("Done,", captures, "visited", file=stderr)

pixmap = []
for i in range(width):
    pixmap.append([0] * height)

# use Monospace font in pyCharm
chars = [' ', '╶', '╷', '┌', '╴', '─', '┐', '┬', '╵', '└', '│', '├', '┘', '┴', '┤', '┼']

for y in range(0, height - 1):
    for x in range(0, width - 1):
        u = map[x][y][0]
        l = map[x][y][1]
        d = map[x][y + 1][0]
        r = map[x + 1][y][1]
        char = u * 8 + l * 4 + d * 2 + r
        stdout.write(chars[char])
        if r == 0:
            stdout.write(chars[0])
        else:
            stdout.write(chars[5])
    stdout.write('\n')

exit(0)
for y in range(-1, picheight):
    for x in range(-1, picwidth):
        n = pixmap[x][y]
        if n == 0:
            stdout.write('\xFF\xFF\xFF')
        elif n == 1:
            stdout.write('\x00\x00\x00')
        elif n == 2:
            stdout.write('\xFF\xFF\xFF')  # show solution
        elif n == 3:
            stdout.write('\x00\x00\xFF')
        else:
            stdout.write('\xFF\x00\xFF')
