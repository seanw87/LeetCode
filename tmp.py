import itertools

tmp_str = "abcdefg"
res = [(tmp_str[i: i + 3]) for i in range(0, len(tmp_str), 3)]
print(res)

print()
tmp_str = "abc"
print(tmp_str[0:len(tmp_str) - 1])

print()
tmp_str = "abc"
print(tmp_str[1])

# tmp_str1 = ""
# print(tmp_str1[0])


print()
tmp_str = "abcd"
print(tmp_str[1:])

# prove: range is faster than enumerate
# t1:  1699047338499
# t2:  1699047340203 variance:  1704
# t3:  1699047341470 variance:  1267
# import time
# t = time.time()
# test_txt = "A"*10000000
# tmp_val = 0
# t1 = int(round(t * 1000))    #毫秒级时间戳
# print("t1: ", t1)
# for k, v in enumerate(test_txt):
#     tmp_val += 1
# t = time.time()
# t2 = int(round(t * 1000))    #毫秒级时间戳
# print("t2: ", t2, "variance: ", t2 - t1)
# tmp_val = 0
# for k in range(len(test_txt)):
#     tmp_val += 1
# t = time.time()
# t3 = int(round(t * 1000))    #毫秒级时间戳
# print("t3: ", t3, "variance: ", t3 - t2)


print()
tmp_str = "abcdefg"
print(tmp_str[:3])

print()
tmp_list = [1, 2, 3, 4, 5, 6]
for i in range(len(tmp_list), 0, -1):
    print(i, tmp_list[i - 1])
print(str(tmp_list))

print()
print("	".encode("UTF-8"))

print()
print('1'.isnumeric())

print()
fruits = ['apple', 'banana', 'cherry']
print(fruits.pop(-1))

print()
num_list = [1, 2, 3, 4, 5, 6]
for num in num_list:
    if num == 1:
        num_list.pop(0)
    print(num, num_list)
print(num_list.pop(-1))
print(num_list.pop())  # pop() == pop(-1)
"""
1 [2, 3, 4, 5, 6]
3 [2, 3, 4, 5, 6]
4 [2, 3, 4, 5, 6]
5 [2, 3, 4, 5, 6]
6 [2, 3, 4, 5, 6]
"""

print()
num_list = [1, 2, 3, 4, 5, 6]
print(num_list[2:])
print(num_list[2:-1])

print()
print(len(set('abcabc')))

print()


class tmp:
    def __init__(self, val=0):
        self.val = val


b = tmp(1)
a = b
print(a, b, a.val, b.val)
a.val = 5
print(a, b, a.val, b.val)


class tmp2:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a1 = tmp2(val=1, next=tmp2(val=2, next=tmp2(val=3, next=tmp2(val=4, next=tmp2(val=5, next=tmp2(val=6, next=None))))))

prev = None
for i in range(3):
    print("i: ", i)
    cur = a1
    a1 = a1.next
    cur.next = prev
    prev = cur

while prev:
    print(prev.val, a1.val)
    prev = prev.next
    a1 = a1.next

# print(prev.val, prev.next.val, prev.next.next.val, a1.val, a1.next.val)


print()
import math

print(math.gcd(12, 4), math.lcm(12, 4))

print()
inputString = "abcedfg"
# Using Extended Slicing to reverse a string
print(inputString[::-1])

print()
# Python 3.7+ or CPython 3.6
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
res = {k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)}
# or
res = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))  # sort by key: item[0]
print(res)
#
import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)


# Unpacking
def fun(a, b, c, d):
    print(a, b, c, d)


my_list = [1, 2, 3, 4]
# Unpacking list into four arguments
fun(*my_list)

print()
from collections import ChainMap

defaults = {'color': 'red', 'user': 'guest'}
usermap = {'color': 'yellow', 'user': 'admin'}

combined = ChainMap(usermap, defaults)
print(combined['color'])  # yellow - left has higher priority
print(combined['user'])  # admin - left has higher priority

print()
from collections import Counter

c = Counter()  # a new, empty counter
c = Counter('gallahad')  # a new counter from an iterable
c = Counter({'red': 4, 'blue': 2})  # a new counter from a mapping
c = Counter(cats=4, dogs=8)  # a new counter from keyword args
print(c.values())

print()
contestants = {'Randy Orton': 'Red', 'Dwayne Johnson': 'Blue'}
contestants['Jhon Cena'] = 'Red'
contestants['Dave Bautista'] = 'Blue'
del contestants['Dwayne Johnson']
print(contestants)
# for python 3.7+ the output is {'Randy Orton': 'Red', 'Jhon Cena': 'Red', 'Dave Bautista': 'Blue'}


print()
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]
print(list1 == list2)

print()
x = 1


def add():
    global x
    x += 1
    print(x)


add()

print()


def dfs():
    count[0] += 1
    print(count)


count = [0]
dfs()

print()
print(1 + (1 > 2))

print()
from collections import deque

dq = deque([1, 2, 3, 4, 5])
print(sum(dq))


print()
x = [8, 2, 3, 4, 1, 5]
y = [6, 3, 7, 2, 1]
set_y = set(y)
# return the first common value in two lists
b = next((a for a in x if a in set_y), None)
print(b)


print()
print("3 % 2: ", 3 % 2,
      "\n3 // 2: ", 3 // 2,
      "\n3/2: ", 3/2,
      "\nmath.floor(3/2): ", math.floor(3/2),
      "\nmath.ceil(3/2): ", math.ceil(3/2))


print()
print(max([(1, 2), (2, 1)]))
# (2, 1)


print()
l = [1, 2, 3]
a = l.pop(0)
print(a, l)


print()
rooms = [[1, 2], [3, 4]]
visited = set([1])
to_visit = {0}
to_visit |= set(rooms[0])-visited
print("to_visit: ", to_visit)


print()
print(set(range(3)))


print()
x = [[0, 1], [2, 3]]
x.remove([2, 3])
y = [1, 2, 3]
y.remove(3)
print(x, y)


print()
print('------')
t = zip([[1, 2], [2, 3]], [4, 5])
for x, y in t:
    print(x, y)


print()
print(set(tuple([1, 2])))


print()
x, y = (1, 2)
print(x, y)


print()
tl = [1, 2, 3, 4, 5, 6, 7, 8]
print(tl[:2])
print(tl[::-1][:2][::-1], tl[-2:])
print(tl[2:3])
print(tl[:100], tl[-100:])
print(tl.pop())


print()
ml = ['a', 'b', 'c']
print([e + 'b' for e in ml])


print()
txt = ''
print(txt[1:])


print()
l1 = []
l2 = ['a', 'b', 'c']
print([e[0]+e[1] for e in list(itertools.product(l1, l2))])
