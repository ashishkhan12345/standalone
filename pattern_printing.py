for i in range(1, 7):
    for j in range(0,i):
        print(i,end= " ")
    print("")
rows = 5


for i in range(1, rows):
    # nested loop for each column
    for j in range(1, i + 1):
        print(j, end=' ')
        # new line after each row
    print(" ")


# for stars half parymid-
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
        # new line after each row
    print(" ")