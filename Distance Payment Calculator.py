def num(taxi,distance):
    print("Taxi Number : ",taxi)
    print("Distance Covered : ",distance)
    
    if distance <= 5:
        return("amount: 100 ")
    elif distance <= 10:
        val=distance-5
        return("amount:",val*10+100)
    elif distance <= 20 :
        val=distance-15
        return(val*8+200)
    elif distance >25:
        val= distance -25
        return(val*5+280)
taxi=input("Enter the Taxi Number:")
distance=int(input("Enter the distance :"))
res=num(taxi,distance)
print(res)