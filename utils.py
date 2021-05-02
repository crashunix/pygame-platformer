import pygame
import engine

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 24)

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

def drawText(screen, t, x, y, fg, alpha):
    text = font.render(t, True, fg)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)

    blit_alpha(screen, text, (x,y), alpha)

heart_image = pygame.image.load('images/heart.png')

coin1 = pygame.image.load('images/coin/coin_0.png')
coin2 = pygame.image.load('images/coin/coin_1.png')
coin3 = pygame.image.load('images/coin/coin_2.png')
coin4 = pygame.image.load('images/coin/coin_3.png')
coin5 = pygame.image.load('images/coin/coin_4.png')
coin6 = pygame.image.load('images/coin/coin_5.png')

def makeCoin(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,23,23)
    entityAnimation = engine.Animation([coin1, coin2, coin3, coin4, coin5, coin6])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'collectable'
    return entity

enemy0 = pygame.image.load('images/spike_monster.png')

def makeEnemy(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,50,26)
    entityAnimation = engine.Animation([enemy0])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'dangerous'
    return entity


idle0 = pygame.image.load('images/player/vita_00.png')
idle1 = pygame.image.load('images/player/vita_01.png')
idle2 = pygame.image.load('images/player/vita_02.png')
idle3 = pygame.image.load('images/player/vita_03.png')

walking0 = pygame.image.load('images/player/vita_04.png')
walking1 = pygame.image.load('images/player/vita_05.png')
walking2 = pygame.image.load('images/player/vita_06.png')
walking3 = pygame.image.load('images/player/vita_07.png')
walking4 = pygame.image.load('images/player/vita_08.png')
walking5 = pygame.image.load('images/player/vita_09.png')

def resetPlayer(entity):
    entity.score.score = 0
    entity.battle.lives = 3
    entity.position.rect.x = 300
    entity.position.rect.y = 0
    entity.speed = 0
    entity.acceleration = 0.2
    entity.camera.setWorldPos(300,0)
    
def makePlayer(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,45,51)
    entityIdleAnimation = engine.Animation([idle0, idle1, idle2, idle3])
    entityWalkingAnimation = engine.Animation([walking0, walking1, walking2, walking3, walking4, walking5])
    entity.animations.add('idle', entityIdleAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    entity.score = engine.Score()
    entity.battle = engine.Battle()
    entity.intention = engine.Intention()
    entity.acceleration = 0.2
    entity.type = 'player'
    entity.reset = resetPlayer
    return entity