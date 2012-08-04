#!/usr/bin/python
# will match pairs like ab, bc, cd ... using ascii codes instead of hash
# goes without saying this works only for ASCII , not UTF
# but saves us the hassle of creating a dict mapping and takes care of number and some special characters too.
pairs = 0
hold = ''
f = open('/home/sbathe/.config/google-chrome/Default/Extensions/bfbameneiokkgbdmiekhjnmfkcnldhhm/0.4.1_0/license.txt','r')
while True:
  c = f.read(1)
  if not c:
    print "EOF"
    break
  else:
    if hold: 
      if ord(c) == (ord(hold) + 1):
        pairs += 1
      hold=c
    else:
      print " hold not found, setting hold to %c" %( c )
      hold=c
f.close()
print pairs
