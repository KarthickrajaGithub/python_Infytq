child_id=(10,20,30,40,50)
chocolates_received=[12,5,3,4,6]

def calculate_total_chocolates():
    
    #Remove pass and write your logic here to find and return the total number of chocolates
    sum=0
    for i in range(len(chocolates_received)):
        sum=sum+chocolates_received[i]
    return(sum)

def reward_child(child_id_rewarded,extra_chocolates):
    
    if (extra_chocolates>=1):
        for i in range(len(child_id)):
            if (child_id[i]==child_id_rewarded):
                chocolates_received[i]=chocolates_received[i]+extra_chocolates
                print(chocolates_received[i])   
    else:
        print("Extra chocolates in less than one")
        
        if child_id[i] not in child_id :
            print("Child ID is invalid")

    return(chocolates_received[i])   
    

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("Extra chocolates is less than 1")
    #print("Child id is invalid")
    #print(chocolates_received)


print(calculate_total_chocolates())
#Test your code by passing different values for child_id_rewarded,extra_chocolates
reward_child(20,2)
