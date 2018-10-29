from random import shuffle

f = open('data.txt', 'r+')
songlist = []

for song in f:
    songlist.append(song)

if '\n' not in songlist[-1]:
    songlist[-1] += '\n'

shuffle(songlist)
f.seek(0)

for song in songlist:
  f.write(song)