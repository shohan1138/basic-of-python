demo_variable = [[1,2,3],[2,3,4],[3,4,1]]
#row and colomn index start from 0

print(demo_variable[1][1])#[row index][colomn index]
print(len(demo_variable[0]))

for i in range(5):  #parent loop is row
    for j in range(5): #child loop is colomn
        print(i,j) 

for row in range(len(demo_variable)):
    for col in range(len(demo_variable)):
        print(demo_variable[row][col])

for row in demo_variable:
    print(row)
    for col in row:
        print(col)