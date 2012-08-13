#!/usr/bin/python
key = []
str = ''
for x in range(26):
  key.append(chr(ord('a') + x))
f = open('/tmp/ocr.txt','r')
while True:
  c = f.read(1)
  if not c:
    print "EOF"
    break
  else:
    if c in key:
      str += c
print str
