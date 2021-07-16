# Tuple of all position codes
pos_tuple = tuple()
for i in range(1, 9):
    for j in range(97, 105):
        pos_tuple += (f"{chr(j).lower()}{i}",)

# Relation (dictionary) between a position code and it's color
position_color_relation = {}
color = "black"
count = 0
for pos in pos_tuple:
    position_color_relation[pos] = color
    count += 1
    
    # If row is finished, set count to 0, else switch color
    if count == 8:
        count = 0
    else:
        if color == "black":
            color = "white"
        elif color == "white":
            color = "black"