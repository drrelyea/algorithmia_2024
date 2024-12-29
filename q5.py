# %%
with open("everybody_codes_e2024_q05_p1.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

import numpy as np

# from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

# grid = {
#     i + j * 1j: 1 if c == "#" else 0
#     for i, r in enumerate(data)
#     for j, c in enumerate(r)
# }


# %%
themin = min([int(x) for x in data])
strokes = sum([int(x) - themin for x in data])
print(strokes)


# %%
with open("everybody_codes_e2024_q05_p2.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

# import numpy as np

# from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

# grid = {
#     i + j * 1j: 1 if c == "#" else 0
#     for i, r in enumerate(data)
#     for j, c in enumerate(r)
# }


# %%

themed = np.median([int(x) for x in data])
strokes = sum([abs(int(x) - themed) for x in data])
print(strokes)

# %%
with open("everybody_codes_e2024_q05_p3.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)

# import numpy as np

# from utils import data_to_numpy, get_indices_from_numpy, load_advent_of_code

# grid = {
#     i + j * 1j: 1 if c == "#" else 0
#     for i, r in enumerate(data)
#     for j, c in enumerate(r)
# }


# %%
