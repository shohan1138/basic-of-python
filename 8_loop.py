# any loop starts from 0
#any loop steps =1 by default
#n is times of looping
#limit always n-1.for ex. = 5-1=4 (0-1-2-3-4) 
# % (mopdulas) reminder of math
sum_odd =0
sum_even =0
for i in range(1,11,2):  #for 1 in range(1,5,2): loop start from 1 not 0||5 is end range and 2 is step
    print("the value of i:",i) 
for o in range(1,11):
    if(o%2==1):
        sum_odd =sum_odd +o
        print(o,"is a odd number")
    else:
        sum_even =sum_even +o

        print(o,"is a even number")
    
print("the sum of all odd numbers:",sum_odd)
print("the sum of all even numbers:",sum_even)
