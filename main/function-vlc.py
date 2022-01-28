"""https://www.geeksforgeeks.org/playing-youtube-video-using-python/"""
"""vlc doc : https://www.olivieraubert.net/vlc/python-ctypes/doc/vlc.Instance-class.html"""
from keyboard import read_key
from keyboard import add_hotkey
import time 
# importing vlc module
import vlc
# importing pafy module
import pafy

def on_space():
    global player
    player.pause()
    print('space was pressed')
def on_esc() :
    global player
    player.stop()
    print('esc was pressed')
def jump_forward() :
    global player
    current_time = player.get_time()
    player.set_time(current_time + 5000)
    #player.pause()
    print(current_time/1000)
    print((current_time + 5000) / 1000)
    #player.set_position(current_position + 0.01)
def set_backward() :
    global player
    current_time = player.get_time()
    print(current_time/1000)
    if current_time - 5000 >= 0 :
        player.set_time(current_time - 5000)
        print((current_time - 5000) / 1000)
    else :
        player.set_time(0)
        print("0")

# url of the video
url = "https://www.youtube.com/watch?v=VZo7YyffGNs&list=OLAK5uy_llgLGWQO1eoZPad5bjU4r9kihcgFgYnGk&index=5"

# creating pafy object of the video
video = pafy.new(url)

# getting best stream
best = video.getbest()

# creating vlc media player object

vlc_instance = vlc.Instance()
#vlc_instance.add_intf("123")
player = vlc_instance.media_player_new()
media = vlc_instance.media_new(best.url)
player.set_media(media)
#make the video start
player.play()
time.sleep(1)
if player.get_state() == 'State.Playing' :
    player.set_pause(1) 

#press space to pause
add_hotkey('space', on_space)

#this may break out the media player with errors
add_hotkey('esc' , on_esc)

#jump forward
add_hotkey('d' , jump_forward)

#set backward
add_hotkey('s' , set_backward)

#media_player.set_rate(n)  set rate

time.sleep(500)
duration = player.get_length()
print("Duration : " , duration*1000 , " min")
