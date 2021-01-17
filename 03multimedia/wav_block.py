import pyaudio, wave

file_name = 'sample.wav'
chunk = 1024

wf = wave.open(file_name, 'rb')
rate=wf.getframerate(),
channels=wf.getnchannels()
width = wf.getsampwidth()
print(f'{file_name}, rate:{rate}, channels:{channels}, width:{width}, {pyaudio.paInt16}')

pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,#pa.get_format_from_width(width),
                channels=channels, 
                rate=rate[0],
                output=True)

while True:
    data = wf.readframes(chunk)
    if len(data) <= 0 :
        break
    stream.write(data)
    
stream.stop_stream()
stream.close()
pa.terminate()