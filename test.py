# calculate number of hosts from IP blocks

total = 0
f = open('cidr','r')
for i in f:
    if total == 0:
        print (i)