# calculate number of hosts from IP blocks

total = 0
f = open('cidr','r')
for i in f:
    if i == 1:
        total = total + 2147483648
    elif i == 2:
        total = total + 1073741824
    elif i == 3:
        total = total + 536870912
    elif i == 4:
        total = total + 268435456
    elif i == 5:
        total = total + 134217728
    elif i == 6:
        total = total + 67108864
    elif i == 7:
        total = total + 33554432
    elif i == 8:
        total = total + 16777216
    elif i == 9:
        total = total + 8388608
    elif i == 10:
        total = total + 4194304
    elif i == 11:
        total = total + 2097152
    elif i == 12:
        total = total + 1048576
    elif i == 13:
        total = total + 524288
    elif i == 14:
        total = total + 262144
    elif i == 15:
        total = total + 131072
    elif i == 16:
        total = total + 65536
    elif i == 17:
        total = total + 32768
    elif i == 18:
        total = total + 16384
    elif i == 19:
        total = total + 8192
    elif i == 20:
        total = total + 4096
    elif i == 21:
        total = total + 2048
    elif i == 22:
        total = total + 1024
    elif i == 23:
        total = total + 512
    elif i == 24:
        total = total + 256
    elif i == 25:
        total = total + 128
    elif i == 26:
        total = total + 64
    elif i == 27:
        total = total + 32
    elif i == 28:
        total = total + 16
    elif i == 29:
        total = total + 8
    elif i == 30:
        total = total + 4
    elif i == 31:
        total = total + 2
    elif i == 32:
        total = total + 1

print(total)
f.close()  
