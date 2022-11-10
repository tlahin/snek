
def walls(wall, snek_data):

    j = 0

    while j < wall.length:

        new_block = wall.cords[j].copy()
        for i in range(len(new_block)):
            new_block[i] += snek_data.block_size
        wall.cords.append(new_block)
        j += 1