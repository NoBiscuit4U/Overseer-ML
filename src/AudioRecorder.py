import sounddevice as sd
import wavio as wv
import Variables
import os

cons=Variables.Constants
nsvars=Variables.NonStaticVars

def recordwriteAudio():
    newwav=sd.rec(int(cons.kdur*cons.kfreq),samplerate=cons.kfreq,channels=cons.kchannels)
    sd.wait()

    filename=f'newrecording-pid{nsvars.pid}-aid{nsvars.aid}.wav'
    path=f"C:\VS\SpeechMimicry\src\info\.wavfiles\pID{nsvars.pid}"
    wv.write(os.path.join(path,filename),newwav,cons.kfreq,sampwidth=cons.ksamplewidth)