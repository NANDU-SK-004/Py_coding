nums =[3,5,3,4,5,7,4,6,2,8,9,10]
k = int(input("howmuch time need to rotate :"))

for i in range (k) :
    for i in range (-2 , -13 , -1):
        k=nums[i]
        nums[i] =nums[i+1]
        nums[i+1]=k

print(nums)