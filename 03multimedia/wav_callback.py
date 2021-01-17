import pyaudio, wave, time

def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

wf = wave.open('sample.wav', 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback = callback)
stream.start_stream()
while stream.is_active():
    time.sleep(0.5)
stream.stop_stream()
stream.close()
wf.close()
p.terminate()