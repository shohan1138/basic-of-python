name_of_the_day_in_week_1st_2_digit ='tu'
print ("enter the name of the day in week 1st 2 digits",name_of_the_day_in_week_1st_2_digit)
the_time_to_visit ='21' 
print("enter the time for arriving in 24 format(e.g.,03)",the_time_to_visit)
if(name_of_the_day_in_week_1st_2_digit==''or the_time_to_visit==''):
    print("Reservation must fulfill")
else:
    if(name_of_the_day_in_week_1st_2_digit=='mo'or'tu'or'we'or'th'or'fr'and the_time_to_visit<17):
        print("NO Discount")
    elif(name_of_the_day_in_week_1st_2_digit=='mo'or'tu'or'we'or'th'or'fr'and the_time_to_visit>17):
        print("10% Discount")
if:
    if(name_of_the_day_in_week_1st_2_digit=='sa'or'su'and the_time_to_visit<15):
        print("5% discount")
    elif(name_of_the_day_in_week_1st_2_digit=='sa''su' and the_time_to_visit>15):
        print("7% dicsount")