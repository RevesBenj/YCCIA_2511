# -------------------------------------------------------
# Week6 - Activity 7  Lambda sorting
# # Author: Benjelyn Reves Patiag
# Date Created: 25-Jan- 2026
# -------------------------------------------------------
data = ['a5', 'a2', 'b1', 'b3', 'c2']  # list values

# sorted() use lambda to decide how sorting happen
sorted_data = sorted(
    data,
    # x[0] take letter, x[1:] take number and change to int
    key=lambda x: (x[0], int(x[1:]))  
)

print(sorted_data)  # print sorted result
