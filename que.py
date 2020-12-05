f=open("quetion.txt","r")
a=[]
for x in f:
    n=x.split()
    a.append(n)
y=a
w=open("delhi.txt","w")
i=0
p=" "
while i<len(y):
    if y[i][-1]=="delhi":
        p=w.write(y[i])
    i=i+1
w.close()
f.close()
