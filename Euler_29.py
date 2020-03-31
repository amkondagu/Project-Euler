sequence = []
term = None
for a in range(2, 101):
    for b in range(2, 101):
        term = a ** b
        if term not in sequence:
            sequence.append(a ** b)

print(len(sequence))
        
