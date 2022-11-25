'''
from array import *                                       # "*" tame badha function sathework karava mango co.
                                                          # import array as arr<tame avi rite pan koy function import kari sako cho.>
vals = array('i', [5, 9, 8, 4, 2])                        # ama 'i' ee integer emm define kare che. jema khali integej avase.

#vals.reverse()

for i in range(len(vals)):                                #always ani sathe work karavanu rahase.
    print(vals[i])
#vals = array('u', ['a', 'e', 'i'])                       #unicode sathe pan work karase.[char]

for e in vals:                                            #aa biji method che.
    print(e)


print(vals)
'''

from array import *
vals = array('i', [5, 9, 8, 4, 2])
newarray = array(vals.typecode, (a for a in vals))

#for e in newarray:
 #   print(e)
e=0
while e <len(newarray):
    print(newarray[e])
    e+=1
