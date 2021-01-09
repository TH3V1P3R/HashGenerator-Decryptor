from hasher import h
from readhw import rdw
use_ag = 'y'
options=['y', 'Y' , 'yes', 'sure', 'Sure' , 'of cours', 'Yes', 'yep', 'Yep', 'Yeah', 'yeah']
while use_ag in options:
    y_hash = str(input("your hash: "))
    y_wordlist = str(input("the wordlist: "))
    htypes = str(input("hash type: "))
    rr = rdw()
    readall = rr.read(y_wordlist)
    hh = h()
    a = []
    for i in readall:
        i = i.rstrip("\n")
        hasht = hh.hashin(i,htypes)
        a.append(hasht)
        global t
        t = a[:]
        if y_hash in t:
            print("Hash Cracked!!\n==>{0}::{1}".format(y_hash,i))
            break;
    if y_hash not in t:
        print("Password Not Found!")
    use_ag=str(input("do you want to use again: "))    
input("press enter to exit...")

