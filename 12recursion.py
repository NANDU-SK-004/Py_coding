count =0

def name():
    global count
    if count == 4:
        return
    print("anupama")
    count +=1
    name() 
    
name()