def calculate_commission(barrels_sold, barrel_price):
    if barrels_sold > 100:
        commission_rate = 0.40
    elif 90 >= barrels_sold >=51:
        commission_rate = 0.20
    elif barrels_sold <= 50:
        commission_rate = 0.15
    else:
        commission_rate = 0.20
    
    commission = barrels_sold * barrel_price * commission_rate
    return commission 
    
barrel_price = float(input("Enter the price of one barrel: Rs."))
barrels_sold = int(input("Enter the number of barrels sold during the month: "))
commission = calculate_commission(barrels_sold, barrel_price)
print(f"The commission for selling {barrels_sold} barrels is: Rs. {commission:.2f}")
