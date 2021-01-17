import pyaudio

audio = pyaudio.PyAudio()
cnt = audio.get_device_count()
for i in range(cnt):
    desc = audio.get_device_info_by_index(i)
    print(desc)