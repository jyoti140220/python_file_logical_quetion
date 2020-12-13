list=[2,4,6,8,23,67]
i=-1
count=0
while True:
    if list[0]==list[i]:
        break
    count=count+1
    i=i-1
print(count+1)