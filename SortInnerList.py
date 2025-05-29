scores=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
scores.sort(key= lambda x: (x[0],x[1]))
print(scores)

list_minimum=[scores[i][1] for i in range(len(scores)) ]

minummElement=min(list_minimum)

lowSecond=min(n for n in list_minimum if n!=minummElement)
print(lowSecond)
for i in range(5):
    if scores[i][1]==lowSecond :
        print(scores[i][0])