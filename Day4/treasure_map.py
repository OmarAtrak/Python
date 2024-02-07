line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()

cols = ["A", "B", "C"]
col = cols.index(position[0])
row = int(position[1]) - 1

map[row][col] = "X"

print(f"{line1}\n{line2}\n{line3}")