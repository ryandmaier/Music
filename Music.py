
import pyaudio
import numpy
import struct
import cmath
import math

class Music:

  def main(self):
    print('hi')
    all = self.getSound(128, 1) # 344, 256
    print(self.getCosData(1,300,1))
    #all = getSound(128, 0.5) # 82 sublists, each 512 long
    #all = getSound(256, 0.5) # 43 sublists, each 1024 long

  def getCosData(self, freq, numData, time):
    all = []
    for i in range(0,numData):
        all.append(int(1000*math.cos(2*math.pi*freq*time*i/numData)))
    return all

  def getSound(self, CHUNK, rec_secs):
    # CHUNK = sublistSize # nt(numData/rec_secs) # default 128
    p = pyaudio.PyAudio()
    rate = 44100
    RECORD_SECONDS = rec_secs
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=CHUNK)

    print("* recording")
    all = []
    #chunk: number of datapoints in 1 sublist
    #rate: number of datapoints in all the sublits in 1 second
    #rate / CHUNK: num of sublists in 1 second
    #chunk/rate: time between each sublist
    for i in range(0, int(rate / CHUNK * RECORD_SECONDS)):
        data = numpy.frombuffer(stream.read(CHUNK, exception_on_overflow = False), numpy.int16)
        all.append(data)
        #all+=data
    print("* done recording")

    # for dat in all:
    #     print(numpy.frombuffer(dat, numpy.int16), '\n\n')
    # print(len(all))
    # print(len(numpy.frombuffer(all[30], numpy.int16)))

      #print(len(all[59]))
      #print(len(all[60]))
      #print(len(all[61]))
      #for dat in all:
      #print(numpy.frombuffer(dat, numpy.int16))
    stream.stop_stream()
    stream.close()
    p.terminate()
    return all

def main():
    m = Music()
    m.main()

if __name__ == "__main__":
    main()
