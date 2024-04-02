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
