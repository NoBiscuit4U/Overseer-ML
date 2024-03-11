import sounddevice as sd
from Constants import AudioHandlerConstants as cons
import wavio as wv
import os
import glob
import argparse

def recordwriteAudio(audioID,fp):
    #writes a .wavfile
    newwav=sd.rec(int(cons.dur*cons.freq),samplerate=cons.freq,channels=cons.channels)
    sd.wait()

    filename=f'newrecording-aid{audioID}.wav'
    file=os.path.join(fp,filename)
    wv.write(file,newwav,cons.freq,sampwidth=cons.sampleWidth)


def audiofileToString(directorypath):
    #listens to audio file and outputs text
    #Maybe work on but might just handle inside of c# in unity

    file=os.listdir(directorypath)[0]
    fp=os.path.join(directorypath,file)

    #os.remove(audioPath)

    #print(returntext)
    #return returntext