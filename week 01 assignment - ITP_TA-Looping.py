i = int(input("number of star:"))

for x in range (0,i):   #to do a looping for x from 0 to i
    print ("*"*(x+1))   #to print the stars as much as x #left angle

print ()

for z in range (0,i+1):     #to do a looping for z from 0 to i+1
    print (" "*(i-z),"*"*z)   #to print the space as much as i-z then print star as much as z # #right angle

print ()

for y in range (i,0,-1):    #to do a looping for y from 0 to i reversely
    print ("*"*y)    #print star as much as y #rvsleft angle

print ()

for a in range (i,0,-1):    #to do a looping for a from 0 to i reversely
    print (" "*(i-a),"*"*a)    #print space as much as i-a then print star as much as a #rvsright angle

print ()

for b in range (0,i):   #to do a looping for b from 0 to i
    for c in range (0,i-b): #to do a looping for c from 0 to i-b inside b looping
        print(" ",end=" ")  #print space for c

    for d in range (0,b*2+1):   #to do a looping for d from 0 to b*2+1 inside b looping
        print("*",end=" ")  #print star for d looping then print space for d looping
    print()     #pyramid

print()

for e in range (0,i):   #to do a looping for e from 0 to i
    for f in range (0,i-e): #to do a looping for f from 0 to i-e inside e looping
        print(" ",end=" ")  #print space for f

    for g in range (0,e*2+1):   #to do a looping for g from 0 to e*2+1 inside b looping
        print("*",end=" ")  #print star for g looping then print space for g looping
    print()
for h in range (i,-1,-1): #to do a looping for h from -1 to i reversely
    for j in range (0,i-h): #to do a looping for j from o to i-h inside h looping
        print(" ",end=" ")  #print space for j looping

    for k in range (0,h*2+1):   #to do a looping for k from 0 to h*2+1 inside h looping
        print("*",end=" ")  #print star for k looping then space
    print()     #diamond
