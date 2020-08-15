length = 0

numb = 1
index = 1
no =0
while index<=6:
    numb=1
    while numb<=6:
        length+=abs(numb-index)
        no+=1
        numb+=1
    index+=1
print("Total length is: ",length)
print("Total number of mappings: ",no)
print("The average distance is ",length/no)