#Tuples are ordered, immutable collections.
'''
# Accessing elements
print("First:", t1[0])
print("Slice:", t1[1:4])

# Concatenation and repetition
t4 = (6,7,8)
print("Concat:", t1 + t4)
print("Repeat:", t2 * 2)

a = "mounika"
print(tuple(a))

details = ('Id001','Mounika','Python','Java','Need Placement','9384540000')
ID,NAME,COURSE,A_COURSE,PLACEMENT,PHONE_NUM = details
print(f"""
ID        :{ID},
NAME      :{NAME},
COURSE    :{COURSE},
A_COURSE  :{A_COURSE},
PLACEMENT :{PLACEMENT},
PHONE_NUM :{PHONE_NUM}
""")
#Sets are unordered, mutable, and contain unique elements

x = {1,7,9,3}
y = {2,17,24}
print(x)
x.add(3)
print(x)
print(y)
y.update([2,25,36,17,23,24])
print(y)
x.remove(369)
x.discard(369)
print(x)
x.pop()
print(x)
'''
s1 = {1,2,3,4}
s2 = {2,4,6,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
