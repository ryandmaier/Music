import cmath
import math

'''
number of datapoints in a computation interval == n == len(f_data)
number of datapoints per second == CHUNK
time spanned by compuation interval == RECORD_TIME
list conatining n intensity datapoints at regualar intervals == f_data
intensity datapoint == i
'''
#sum(-i(t)*e^(-2*pi*f*t))

def main(f_data,rate):
    freq = open('frequancy.txt')
    T_RESULT = []
    for line in freq:
        f = float((line.split()[1]).strip())
        T_RESULT.append([line.split()[0],transform(f_data,f,rate)])

    freq.close()

    

    return T_RESULT
    


def transform(f_data,f,rate):
    transform = 0
    c=0
    for i in f_data:
        transform += cmath.rect(-float(i),-2*(cmath.pi)*f*c/rate)
        c+=1
    return transform

def getCosData(freq, numData, time):
    all = []
    for i in range(0,numData):
        all.append(int(1000*math.cos(2*math.pi*freq*time*i/numData)))
    return all

g = open('lookRyan.txt','w')
freq = 261.63
numData = 128
time = 1

f_data = getCosData(freq, numData, time)
rate = numData/time

dat = main(f_data,rate)
g.write(str(main(f_data,rate)))
#reduced = []
for item in dat:
    reduced = []
    reduced.append(item[0])
    reduced.append(abs(item[1]))
    reduced.append(cmath.phase(item[1]))
    g.write(str(reduced)+'\n')

g.close()
    
    
'''
freq = 698.46
numData = 128
time = 1
'''


