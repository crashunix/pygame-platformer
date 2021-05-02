import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.soundVolume = 0.4
        self.musicVolume = 0.2
        self.sounds = {
            'jump': pygame.mixer.Sound('sounds/03_Jump_v2.wav'),
            'coin': pygame.mixer.Sound('sounds/01_Coin Pickup_v2.wav')
        }
        self.music = {
            'towering': 'musics/towering.mp3',
            'coffee': 'musics/coffee.mp3'
        }
    def playSound(self, soundName):
        self.sounds[soundName].set_volume(self.soundVolume)
        self.sounds[soundName].play()
    def playMusic(self, musicName):
        pass
        # pygame.mixer.music.load(self.music[musicName])
        # pygame.mixer.music.set_volume(self.musicVolume)
        # pygame.mixer.music.play(-1)
