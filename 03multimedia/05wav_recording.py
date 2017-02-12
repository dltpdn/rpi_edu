import pyaudio, wave

RSec = 5
WaveFile = "mic_in.wav"
Format = pyaudio.paInt16
Rate = 48000
Chunk = 12000

p = pyaudio.PyAudio()
stream = p.open(format=Format, channels=1, rate=Rate, input=True, frames_per_buffer=Chunk)
print "* recording.."
frames = []
for i in range(0, int(Rate/Chunk * RSec)):
    data = stream.read(Chunk)
    frames.append(data)
print "* dong"
stream.stop_stream()
stream.close()
p.terminate()
wf= wave.open(WaveFile, 'wb')
wf.setnchannels(1)
wf.setsampwidth(p.get_sample_size(Format))
wf.setframerate(Rate)
wf.writeframes(b''.join(frames))
wf.close()

