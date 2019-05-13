def find_common_characters(msg1,msg2):
     #Remove pass and write your logic here
    list1=[]
    list2=[]
    join=""
    for m1 in msg1:
        for m2 in msg2:
            if m1==m2:
                list1.append(m1)
    for alpha in list1:
        if alpha not in list2 and alpha!=" ":
            list2.append(alpha)
    if list2==[]:
        join=-1
    else:
        for final in list2:
            join=join+final
            
    return join

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
