import pyaudio, wave

chunk = 1200
wf = wave.open('sample.wav', 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
data = wf.readframes(chunk)
while len(data) > 0:
    stream.write(data)
    data = wf.readframes(chunk)
stream.stop_stream()
stream.close()
p.terminate()