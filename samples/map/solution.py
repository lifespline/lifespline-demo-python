# map integers from 1 to 9 to their square values
print(list(map(lambda x: x*x, range(1, 10))))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(lambda x, y: x * y, range(1, 10), range(1, 10))))
# [1, 4, 9, 16, 25, 36, 49, 64, 81]

# sum sublists
print(list(map(sum, [range(1, 10), range(1, 10)])))
