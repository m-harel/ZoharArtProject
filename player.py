import pyaudio
import wave
import time
import serial
import serial.tools.list_ports

stopTimes = [37.68,214.84,369.79,529.64]
stopPlace = 0

ards = []
for port in serial.tools.list_ports.comports():
    port_data = (str)(port).split("-")
    if(port_data[1][1:12] == 'Arduino Uno'):
        print(port_data[0])
        temp_ard = serial.Serial(port_data[0],9600,timeout=5)
        ards.append(temp_ard)

by = bytearray('j','ascii')

for ard in ards:
    print(by)
    ard.write(by)
    time.sleep(5)
    ard.write(by)

print("init")

#define stream chunk
chunk = 1024

#open a wav format music


    #open stream

f = wave.open(r"thunder.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)


#read data
stopPlace=0
data = f.readframes(chunk)

#paly stream
start = time.time()
while 1:
    stream.write(data)
    data = f.readframes(chunk)
    done = time.time()
    elapsed = done - start

    if(stopPlace < len(stopTimes)):
        print(abs(stopTimes[stopPlace] - elapsed))
        if(abs(stopTimes[stopPlace] - elapsed) < 0.5):
            print(elapsed)
            stopPlace+=1
            for ard in ards:
                ard.write(by)
    if(len(data) == 0) : # If file is over then rewind.
        print('end')
        f.rewind()
        data = f.readframes(chunk)
        stopPlace=0
        start = time.time()
#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()