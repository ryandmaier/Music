import cmath
import math


#number of datapoints in a computation interval == n
#list conatining n intensity datapoints at regualar intervals == f_data
#intensity datapoint == i



freq = open('frequancy.txt')
for line in freq:
    f = float((line.split()[1]).strip())
    print('The note, {:<4} has a frequancy of {:} Hz'.format(line.split()[0],f))

freq.close()
