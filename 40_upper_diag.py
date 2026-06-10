nums=[[5 ,10 ,8],[7 ,6 ,3],[2 ,1 ,9]]

for i in range (0 ,len(nums)):
    for j in range (0 ,len(nums[0])):
        if i>j :
            print ("*" , end='      ')
        else :
            print(nums[i][j],end ='     ')
    print("\n")