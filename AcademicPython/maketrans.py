#!/usr/bin/python
alpha=[]
key=[]
h={}
for x in range(26):
  key.append(chr(ord('A') + x))
  if (ord('C')+x) <= ord('Z'):
    alpha.append(chr(ord('C') + x))
  else:
    alpha.append(chr(ord('C') -( 26 - x)))
for x in range(26):
  h[key[x]]=alpha[x]

ciphertext="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
trans = string.maketrans(ciphertext.upper, cleartext)

#for c in ciphertext:
#  if h.has_key(c.upper()):
#    print c.upper() + "found in h" 
#    cleartext += h[c.upper()]
#  else:
#    print c.upper() + "not found in h " 
#    cleartext += c 
print cleartext
