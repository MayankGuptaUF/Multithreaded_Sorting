import xmlrpc.client

import random
import sys
address=sys.argv[1]
N=(int(sys.argv[2]))
R=(int(sys.argv[3]))
string="http://"+address
s = xmlrpc.client.ServerProxy(string)

def generate(N,R):
    
    ra=[]
    for i in range(1,R):
        ra.append(i)
    return random.sample(ra, N)

arra=generate(N,R)

print("Generated List",arra)
print("Sorted List",s.para(N,R,arra))


