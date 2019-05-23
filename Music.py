
import pyaudio
import numpy
import struct
import cmath
import math

class Music:

  def main():
    print('hi')
    all = getSound(128, 2) # 344, 256
    #all = getSound(128, 0.5) # 82 sublists, each 512 long
    #all = getSound(256, 0.5) # 43 sublists, each 1024 long

def getSound(CHUNK, rec_secs):

  # CHUNK = sublistSize # nt(numData/rec_secs) # default 128
  p = pyaudio.PyAudio()
  rate = 44100
  RECORD_SECONDS = rec_secs
  stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=CHUNK)

  print("* recording")
  all = []
  for i in range(0, int(rate / CHUNK * RECORD_SECONDS)):
    data = numpy.frombuffer(stream.read(CHUNK, exception_on_overflow = False), numpy.int16)
    all.append(data)
    #all+=data
  print("* done recording")

  for dat in all:
    print(numpy.frombuffer(dat, numpy.int16), '\n\n')
  print(len(all))
  print(len(numpy.frombuffer(all[30], numpy.int16)))

  #print(len(all[59]))
  #print(len(all[60]))
  #print(len(all[61]))
  #for dat in all:
  #print(numpy.frombuffer(dat, numpy.int16))
  return all



  #data = stream.read(CHUNK, exception_on_overflow = False)
  #print(numpy.frombuffer(data, numpy.int16)) # use external numpy module
  #print(struct.unpack('h'*CHUNK, data)) # use built-in struct module

  stream.stop_stream()
  stream.close()
  p.terminate()

Music.main()
