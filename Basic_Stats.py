import matplotlib.pyplot as plt
import math

def basic_stats(x):

    avg = mean(x)
    stdev = std(x, avg)

    # Count number of values within one standard deviation of the mean and report whether or not the data is normally
    # distributed

    count = 0
    for el in x:
        if el >= (avg-stdev) and el <= (avg+stdev):
            count += 1

    isNormal = False
    percentage = (count/len(x))*100

    if percentage > 67 and percentage < 69:
        print("The data is normally distributed.")
    else:
        print("The data is not normally distributed.")

    histo = plt.hist(x, 20)
    plt.show()

    return avg, stdev, histo

def mean(x):

    num = 0

    for el in x:
        num += el

    mu = num/len(x)

    return mu

def std(x, mu):

    num = 0

    for el in x:
        num += (el-mu)**2

    sigma = math.sqrt(num/len(x))

    return sigma