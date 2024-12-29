# %%
with open("everybody_codes_e2024_q03_p1.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

import numpy as np

from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

grid = {
    i + j * 1j: 1 if c == "#" else 0
    for i, r in enumerate(data)
    for j, c in enumerate(r)
}


# %%
def remove_pieces(arr):
    new_arr = dict()
    changed = False
    for cell, value in arr.items():
        if (
            value > 0
            and arr.get(cell - 1, -1) == value
            and arr.get(cell + 1, -1) == value
            and arr.get(cell + 1j, -1) == value
            and arr.get(cell - 1j, -1) == value
        ):
            new_arr[cell] = value + 1
            changed = True
        else:
            new_arr[cell] = value
    return changed, new_arr


changed = True
new_grid = grid.copy()
while changed:
    changed, new_grid = remove_pieces(new_grid)

print(sum(ii for ii in new_grid.values()))
# %%
with open("everybody_codes_e2024_q03_p2.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

import numpy as np

from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

grid = {
    i + j * 1j: 1 if c == "#" else 0
    for i, r in enumerate(data)
    for j, c in enumerate(r)
}


# %%
def remove_pieces(arr):
    new_arr = dict()
    changed = False
    for cell, value in arr.items():
        if (
            value > 0
            and arr.get(cell - 1, -1) == value
            and arr.get(cell + 1, -1) == value
            and arr.get(cell + 1j, -1) == value
            and arr.get(cell - 1j, -1) == value
        ):
            new_arr[cell] = value + 1
            changed = True
        else:
            new_arr[cell] = value
    return changed, new_arr


changed = True
new_grid = grid.copy()
while changed:
    changed, new_grid = remove_pieces(new_grid)

print(sum(ii for ii in new_grid.values()))

# %%
with open("everybody_codes_e2024_q03_p3.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

import numpy as np

from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

grid = {
    i + j * 1j: 1 if c == "#" else 0
    for i, r in enumerate(data)
    for j, c in enumerate(r)
}


# %%
def remove_pieces(arr):
    new_arr = dict()
    changed = False
    for cell, value in arr.items():
        if (
            value > 0
            and arr.get(cell - 1, -1) == value
            and arr.get(cell + 1, -1) == value
            and arr.get(cell + 1j, -1) == value
            and arr.get(cell - 1j, -1) == value
            and arr.get(cell - 1 - 1j, -1) == value
            and arr.get(cell + 1 - 1j, -1) == value
            and arr.get(cell - 1 + 1j, -1) == value
            and arr.get(cell + 1 + 1j, -1) == value
        ):
            new_arr[cell] = value + 1
            changed = True
        else:
            new_arr[cell] = value
    return changed, new_arr


changed = True
new_grid = grid.copy()
while changed:
    changed, new_grid = remove_pieces(new_grid)

print(sum(ii for ii in new_grid.values()))

# %%
