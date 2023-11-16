import math

slova = ['S','T','P','H','K','Z']

def komb(slova,duzina,i,ans,cur):
    if i==duzina:
        ans.append(cur.copy())
    else:
        for c in slova:
            cur.append(c)
            komb(slova,duzina,i+1,ans,cur)
            cur.pop()

def vratiSveKombinacije(slova,duzina):
    ans = []
    komb(slova,duzina,0,ans,[])
    return ans

def calcEntropy(cnt,duzina):
    ans=0.0
    for v in cnt.values():
        p=v/duzina
        ans-=p*math.log(p,2)
    return ans

def racunaj(komb):
    rez=[]
    for a in komb:
        cur=a.copy()
        cnt={}
        for b in komb:
            moguci=b.copy()
            cz = [0, 0]
            for i in range(len(cur)):
                id = nadji(cur[i], moguci)
                if i == id:
                    cz[0] += 1
                    moguci[i] = 'x'
                elif id != -1:
                    cz[1] += 1
                    moguci[id] = 'x'
            if tuple(cz) in cnt.keys():
                cnt[tuple(cz)]+=1
            else:
                cnt[tuple(cz)]=1
        rez.append([cur.copy(),calcEntropy(cnt,len(komb))])
        #print(cnt)
        #print(cur,ans)
    return rez
def nadji(c,str):
    for i in range(len(str)):
        if str[i]==c:
            return i
    return -1
def crvenoZuti(a,b):
    komb1 = a.copy()
    komb2 = b.copy()
    ans = [0,0]
    for i in range(len(komb1)):
        id = nadji(komb1[i],komb2)
        if i==id:
            ans[0]+=1
            komb2[i]='x'
            komb1[i]='o'
    #print(komb1,komb2)
    for i in range(len(komb1)):
        id = nadji(komb1[i],komb2)
        if id!=-1:
            ans[1]+=1
            komb2[id]='x'
            komb1[i]='o'
    #print(komb1,komb2)
    return ans

sveKombinacije = vratiSveKombinacije(slova,4)
komb = sveKombinacije.copy()
target = ['S','H','P','T']# set to None for manual input
opt = 'a'
while opt != 'q':
    komb = sveKombinacije.copy()
    while len(komb)>1:
        rez = racunaj(komb)
        #rez.sort(key=lambda x:-x[1])

        #print(rez[0][0])
        maksimal = max(rez,key=lambda x:x[1])[0]
        print(maksimal)
        cz0=[0,0]
        if target==None:
            cz0[0] = int(input('Broj crvenih kruzica:'))
            cz0[1] = int(input('Broj zutih kruzica:'))
        else:
            cz0 = crvenoZuti(maksimal,target)
        #print(cz0)
        for i in range(len(komb)-1,-1,-1):
            cz = crvenoZuti(maksimal,komb[i])
            #print(cz)
            if cz[0]!=cz0[0] or cz[1]!=cz0[1]:
                komb.pop(i)
    print(komb)
    opt = input(opt)
