'''
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

s1 = {1,2,3,4}
s2 = {2,4,6,8}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1.difference(s2))
print(s1)

print(s2.difference(s1))
print(s2)

s1.difference_update(s2)
print(s1,s2)

s1 = {1,2,3,4}
s2.difference_update(s1)
print(s1,s2)

s1 = {1,2,3,4}
s2 = {2,4,6,8}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1,s2)

x = {1,2,3,4}
y = {5,6,7,8}
print(x.isdisjoint(y))

parentSet = {1,2,3,4,5,6,7,8,9,0}
childSet = {1,2,3}
print(parentSet.issuperset(childSet))
print(childSet.issubset(parentSet))

x.clear()
print(x)
'''

#Dictionaries are key-value pairs, mutable and unordered

d = {"Live001":"Live@123","Live002":"Live@456","Live003":"Live@789"}
print(d)

d1 = {}
print(d1)

print(d["Live001"])
print(d.get("Live001"))

d.pop("Live001")
print(d)

d["Live002"]="Live@123"
print(d)

d.update({"Live001":"Live@123","Live004":"Live@321"})
print(d)

print(d.keys())
print(d.values())
print(d.items())

for i in d:
    print("Username :",i,",Password :",d[i])


course = {"AI Developer":{"Duration":"360Hrs","Tools Covered":"Python,DS,DA,ML,DL,SQL,R,C,AI","Projects":"9 Projects"},
          "Python Full Stack":{"Duration":"180Hrs","Tools Covered":"Python,WD,SQL,C,Django","Projects":"9 Projects"},
          "Java Full Stack":{"Duration":"180Hrs","Tools Covered":"Java,WD,SQL,C,SpringBoot","Projects":"9 Projects"}}
print(course["AI Developer"]["Duration"])
print(course["Python Full Stack"]["Projects"])



