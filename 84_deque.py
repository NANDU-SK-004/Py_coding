from collections import deque

lst =deque([])

lst.append(199)
lst.append(45)
lst.append(56)
lst.append(256)
lst.appendleft(5)
lst.pop()
print(lst[0])


