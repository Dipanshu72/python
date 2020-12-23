l=None
s= None
while True:
    try:
        n=input(">")
        if n == "done":
          break
        ni=int(n)
        if l is None or ni>l:
            l=ni
        elif s is None or ni<s:
            s=ni
    except:
        print("Invalid input")
        continue
print("max is:", l)
print("min is:", s)