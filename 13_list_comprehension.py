square_list = [i**2 for i in range(10)if i%2==0]

print(square_list)

# assignment convert 2d list to 1d list
two_D_list =[[1,2,3],[3,4],[5,3]]

one_d_list=[item for sublist in two_D_list for item in sublist]

print(one_d_list)