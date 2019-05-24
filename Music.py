
import pyaudio
import numpy
import struct
import cmath
import math
from pyaudio import PyAudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

class Music:

  def main(self):
    print('hi')
    self.outputSound(600)
    #all = self.getSound(128, 1) # 344, 256
    #print(self.getCosData(1,300,1))
    #all = getSound(128, 0.5) # 82 sublists, each 512 long
    #all = getSound(256, 0.5) # 43 sublists, each 1024 long

  def outputSound(self, freq):
    for i in range(0,10,):
        self.sine_tone(freq+i*20, 1)

  def sine_tone(self, frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    for buf in izip(*[samples]*sample_rate): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    #stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()

  def getFreqList(self, intensities):
    freqs = [] # 1 value for each piece
    for i in range(len(intensities)):
        piece = intensities[i] # sublist
        for i in range(0,len(piece)):
            print("hold up")

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
