N, D, M, P = input().split()

N = int(N)
D = int(D)
M = int(M)
P = int(P)

total01 = N * D
total02 = M * P

if(total02) > (total01):
    print("BUFF")
elif (total01) > (total02):
    print("NERF")
