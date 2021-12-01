with open("input.txt") as f:
    A = []
    increases = 0
    
    for line in f:
        A.append(int(line.strip()))
        
    prev = A[0]+A[1]+A[2]
    for i in range(0, len(A)-2):
        B = A[i]+A[i+1]+A[i+2]
        if B > prev:
            increases += 1
        prev = B
print(increases)