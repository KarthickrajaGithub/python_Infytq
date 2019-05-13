def calculate(distance,no_of_passengers):
    
    #Remove pass and write your logic here
    Price_per_litre = 70
    Mileage_of_bus = 10
    Price_per_ticket = 80
    Total_cost_bus=(distance/Mileage_of_bus)*Price_per_litre
    Total_cost_Passengers=no_of_passengers*Price_per_ticket
    profit=Total_cost_Passengers-Total_cost_bus
    loss= -1
    if(Total_cost_Passengers>Total_cost_bus):
        return(profit)
    else:
        return(loss)
    



#Provide different values for distance, no_of_passenger and test your program
distance=100
no_of_passengers=10
print(calculate(distance,no_of_passengers))
