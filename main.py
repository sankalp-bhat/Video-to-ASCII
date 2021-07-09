from toascii import Video
import time
import os

start_time = time.time()
vid = Video('Budraman.mp4', scale=0.1, verbose=True)
vid.convert()
print("--- %s seconds ---" % (time.time() - start_time))
gap = 0.03
a = 0
st = 0
v_time = time.time()
b = len(vid.frames)
input("Start?")
start_time = time.time()
while a < b:
    #os.system('cls')
    c = str(vid.frames[a])
    print(c+'\n')
    a += 1
    time.sleep(gap)


st = time.time() - start_time
print("--- ", st, " seconds ---")