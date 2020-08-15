x=1
y1=1
x2=1
y2=1
max=6
length =0
no=0
while y1<=max:
    x1=1
    while x1<=max:
        y2=1
        while y2<=max:
            x2=1
            while x2<=max:
                length+=abs(x2-x1)+abs(y2-y1)
                no+=1
                x2+=1
            y2+=1
        x1+=1
    y1+=1

print("Total distance is: ",length)
print("Total number of mappings is: ",no)
print("Average length of all mappings is ",length/no)
