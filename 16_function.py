#function is 2 type
# build in function/method
#user defined function



def sum(x,y):
    sum =x+y
    return(sum)
a=10
b=20
result = sum(a,b)
print(result)


#declare global variable inside the function
my_list=[]

def create_first_line():
    global my_list

    two_d_list=[[1,2,3],[2,3,4],[3,4,5]]

    my_list =[item for sublist in two_d_list for item in sublist]

create_first_line()
print("flattened list:",my_list)

##lambda function
#normal function
def square(x):
    return x**2
#lambda function 
square_lambda=lambda x:x**2

print(square(3))
print(square_lambda(3))

add =lambda a,b:a+b
print(add(10,20))

name=["Alice","Leah","Charlie"]
name.sort(key=lambda x:len(x))
print(name)
