import pyaudio

class Audio:
    def __init__(self):
        self.formato = pyaudio.paInt8
        self.canales = 1
        self.rate = 44100
        self.frames = 1
        self.max_frames = 65000
    def crearAudio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.formato,
            channels=self.canales,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.max_frames
        )
        print("Grabando Audio..")
        return stream
    def salidaAudio(self):
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=self.formato,
            channels=self.canales,
            rate=self.rate,
            output=True,
            output_device_index=8
        )
        print("Salida Audio..")
        return stream