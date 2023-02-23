# a=open("people.txt","x")

# a=open("people.txt","w")
# a.write("priyanka - shimla\n neela - delhi\nsashi - jaipur\nsarika - delhi\ndeepti - shimla\nnharshad - delhi\ntrishna - delhi\npradeep - jaipur\nsekhar - delhi\nnand - delhi\nanoop - delhi")
# a.close()


a=open("people.txt","r")
b=a.readlines()
print(b)
i=0
while i<len(b):
    if "delhi" not in b[i] and "shimla" not in b[i]:
        o=open("other.txt","a")
        o.write(b[i])
        # o.close()
    if"delhi" in b[i]:
        d=open("delhi.txt","a")
        d.write(b[i])
        # d.close()
    if "shimla" in b[i]:
        s=open("shimla.txt","a")
        s.write(b[i])
        # s.close()
    i+=1


# print(b)
# a.close()

# a=open("people.txt","a")
# b=a.write("\nsimi-delhi")
# a.close()

# d=open("delhi.txt","x")
# s=open("shimla.txt","x")
# o=open("other.txt","x")
