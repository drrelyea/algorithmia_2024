# %%
with open("everybody_codes_e2024_q02_p1.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%
num_runewords = 0
for line in data:
    if "WORDS" in line:
        runewords = line.split(":")[1].split(",")
    elif line:
        for lineword in line.split(" "):
            for ilineword in range(len(lineword)):
                for rune in runewords:
                    if (
                        len(rune) + ilineword <= len(lineword)
                        and lineword[ilineword : ilineword + len(rune)] == rune
                    ):
                        num_runewords += 1

print(num_runewords)
# %%
with open("everybody_codes_e2024_q02_p2.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%
num_runesymbols = 0
for line in data:
    if "WORDS" in line:
        runewords = line.split(":")[1].split(",")
    elif line:
        for lineword in line.split(" "):
            symbol_indices = set()
            for ilineword in range(len(lineword)):
                for rune in runewords:
                    if len(rune) + ilineword <= len(lineword) and (
                        lineword[ilineword : ilineword + len(rune)] == rune
                        or lineword[ilineword : ilineword + len(rune)] == rune[::-1]
                    ):
                        for rr in range(len(rune)):
                            symbol_indices.add(ilineword + rr)
            num_runesymbols += len(symbol_indices)

print(num_runesymbols)


# %%
with open("everybody_codes_e2024_q02_p3.txt") as input_file:
    inpstring = input_file.readlines()

data = [line.strip() for line in inpstring]
print(data)


# %%
symbol_lines = list()
for line in data:
    if "WORDS" in line:
        runewords = line.split(":")[1].split(",")
    elif line:
        symbol_lines.append(line)

# runewords = "THE,OWE,MES,ROD,RODEO".split(",")
# symbol_lines = [
#     "HELWORLT",
#     "ENIGWDXL",
#     "TRODEOAL",
# ]
symbol_map = set()
for iline, lineword in enumerate(symbol_lines):
    for ilineword in range(len(lineword)):
        for rune in runewords:
            if len(rune) + ilineword <= len(lineword):
                if (
                    lineword[ilineword : ilineword + len(rune)] == rune
                    or lineword[ilineword : ilineword + len(rune)] == rune[::-1]
                ):
                    for rr in range(len(rune)):
                        symbol_map.add((iline, ilineword + rr))
            else:
                if (
                    lineword[ilineword : len(lineword)]
                    + lineword[0 : ilineword + len(rune) - len(lineword)]
                    == rune
                    or lineword[ilineword : len(lineword)]
                    + lineword[0 : ilineword + len(rune) - len(lineword)]
                    == rune[::-1]
                ):
                    for rr in range(ilineword, len(lineword)):
                        symbol_map.add((iline, rr))
                    for rr in range(ilineword + len(rune) - len(lineword)):
                        symbol_map.add((iline, rr))
for iline, lineword_list in enumerate(list(map(list, zip(*symbol_lines)))):
    lineword = "".join(lineword_list)
    for ilineword in range(len(lineword)):
        for rune in runewords:
            if len(rune) + ilineword <= len(lineword):
                # print(lineword, rune, lineword[ilineword : ilineword + len(rune)], rune)
                if (
                    lineword[ilineword : ilineword + len(rune)] == rune
                    or lineword[ilineword : ilineword + len(rune)] == rune[::-1]
                ):
                    for rr in range(len(rune)):
                        symbol_map.add((ilineword + rr, iline))

print(len(symbol_map))

# %%
