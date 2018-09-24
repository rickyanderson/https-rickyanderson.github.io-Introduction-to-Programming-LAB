i = int(input("number of star:"))

for x in range (0,i):
    print ("*"*(x+1))   #left angle

print ()

for z in range (0,i+1):
    print (" "*(i-z),"*"*z)     #right angle

print ()

for y in range (i,0,-1):
    print ("*"*y)     #rvsleft angle

print ()

for a in range (i,0,-1):
    print (" "*(i-a),"*"*a)     #rvsright angle

print ()

for b in range (0,i):
    for c in range (0,i-b):
        print(" ",end=" ")

    for d in range (0,b*2+1):
        print("*",end=" ")
    print()     #pyramid

print()

for e in range (0,i):
    for f in range (0,i-e):
        print(" ",end=" ")

    for g in range (0,e*2+1):
        print("*",end=" ")
    print()
for h in range (i,-1,-1):
    for j in range (0,i-h):
        print(" ",end=" ")

    for k in range (0,h*2+1):
        print("*",end=" ")
    print()     #diamond
