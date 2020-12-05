s=open("pepole.txt","w")
a= ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(a):
    p=s.write(a[i])
    p=s.write("\n")
    i=i+1
s.close()
