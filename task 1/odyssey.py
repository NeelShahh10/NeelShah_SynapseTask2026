s = input()

count = {
    'I': 0,
    'T': 0,
    'H': 0,
    'A': 0,
    'C': 0
}

step = 0

for ch in s:
    if ch.isspace():
        continue

    step += 1
    ch = ch.upper()

    if ch in count:
        count[ch] += 1


    if (count['I'] >= 1 and
        count['T'] >= 1 and
        count['H'] >= 1 and
        count['A'] >= 2 and
        count['C'] >= 1):

        print(step)
        break
else:
    print(-1)