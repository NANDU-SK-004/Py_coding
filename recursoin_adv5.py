class Solution:
    def solve(self ,index ,flag ,number,result):
        if index >=len(number):
            result.append("".join(number))  #we use join bcz the array will be in form like example ["1","0","1"] so join 
            return
        number[index] ="0"
        self.solve(index +1 ,True ,number,result)
        if flag == True:
            number[index]="1"
            self.solve(index +1 ,False,number,result)
            number[index]="0"



    def GenerateBinaryString(self ,n):
        number =["0"]*n
        result =[]
        self.solve(0,  True   ,  number,result)
        return result
s =Solution()
print  ( s.GenerateBinaryString(3))