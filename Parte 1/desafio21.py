from pygame import mixer
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
mixer.music.wait()
