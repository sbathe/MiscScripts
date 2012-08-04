#!/usr/bin/python
import collections
f = open('/home/sbathe/.config/google-chrome/Default/Extensions/bfbameneiokkgbdmiekhjnmfkcnldhhm/0.4.1_0/license.txt','r')
data = f.readlines()
f.close()
counts = collections.defaultdict(int)
for line in data:
  for word in line.split():
    for c in word:
      counts[c.upper()] += 1 

for k,v in counts.iteritems():
 print "%s: %d" %(k, v)
