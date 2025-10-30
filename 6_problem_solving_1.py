cake_1="black forest"
cake_2="vanila cake"
cake_3="red velvet"
cake_4="lemon spange"
cake_5="chocolate cake"

print("here is the all cake names:",cake_1,cake_2,cake_3,cake_4,cake_5)

#material cost for each cake
material_cost_cake_1 = 180
material_cost_cake_2 = 700
material_cost_cake_3 = 220
material_cost_cake_4 = 777
material_cost_cake_5 = 170

#transportation cost
transportation_cost = 150

#total cost of material and transportation
material_tranportation_cost_cake_1 = material_cost_cake_1 + transportation_cost
material_tranportation_cost_cake_2 = material_cost_cake_2 + transportation_cost
material_tranportation_cost_cake_3 = material_cost_cake_3 + transportation_cost
material_tranportation_cost_cake_4 = material_cost_cake_4 + transportation_cost
material_tranportation_cost_cake_5 = material_cost_cake_5 + transportation_cost

print("material tranportation cost black forest",material_tranportation_cost_cake_1)
print("material tranportation cost vaniala cake",material_tranportation_cost_cake_2)
print("material tranportation cost red velvet",material_tranportation_cost_cake_3)
print("material tranportation cost lemon spange",material_tranportation_cost_cake_4)
print("material tranportation cost chocolate cake",material_tranportation_cost_cake_5)

#utility cost per pound
utility_cost_cake_1 =(material_tranportation_cost_cake_1*3)/100
utility_cost_cake_2 =(material_tranportation_cost_cake_2*3)/100
utility_cost_cake_3 =(material_tranportation_cost_cake_3*3)/100
utility_cost_cake_4 =(material_tranportation_cost_cake_4*3)/100
utility_cost_cake_5 =(material_tranportation_cost_cake_5*3)/100

print("utility cost for black forest",utility_cost_cake_1)
print("utility cost for vaniala cake",utility_cost_cake_2)
print("utility cost for red velvet",utility_cost_cake_3)
print("utility cost for lemon spange",utility_cost_cake_4)
print("utility cost for chocolate cake",utility_cost_cake_5)

#space cost & staff cost per pound
space_cost = 50
staff_cost = 60

#total cost
total_inventory_cost_cake_1=material_tranportation_cost_cake_1 + utility_cost_cake_1 + space_cost + staff_cost
total_inventory_cost_cake_2=material_tranportation_cost_cake_2 + utility_cost_cake_2 + space_cost + staff_cost
total_inventory_cost_cake_3=material_tranportation_cost_cake_3 + utility_cost_cake_3 + space_cost + staff_cost
total_inventory_cost_cake_4=material_tranportation_cost_cake_4 + utility_cost_cake_4 + space_cost + staff_cost
total_inventory_cost_cake_5=material_tranportation_cost_cake_5 + utility_cost_cake_5 + space_cost + staff_cost

print("total cost of black forest per pound",total_inventory_cost_cake_1)
print("total cost of vaniala cake per pound",total_inventory_cost_cake_2)
print("total cost of red velvet per pound",total_inventory_cost_cake_3)
print("total cost of lemon spange per pound",total_inventory_cost_cake_4)
print("total cost of chocolate cake per pound",total_inventory_cost_cake_5)

#Assignment_1_problem_solving_1

#3.Selling price for all cakes
Selling_price_for_cake_1 = 780
Selling_price_for_cake_2 = 600
Selling_price_for_cake_3 = 800
Selling_price_for_cake_4 = 650
Selling_price_for_cake_5 = 660

print("Selling price for Black Forest:",Selling_price_for_cake_1)
print("Selling price for vanila cake:",Selling_price_for_cake_2)
print("Selling price for red velvet:",Selling_price_for_cake_3)
print("Selling price for lemon spange:",Selling_price_for_cake_4)
print("Selling price for chocolate cake:",Selling_price_for_cake_5)

#4.Selling price with Discount

discount_price_for_cake_1=Selling_price_for_cake_1-((Selling_price_for_cake_1*5)/100)
discount_price_for_cake_2=Selling_price_for_cake_2-((Selling_price_for_cake_2*5)/100)
discount_price_for_cake_3=Selling_price_for_cake_3-((Selling_price_for_cake_3*5)/100)
discount_price_for_cake_4=Selling_price_for_cake_4-((Selling_price_for_cake_4*7)/100)
discount_price_for_cake_5=Selling_price_for_cake_5-((Selling_price_for_cake_5*7)/100)

print("Selling price With discount for black forest",discount_price_for_cake_1)
print("Selling price With discount for vanila cake",discount_price_for_cake_2)
print("Selling price With discount for red velvet",discount_price_for_cake_3)
print("Selling price With discount for lemon spange",discount_price_for_cake_4)
print("Selling price With discount for chocolate cake",discount_price_for_cake_5)

#5. selling Profit After for each Cake
profit_from_cake_1=discount_price_for_cake_1 - total_inventory_cost_cake_1
profit_from_cake_2=discount_price_for_cake_2 - total_inventory_cost_cake_2
profit_from_cake_3=discount_price_for_cake_3 - total_inventory_cost_cake_3
profit_from_cake_4=discount_price_for_cake_4 - total_inventory_cost_cake_4
profit_from_cake_5=discount_price_for_cake_5 - total_inventory_cost_cake_5

print("Profit after selling black forest per pound",profit_from_cake_1)
print("Profit after selling vanila cake per pound",profit_from_cake_2)
print("Profit after selling red velvet per pound",profit_from_cake_3)
print("Profit after selling lemon spange per pound",profit_from_cake_4)
print("Profit after selling chocolate cake per pound",profit_from_cake_5)

#selling Profit After for each Cake percentage
if total_inventory_cost_cake_1<=discount_price_for_cake_1:
    percentage_profit_after_selling_cake_1 = (total_inventory_cost_cake_1/discount_price_for_cake_1)*100

    print("Percentage profit Selling black forest",percentage_profit_after_selling_cake_1)

elif total_inventory_cost_cake_1<=discount_price_for_cake_1:
    percentage_profit_after_selling_cake_1 = (discount_price_for_cake_1/total_inventory_cost_cake_1)*100

    print("Percentage loss Selling black forest",percentage_profit_after_selling_cake_1)

if total_inventory_cost_cake_2<=discount_price_for_cake_2:
    percentage_profit_after_selling_cake_2 = (total_inventory_cost_cake_2/discount_price_for_cake_2)*100

    print("Percentage profit Selling vanila cake",percentage_profit_after_selling_cake_2)

elif total_inventory_cost_cake_2<=discount_price_for_cake_2:
    percentage_profit_after_selling_cake_2 = (discount_price_for_cake_2/total_inventory_cost_cake_2)*100

    print("Percentage loss Selling vanila cake",percentage_profit_after_selling_cake_2)

if total_inventory_cost_cake_3<=discount_price_for_cake_3:
    percentage_profit_after_selling_cake_3 = (total_inventory_cost_cake_3/discount_price_for_cake_3)*100

    print("Percentage profit Selling red velvet",percentage_profit_after_selling_cake_3)

elif total_inventory_cost_cake_3<=discount_price_for_cake_3:
    percentage_profit_after_selling_cake_3 = (discount_price_for_cake_3/total_inventory_cost_cake_3)*100

    print("Percentage loss Selling red velvet",percentage_profit_after_selling_cake_3)

if total_inventory_cost_cake_4<=discount_price_for_cake_4:
    percentage_profit_after_selling_cake_4 = (total_inventory_cost_cake_4/discount_price_for_cake_4)*100

    print("Percentage profit Selling lemon spange",percentage_profit_after_selling_cake_4)

elif discount_price_for_cake_4<total_inventory_cost_cake_4:
    percentage_loss_after_selling_cake_4 = (discount_price_for_cake_4/total_inventory_cost_cake_4)*100

    print("Percentage loss after Selling lemon spange",percentage_loss_after_selling_cake_4)

if total_inventory_cost_cake_5<=discount_price_for_cake_5:
    percentage_profit_after_selling_cake_5 = (total_inventory_cost_cake_5/discount_price_for_cake_5)*100

    print("Percentage profit Selling chocolate cake",percentage_profit_after_selling_cake_5)


elif total_inventory_cost_cake_5<=discount_price_for_cake_5:
    percentage_profit_after_selling_cake_5 = (discount_price_for_cake_5/total_inventory_cost_cake_5)*100

    print("Percentage loss Selling chocolate cake",percentage_profit_after_selling_cake_5)

