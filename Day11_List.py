#LIST -> Lists are ordered, mutable, and can contain duplicate items.

a = [1,2.34,"hi",'c',True,[12,23,34]]
print(a)

a = [1,2,3,4,5,1,2,3,4,5]
print(a) 
print(len(a))

print(a[0])
print(a[-1])
print(a[::-1])
print(a[2:6])
print(a[::2])
#print(a[10])
print(a[:])
print(a[:6])
print(a[0:])

# Adding an element in a list
a = [1,2,4]
a.append(5)
print(a)
a.extend([6,7,8,3])
print(a)
a.insert(2,3)
print(a)


# Delete an element
a.remove(3)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)

# update an element in a list
#a[0]="hi"
print(a)

# clear element in a list
#a.clear()
#print(a)

# delete an list permanently
#del a
#print(a)

#build-in functions of list
print(a.index(5))
print(a.count(5))
a=[1,7,2,4,6,27,8,9,91,1,2,4,5,5]
a.sort()
print(a)
a.reverse()
print(a)
b = a
#b = a.copy()
print(b)
a.insert(0,'hi')
print(a)
print(b)

#pre-defined functions for list

a = [1, 1, 2, 2, 4, 4, 5, 5, 6, 7, 8, 9, 27, 91]
print(list(reversed(a)))
print(min(a))
print(max(a))
print(sum(a))
print(sorted(a))
print(list((1,2,3)))
a= [[1,2],[3,4]]
print(a[0][1])
print("Comprehension:", [x**2 for x in range(5)])
print(list(range(5)))

#linear search
a = [1,6,2,7,3,4,8,3,4,2]
key = 7
for i in a:
    if i==key:
        print(a.index(i))

#binary search task

