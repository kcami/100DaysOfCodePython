# Dia 4 - 100DaysOfCodeChallenge
# Treasure Map

row1 = ['O', 'O', 'O']
row2 = ['O', 'O', 'O']
row3 = ['O', 'O', 'O']
map = [row1, row2, row3 ]

print(f"{row1}\n{row2}\n{row3}")
pos_column, pos_row = input("Where do you want to put the treasure? ")
map[int(pos_row) - 1][int(pos_column) - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")