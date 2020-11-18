from random import randrange
from Basic_Stats import basic_stats
import matplotlib.pyplot as plt
x = []

for i in range(1000):
    x.append(randrange(0,101,1))

avg, stdev, histo = basic_stats(x)
print(avg)
print(stdev)
