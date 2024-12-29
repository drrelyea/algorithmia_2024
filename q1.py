# %%
with open("everybody_codes_e2024_q01_p1.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%
def get_score(x):
    if x == "B":
        return 1
    elif x == "C":
        return 3
    elif x == "A":
        return 0


print(sum(map(get_score, [x for x in data[0]])))

# %%
with open("everybody_codes_e2024_q01_p2.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%


def get_score(x):
    if x == "B":
        return 1
    elif x == "C":
        return 3
    elif x == "A":
        return 0
    elif x == "D":
        return 5
    elif x == "x":
        return 0


ii = 0
score = 0
while ii < len(data[0]):
    p0 = data[0][ii]
    p1 = data[0][ii + 1]
    score += get_score(p1) + get_score(p0)
    if p0 != "x" and p1 != "x":
        score += 2
    ii += 2
print(score)


# %%
with open("everybody_codes_e2024_q01_p3.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%


def get_score(x):
    if x == "B":
        return 1
    elif x == "C":
        return 3
    elif x == "A":
        return 0
    elif x == "D":
        return 5
    elif x == "x":
        return 0


ii = 0
score = 0
while ii < len(data[0]):
    p0 = data[0][ii]
    p1 = data[0][ii + 1]
    p2 = data[0][ii + 2]
    score += get_score(p1) + get_score(p0) + get_score(p2)
    num_creatures = 3 - data[0][ii : ii + 3].count("x")
    if num_creatures == 2:
        score += 2
    elif num_creatures == 3:
        score += 6
    ii += 3
print(score)


# %%
