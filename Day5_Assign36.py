def create_largest_number(number_list):
    
    #remove pass and write your logic here
    count=0
    find_large=[]
    find_large=list(number_list)
    for i in range(0,3):
        temp=0
        temp=max(number_list)
        if temp not in find_large:
            find_large.append(temp)
        #number_list.remove(temp)
    
    find_large=find_large[::-1]        #Reversing the List  
    
    
    join=""
    for num in find_large:
        num=str(num)
        join=join+num
    join=int(join)
    return join
    
    
number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
