my_file=open("fileq_3.txt")
file1=open("delhi.txt","w")
file2=open("shimla.txt","w")
file3=open("other.txt","w")
for data in my_file:
    if "delhi" in data:
        file1.write(data)
    elif "shimla " in data:
        file2.write(data)
    elif "jaipur" in data:
        file3.write(data)
file1.close()