list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    sum=0
    count=0
    for i in range(len(list_of_marks)):
        sum=sum+list_of_marks[i]
        average = sum/10
    i=0 
    while(i<len(list_of_marks)):
            if(average<list_of_marks[i]):
                count+=1 
            i+=1    
    percentage = (count)*10
    return(percentage)
    
    
        
def sort_marks():
    list_marks=[]
    list_marks=list(list_of_marks)
    list_marks.sort()
    return(list_marks)

def generate_frequency():
    d=[]
    for j in range (0,26):
        d.append(0)
    k=0 
    while(k<=25):
        count=0 
        for m in range(0,len(list_of_marks)):
            if(list_of_marks[m]==k):
                count+=1
            d[k]=count
        k+=1
    return(d)

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
