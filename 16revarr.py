def revar(num ,left ,right):
    if left >= right:
        return 
    num[left] ,num[right] = num[right] ,num[left]
    revar(num,left +1 ,right -1)

num =[1 ,2 ,34 ,5 ,6 ,7 ,4,56 ,5 ,54]
revar(num ,0 ,len(num) - 1)

print(num)