def encode(message):
    
    #Remove pass and write your logic her
    message_list=list(message)
    enc_str=""
    counter=1
    for i in range (len(message_list)-1):
        if(message_list[i]==message_list[i+1]):
            counter+=1
            if i==len(message_list)-2:
                enc_str+=str(counter)+message_list[i]
        else:
            print(counter,message_list[i])
            temp=str(counter)
            enc_str=enc_str+temp+message_list[i]
            counter=1
            if i==len(message_list)-2:
                enc_str+=str(counter)+message_list[i+1]

    return(enc_str)        
#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
