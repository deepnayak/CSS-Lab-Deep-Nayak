p=19
q=13
N=p*q

PHI=(p-1)*(q-1)
e=5
for d in range(1,100):
    if ((e*d % PHI)==1): break
print (e,N)

print (d,N)
M=4
cipher = M**e % N

print (cipher)
message = cipher**d % N
print (message)