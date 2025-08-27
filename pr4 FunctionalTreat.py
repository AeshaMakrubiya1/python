
hub = {"mode":"1D","bag":[]}

def put():
    """input numbers, save in hub"""
    global hub
    t=input("1=1D 2=2D: ")
    if t=="2":
        r=int(input("rows: ")); g=[]
        for i in range(r):
            g.append([int(x) for x in input("row %d: " % (i+1)).split()])
        hub={"mode":"2D","bag":g}
    else:
        hub={"mode":"1D","bag":[int(x) for x in input("values: ").split()]}
    print("done")

def basics():
    """built-in stats"""
    if hub["mode"]=="1D":
        a=hub["bag"]; 
        if not a: print("no"); return
        print("len",len(a),"min",min(a),"max",max(a),"sum",sum(a),"avg",round(sum(a)/len(a),2))
    else:
        g=hub["bag"]; flat=[n for r in g for n in r]
        if not flat: print("no"); return
        print("total",len(flat),"min",min(flat),"max",max(flat),"sum",sum(flat))

def rec(n): 
    """factorial recursion demo"""
    return 1 if n<=1 else n*rec(n-1)

def rec_menu():
    k=int(input("n: ")); print("fact:",rec(k))

def lam_menu():
    """filter odd numbers using lambda, then map to (-1) power"""
    if hub["mode"]!="1D": print("need 1D"); return
    a=hub["bag"]; 
    if not a: print("no"); return
    kept=list(filter(lambda x:x%2==1,a))
    print("odds:",kept); print("negated:",list(map(lambda x:-x,kept)))

def back():
    """multi return values"""
    seq=hub["bag"] if hub["mode"]=="1D" else [n for r in hub["bag"] for n in r]
    if not seq: return None
    return min(seq),max(seq),sum(seq),sum(seq)/len(seq)

def ord():
    """sort either kind"""
    if hub["mode"]=="1D":
        a=hub["bag"]; rev=input("desc? y/n: ")=="y"; a.sort(reverse=rev); print(a)
    else:
        print("rows sorted:"); 
        for r in [sorted(r) for r in hub["bag"]]: print(r)

def star(*a,**k):
    """*args/**kwargs printer"""
    print("A:",a); print("K:",k)


def show_menu():
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Help: Function Docs")
    print("8. Exit Program")

def docer():
    for f in [put,basics,rec_menu,lam_menu,ord,back,star]:
        print(f.__name__,":",(f.__doc__ or "").strip())

while True:
    show_menu()
    ch=input("sel: ")
    if ch=="1": put()
    elif ch=="2": basics()
    elif ch=="3": rec_menu()
    elif ch=="4": lam_menu()
    elif ch=="5": ord()
    elif ch=="6":
        r=back()
        if r: mn,mx,sm,av=r; star(mn,mx,sm,round(av,2), minimum=mn, maximum=mx, total=sm, average=round(av,2))
        else: print("no data")
    elif ch=="7": docer()
    elif ch=="8": print("bye"); break
    else: print("bad")
