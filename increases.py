with open("input.txt") as f:
    A = []
    prev = 0
    increases = 0
    for line in f:
        A.append(int(line.strip()))
    for i in range(0, len(A)-2):
        if prev == 0:
            prev = A[0]+A[1]+A[2]
        else:
            B = A[i]+A[i+1]+A[i+2]
            if B > prev:
                increases += 1
            prev = B
print(increases)