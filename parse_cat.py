#!/usr/bin/env python
#-*- coding: utf-8 -*-

# Note to Bill Harris: this is the worst possible way of formatting data.

import numpy as np
import matplotlib.pyplot as p
import pandas as pd
from collections import OrderedDict

a = open('mwgc.dat', 'r')
lines = a.readlines()

d = OrderedDict({})
p = []
coldefs = []

for j,line in enumerate(lines):
    if 'ID' in line:
        colnames = line.split()
        tmp = colnames
        for i,col in enumerate(colnames):
            if '+' in col:
                tmp[i] = tmp[i-1]+'err'
            d[tmp[i]] = []
        coldefs.append(tmp)
        p.append(j+2)
    if 'NGC 7492' in  line:
        p.append(j+1)

#datalines = lines[p[0]:p[1]] + lines[p[2]:p[3]] + lines[p[4]:p[5]]
datalines = lines[p[0]:p[1]]

# Part 1
for j, line in enumerate(datalines):
    cols = coldefs[0]
    d[cols[0]].append(line[0:9].strip())
    d[cols[1]].append(line[10:21].strip())
    d[cols[2]].append(line[23:37].strip())
    d[cols[3]].append(line[38:51].strip())
    d[cols[4]].append(line[52:60].strip())
    d[cols[5]].append(line[61:68].strip())
    d[cols[6]].append(line[68:74].strip())
    d[cols[7]].append(line[74:80].strip())
    d[cols[8]].append(line[80:85].strip())
    d[cols[9]].append(line[85:91].strip())
    d[cols[10]].append(line[91:97].strip())


# Part 2
datalines = lines[p[2]:p[3]]
for j, line in enumerate(datalines):
    cols = coldefs[1]
    d[cols[1]].append(line[10:17].strip())
    d[cols[2]].append(line[17:19].strip())
    d[cols[3]].append(line[23:27].strip())
    d[cols[4]].append(line[28:34].strip())
    d[cols[5]].append(line[35:40].strip())
    d[cols[6]].append(line[40:45].strip())
    d[cols[7]].append(line[46:53].strip())
    d[cols[8]].append(line[53:60].strip())
    d[cols[9]].append(line[60:66].strip())
    d[cols[10]].append(line[66:72].strip())
    d[cols[11]].append(line[72:79].strip())
    d[cols[12]].append(line[79:86].strip())
    d[cols[13]].append(line[85:].strip())

# Part 3
datalines = lines[p[4]:p[5]]
for j, line in enumerate(datalines):
    cols = coldefs[2]
    d[cols[1]].append(line[12:20].strip())
    d[cols[2]].append(line[20:26].strip())
    d[cols[3]].append(line[26:34].strip())
    d[cols[4]].append(line[34:42].strip())
    d[cols[5]].append(line[42:48].strip())
    d[cols[6]].append(line[48:54].strip()) # skip core-collapse label
    d[cols[7]].append(line[59:64].strip())
    d[cols[8]].append(line[64:70].strip())
    d[cols[9]].append(line[70:78].strip())
    d[cols[10]].append(line[78:86].strip())
    d[cols[11]].append(line[86:92].strip())
    d[cols[12]].append(line[92:].strip())

df = pd.DataFrame(d)


# Add correct types and mask n/a
df[df==''] = np.NaN
for col in coldefs[0]+coldefs[1]+coldefs[2]:
    if col not in "RA DEC Name ID spt".split():
        print col
        df[col] = df[col].astype(np.float64)
    else:
        df[col] = df[col].astype(np.str)

import ipdb; ipdb.set_trace()  # XXX BREAKPOINT
