# n =[4888,-1,-234,7,4,5,676,5444,44]

# largest =float("-inf")
# s_largest=float("-inf")

# for i  in n:
#     largest = max(largest ,i)

# for i in n:
#     if i > s_largest and i < largest:
#         s_largest = i
# print(s_largest)

n =[48,-1,-234,7,4,5,676,5444,44]

largest =float("-inf")
s_largest=float("-inf")

for i  in n:
    if i > largest:
        s_largest =largest
        largest = i

    elif i > s_largest and i != largest:
        s_largest =i

print(s_largest)
        