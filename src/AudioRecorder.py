import sounddevice as sd
import wavio as wv
import os

#player id
m_pid=1
#audio id
m_aid=1

kfreq=44100
kdur=10
ksamplewidth=2
kchannels=2

def recordwriteAudio():
    newwav=sd.rec(int(kdur*kfreq),samplerate=kfreq,channels=kchannels)
    sd.wait()

    filename=f'newrecording-pid{m_pid}-aid{m_aid}.wav'
    path=f"C:\VS\SpeechMimicry\src\info\.wavfiles\pID{m_pid}"
    wv.write(os.path.join(path,filename),newwav,kfreq,sampwidth=ksamplewidth)

recordwriteAudio()