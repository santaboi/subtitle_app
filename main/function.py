import os
from playsound import playsound
print(os.path.abspath("./test_mp4/mp41.mp4"))

def play_movie():
    #need to take abspath
    os.startfile(os.path.abspath("./test_mp4/mp41.mp4") , show_cmd = 0)
play_movie()

