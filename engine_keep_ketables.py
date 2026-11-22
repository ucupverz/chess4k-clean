import json;import os;import urllib.request;INF=30000;BU=450000;MSK=262143;MV=(0,100,320,330,500,900,0);PS='AAAAAAAADFF77FFDD><AA<>DAAAKKAAADDFMMFDDFFKPPKFFZZZZZZZZAAAAAAAA(-2222-(-7ACCA7-2CFHHFC22AHKKHA27<<<<<<7<CAAAAC<<FFFFFF<<AFFFFA<AACCCCAA?AACCAA??AAAAAA??AAAAAA?7<<??<<7<AAAAAA<<ACCCCA<?ACCCCA?KPF<<FPKKKA<<AKK<777777<722--2272--((--22--((--22--((--22--((--2';PT=[[0]*128 for _ in range(7)];_i=0
for _t in(1,2,3,4,5,6):
    _m=8 if _t in(1,6)else 4
    for _r in range(8):
        _j=_i+(_r if _m==8 else min(_r,7-_r))*8;PT[_t][_r*16:_r*16+8]=[2*(ord(c)-65)for c in PS[_j:_j+8]]
    _i+=_m*8
PZ=[[0]*128 for _ in range(16)]
for _t in range(1,7):
    for _s in range(128):
        if not _s&136:
            PZ[_t][_s]=MV[_t]+PT[_t][_s];PZ[_t+8][_s]=MV[_t]+PT[_t][_s^112]
_x=20260820
def _r():
    global _x;_x=_x*6364136223846793005+1442695040888963407&18446744073709551615;return _x
Z=[[_r()for _ in range(128)]for _ in range(16)];ZC=[_r()for _ in range(16)];ZE=[_r()for _ in range(8)];ZS=_r()
def _ray(s,o):
    r=[]
    while 1:
        s+=o
        if s>127 or s<0 or s&136:
            return r
        r.append(s)
RA=[[_ray(s,o)for o in(17,15,-17,-15,16,1,-16,-1)]for s in range(128)];RD=[r[:4]for r in RA];RF=[r[4:]for r in RA];NT=[[n for n in(s+o for o in(33,31,18,14,-33,-31,-18,-14))if n<128 and(not n&136)]for s in range(128)];KT=[[n for n in(s+o for o in(17,16,15,1,-1,-15,-16,-17))if n<128 and(not n&136)]for s in range(128)];PA=[[[n for n in(s+15,s+17)if n<128 and(not n&136)]for s in range(128)],[[n for n in(s-15,s-17)if not n&136]for s in range(128)]];PQ=[[[n for n in(s-15,s-17)if not n&136]for s in range(128)],[[n for n in(s+15,s+17)if n<128 and(not n&136)]for s in range(128)]];RC=[~0]*128;RC[0]=~2;RC[7]=~1;RC[112]=~8;RC[119]=~4;B=[0]*128;PC=[[[]for _ in range(7)]for _ in range(2)];KS=[0,0];S=CT=EP=HM=H=MG=N=BM=0;U=[];HU=[];GS=set();TT=[None]*(MSK+1);K1=[0]*128;K2=[0]*128;HH=[0]*16384;Q1=Q2=0;GID=-1;KE=[8*(min(s>>4,7-(s>>4))+min(s&7,7-(s&7)))for s in range(128)]
class Cut(Exception):
    pass
def setpos(f):
    global B,PC,KS,S,CT,EP,HM,H,MG;B=[0]*128;PC=[[[]for _ in range(7)]for _ in range(2)];KS=[0,0];MG=H=0;a=f.split();r=7;c=0
    for ch in a[0]:
        if ch=='/':
            r-=1;c=0
        elif ch.isdigit():
            c+=int(ch)
        else:
            p=' PNBRQK'.index(ch.upper())
            if ch>'Z':
                p|=8
            s=p>>3;q=r*16+c;B[q]=p;PC[s][p&7].append(q);MG+=(1-2*s)*PZ[p][q];H^=Z[p][q]
            if p&7==6:
                KS[s]=q
            c+=1
    S=0 if a[1]=='w'else 1
    if S:
        H^=ZS
    CT=0
    for ch in a[2]if len(a)>2 else'-':
        CT|={'K':1,'Q':2,'k':4,'q':8}.get(ch,0)
    EP=0
    if len(a)>3 and a[3]!='-':
        EP=(int(a[3][1])-1)*16+ord(a[3][0])-97
    HM=int(a[4])if len(a)>4 else 0;H^=ZC[CT]
    if EP:
        H^=ZE[EP&7]
    del HU[:];del U[:]
def atk(q,c):
    b=B;t=(c<<3)+2
    for n in NT[q]:
        if b[n]==t:
            return 1
    t-=1
    for n in PQ[c][q]:
        if b[n]==t:
            return 1
    t+=5
    for n in KT[q]:
        if b[n]==t:
            return 1
    for r in RD[q]:
        for n in r:
            p=b[n]
            if p:
                if p>>3==c and(p&7==3 or p&7==5):
                    return 1
                break
    for r in RF[q]:
        for n in r:
            p=b[n]
            if p:
                if p>>3==c and(p&7==4 or p&7==5):
                    return 1
                break
    return 0
def inf(s):
    b=B;e=s^1;k=KS[s];ck=0;pn={}
    for i,r in enumerate(RA[k]):
        bl=0
        for n in r:
            q=b[n]
            if q:
                if bl:
                    if q>>3==e and(q&7==5 or q&7==(3 if i<4 else 4)):
                        pn[bl]=set(r)
                    break
                if q>>3==s:
                    bl=n
                elif q&7==5 or q&7==(3 if i<4 else 4):
                    ck=1;break
                else:
                    break
        if ck:
            break
    if not ck:
        for n in NT[k]:
            if b[n]==(e<<3)+2:
                ck=1;break
        if not ck:
            for n in PQ[e][k]:
                if b[n]==(e<<3)+1:
                    ck=1;break
    return(ck,pn)
def gen(cap):
    b=B;s=S;ep=EP;P=PC[s];ms=[];ap=ms.append;d=16 if not s else-16;r2=1 if not s else 6
    for f in P[1]:
        t=f+d
        if not b[t]:
            u=t>>4
            if u==0 or u==7:
                for c in(1,2,3,4):
                    ap(f|t<<7|c<<14)
            elif not cap:
                ap(f|t<<7)
                if f>>4==r2 and(not b[t+d]):
                    ap(f|t+d<<7)
        for n in PA[s][f]:
            q=b[n]
            if q:
                if q>>3!=s:
                    if n>>4==0 or n>>4==7:
                        for c in(1,2,3,4):
                            ap(f|n<<7|c<<14)
                    else:
                        ap(f|n<<7)
            elif n==ep and ep:
                ap(f|n<<7|5<<14)
    for f in P[2]:
        for n in NT[f]:
            q=b[n]
            if q:
                if q>>3!=s:
                    ap(f|n<<7)
            elif not cap:
                ap(f|n<<7)
    for f in P[6]:
        for n in KT[f]:
            q=b[n]
            if q:
                if q>>3!=s:
                    ap(f|n<<7)
            elif not cap:
                ap(f|n<<7)
    for t,rays in((3,RD),(4,RF),(5,RA)):
        for f in P[t]:
            for r in rays[f]:
                for n in r:
                    q=b[n]
                    if q:
                        if q>>3!=s:
                            ap(f|n<<7)
                        break
                    if not cap:
                        ap(f|n<<7)
    if not cap:
        f=KS[s]
        if f==4 or f==116:
            o=1-s
            if s:
                if not b[117]and(not b[118])and CT&4 and(not atk(116,o))and(not atk(117,o)):
                    ap(116|118<<7|6<<14)
                if not b[113]and(not b[114])and(not b[115])and CT&8 and(not atk(116,o))and(not atk(115,o)):
                    ap(116|114<<7|6<<14)
            else:
                if not b[5]and(not b[6])and CT&1 and(not atk(4,o))and(not atk(5,o)):
                    ap(4|6<<7|6<<14)
                if not b[1]and(not b[2])and(not b[3])and CT&2 and(not atk(4,o))and(not atk(3,o)):
                    ap(4|2<<7|6<<14)
    return ms
def mk(m):
    global B,H,MG,CT,EP,HM,S;f=m&127;t=m>>7&127;c=m>>14;p=B[f];s=p>>3;v=B[t];U.append((m,v,CT,EP,HM,H,MG,s));HU.append(H);g=1-2*s;H^=Z[p][f]^Z[p][t]^ZS
    if v:
        H^=Z[v][t];MG+=g*PZ[v][t];PC[1-s][v&7].remove(t)
    B[t]=p;B[f]=0;pl=PC[s][p&7];pl.remove(f);pl.append(t);MG+=g*(PZ[p][t]-PZ[p][f]);oc=CT;oe=EP;EP=0
    if p&7==1:
        if t-f==32 or f-t==32:
            EP=f+t>>1
        HM=0
    elif v:
        HM=0
    else:
        HM+=1
    if c and c<5:
        q=c+1|s<<3;B[t]=q;pl.remove(t);PC[s][c+1].append(t);MG+=g*(PZ[q][t]-PZ[s*8+1][t]);H^=Z[q][t]^Z[s*8+1][t];HM=0
    elif c==5:
        n=t-16 if not s else t+16;v=B[n];B[n]=0;PC[1-s][1].remove(n);MG+=g*PZ[v][n];H^=Z[v][n];HM=0
    elif c==6:
        if t>f:
            r0=f+3;r1=f+1
        else:
            r0=f-4;r1=f-1
        rp=B[r0];B[r1]=rp;B[r0]=0;pq=PC[s][4];pq.remove(r0);pq.append(r1);MG+=g*(PZ[rp][r1]-PZ[rp][r0]);H^=Z[rp][r0]^Z[rp][r1]
    if p&7==6:
        CT&=12 if not s else 3;KS[s]=t
    elif p&7==4:
        CT&=RC[f]
    if v and v&7==4:
        CT&=RC[t]
    H^=ZC[oc]^ZC[CT]
    if oe:
        H^=ZE[oe&7]
    if EP:
        H^=ZE[EP&7]
    S=s^1
def mkn():
    global H,EP,HM,S;s=S;U.append((0,0,CT,EP,HM,H,MG,s))
    if EP:
        H^=ZE[EP&7]
    EP=0;HM+=1;H^=ZS;S=s^1
def um():
    global B,H,MG,CT,EP,HM,S;m,v,CT,EP,HM,H,MG,s=U.pop()
    if not m:
        S=s;return
    HU.pop();S=s;f=m&127;t=m>>7&127;c=m>>14;p=B[t]
    if c and c<5:
        PC[s][c+1].remove(t);PC[s][1].append(f);B[f]=s*8+1
    else:
        PC[s][p&7].remove(t);PC[s][p&7].append(f);B[f]=p
    B[t]=v
    if v:
        PC[1-s][v&7].append(t)
    if c==5:
        n=t-16 if not s else t+16;B[n]=9-s*8;PC[1-s][1].append(n)
    elif c==6:
        if t>f:
            r0=f+3;r1=f+1
        else:
            r0=f-4;r1=f-1
        rp=B[r1];B[r0]=rp;B[r1]=0;pq=PC[s][4];pq.remove(r1);pq.append(r0)
    if p&7==6:
        KS[s]=f
def ev():
    v=MG+(24 if len(PC[0][3])>1 else 0)-(24 if len(PC[1][3])>1 else 0)
    if not PC[0][5]and not PC[1][5]:v+=KE[KS[0]]-KE[KS[1]]
    return v if not S else -v
def sk(m):
    t=m>>7&127;v=B[t]
    if v:
        return 100000+(v&7)*64-(B[m&127]&7)
    if m>>14:
        return 95000+(m>>14)
    if m==Q1:
        return 90000
    if m==Q2:
        return 89000
    return HH[(m&127)<<7|t]
def qs(a,b,ply):
    global N;N+=1
    if N>BU:
        raise Cut
    s=S;e=s^1;k=KS[s];ck,pn=inf(s);nk=ck;best=-INF
    if not nk:
        best=ev()
        if best>=b:
            return best
        if best>a:
            a=best
    ms=gen(not nk)
    if len(ms)>1:
        ms.sort(key=sk,reverse=True)
    n=0
    for m in ms:
        t=m>>7&127
        if nk or m&127==k:
            mk(m)
            if atk(KS[s],e):
                um();continue
        else:
            if pn:
                ps=pn.get(m&127)
                if ps is not None and t not in ps:
                    continue
            mk(m)
            if m>>14==5 and atk(k,e):
                um();continue
        n+=1;v=-qs(-b,-a,ply+1);um()
        if v>best:
            best=v
            if v>a:
                a=v
                if a>=b:
                    break
    if nk and(not n):
        return-INF+ply
    return best
def srch(d,a,b,ply):
    global N,BM,Q1,Q2;N+=1
    if N>BU:
        raise Cut
    s=S;e=s^1
    if ply and(HM>99 or H in HU or H in GS):
        return 0
    ck,pn=inf(s);nk=ck
    if nk:
        d+=1
    if d<1:
        return qs(a,b,ply)
    k=KS[s];h=H;en=TT[h&MSK];tm=0
    if en is not None and en[0]==h:
        tm=en[4]
        if ply and en[1]>=d:
            v=en[3]
            if v>29000:
                v-=ply
            elif v<-29000:
                v+=ply
            if en[2]==0 or(en[2]==1 and v>=b)or(en[2]==2 and v<=a):
                return v
    if not nk and ply and(d>=3)and(PC[s][2]or PC[s][3]or PC[s][4]or PC[s][5]):
        mkn();v=-srch(d-3 if d>=6 else d-2,-b,1-b,ply+1);um()
        if v>=b:
            return v
    ms=gen(0)
    if len(ms)>1:
        Q1=K1[ply];Q2=K2[ply];ms.sort(key=sk,reverse=True)
    if tm and tm in ms:
        ms.remove(tm);ms.insert(0,tm)
    best=-INF;bm=0;oa=a;n=0
    for m in ms:
        f=m&127;t=m>>7&127;cap=B[t]or m>>14
        if nk or f==k:
            mk(m)
            if atk(KS[s],e):
                um();continue
        else:
            if pn:
                ps=pn.get(f)
                if ps is not None and t not in ps:
                    continue
            mk(m)
            if cap==5 and atk(k,e):
                um();continue
        if not n:
            v=-srch(d-1,-b,-a,ply+1)
        else:
            r=0
            if d>=3 and n>=3 and(not cap)and(not nk):
                r=2 if d>=6 and n>=10 else 1
            v=-srch(d-1-r,-a-1,-a,ply+1)
            if v>a:
                v=-srch(d-1,-b,-a,ply+1)
        um()
        if v>best:
            best=v;bm=m
            if not ply:
                BM=m
            if v>a:
                a=v
                if a>=b:
                    if not cap:
                        x=f<<7|t;w=HH[x]+d*d;HH[x]=w if w<60000 else 60000
                        if K1[ply]!=m:
                            K2[ply]=K1[ply];K1[ply]=m
                    break
        n+=1
    if not bm:
        return-INF+ply if nk else 0
    if best>29000:
        v=best+ply
    elif best<-29000:
        v=best-ply
    else:
        v=best
    fl=0
    if best<=oa:
        fl=2
    elif best>=b:
        fl=1
    en=TT[h&MSK]
    if en is None or en[0]!=h or en[1]<=d:
        TT[h&MSK]=(h,d,fl,v,bm)
    return best
def best():
    global N,BM;N=0;bm=0;d=1
    while d<64:
        BM=0
        try:
            srch(d,-INF,INF,0)
        except Cut:
            bm=BM or bm
            break
        if not BM:
            break
        bm=BM
        if N>BU:
            break
        d+=1
    return bm
def uci(m):
    f=m&127;t=m>>7&127;u='abcdefgh'[f&7]+str(1+(f>>4))+'abcdefgh'[t&7]+str(1+(t>>4));c=m>>14;return u+('nbrq'[c-1]if 0<c<5 else'')
def pick2(g):
    global GID
    if g.get('game')!=GID:
        GID=g.get('game');GS.clear();TT[:]=[None]*(MSK+1);K1[:]=[0]*128;K2[:]=[0]*128;HH[:]=[0]*16384
    setpos(g['fen']);GS.add(H);m=best();L=g.get('legal_moves')or[]
    if L and uci(m)not in L:
        setpos(g['fen']);m=0
        for x in gen(0):
            if uci(x)in L:
                m=x;break
    return m
def post(path,body):
    req=urllib.request.Request(ENV_URL+path,data=json.dumps(body).encode(),headers={'content-type':'application/json'})
    with urllib.request.urlopen(req)as r:
        return json.load(r)
ENV_URL=os.environ['MAKEFUN_ENV_URL'];g=post('/game',{})
while g.get('status')!='done':
    while g.get('status')=='your_move':
        g=post('/move',{'game':g['game'],'move':uci(pick2(g))})
    g=post('/game',{})
