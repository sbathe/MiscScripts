#!/usr/bin/python
# Uses collections.defaultdict 
# So that I do not have to do:
#
# if not paircount.has_key(hold):
#   paircount[hold]=1
# else
#   paircount[hold] += 1
import collections
str = 'abcdefghijklmnopqrstuvwxyz'
paircount = collections.defaultdict(int)
letterdict = {}
pairs=0
old='' 
hold='' 
for c in str:
  if old:
    letterdict[old]=c
    old=c
  else:
    old=c
f = open('/home/sbathe/.config/google-chrome/Default/Extensions/bfbameneiokkgbdmiekhjnmfkcnldhhm/0.4.1_0/license.txt','r')
while True:
  c = f.read(1)
  if not c:
    print "EOF"
    break
  else:
    if hold: 
      if letterdict.has_key(hold):
        if c == letterdict[hold]:
          paircount[hold] += 1
          pairs += 1
      hold=c
    else:
      print " hold not found, setting hold to %c" %( c )
      hold=c
f.close()
for k in letterdict.iterkeys():
  print "Pairing for %s : %d" %(k,paircount[k])
print pairs
