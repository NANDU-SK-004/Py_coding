
items =[]
def push1(item):
    items.append(item)

def pop1():
    if len(items) == 0:
        print("empty list")
        return
    x = items.pop()
    return x
    
def top1():
    if len(items) == 0:
        return None
    return items[-1]


s ="([{()}]"    

for i in range(0 ,len(s)):
    if s[i] == ")" and top1() =="(" :  pop1()
    elif s[i] == "]"  and   top1() == "[": pop1()
    elif s[i] == "}" and top1() == "{" :pop1()
    else :
        push1(s[i])
if len(items) == 0:
    print  ( "valid")
else:
    print( "invalid")
print(items)