#iterative control
#-> Entry check loop (for , while)
#-> Exit check loop (not supported in python)

# for loop
for i in range(1,5,1):
    print("hi")

for i in range(1,6,1):
    print(i)

#for i in range(1,6,1):
    #print(i,end=" ")

for i in range(5,0,-1):
    print(i)

'''
i	i<5	block	i=i+1
i=1	1<5 -> T	hi	i=1+1
i=2	2<5 ->T	hi	i=2+1
i=3	3<5 ->T	hi	i=3+1
i=4	4<5 ->T	hi	i=4+1
i=5	5<5 -> F		

'''
