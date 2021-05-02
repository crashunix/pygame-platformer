import globals
import pygame
import utils

class Level:
    def __init__(self, platforms=None, entities=None, winFunc=None, loseFunc=None):
        self.platforms = platforms
        self.entities = entities
        self.winFunc = winFunc
        self.loseFunc = loseFunc        
    def isWon(self):
        if self.winFunc is None:
            return False
        return self.winFunc(self)
    def isLost(self):
        if self.loseFunc is None:
            return False
        return self.loseFunc(self)

#lose if no players have lives remaining
def lostLevel(level):
    #level isn`t lost if any player has a life left
    for entity in level.entities:
        if entity.type == 'player':
            if entity.battle is not None:
                if entity.battle.lives > 0:
                    return False
    #level is lost otherwise
    return True

#win if no collectable items left
def wonLevel(level):
    # level isn't won if any collectable exists
    for entity in level.entities:
        if entity.type == 'collectable':
            return False
    #level isn`t won otherwise
    return True

def loadLevel(levelNumber):
    if levelNumber == 1:
        #load level 1
        globals.world = Level(
            platforms = [
                #middle
                pygame.Rect(100,300,400,50),
                #left
                pygame.Rect(100,250,50,50),
                #right
                pygame.Rect(450,250,50,50)
            ],
            entities = [
                #coins
                utils.makeCoin(100, 200),
                utils.makeCoin(200, 250),

                #enemy
                utils.makeEnemy(150, 274),

                #players
                globals.player1
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )

    if levelNumber == 2:
        #load level 2
        globals.world = Level(
            platforms = [
                #middle
                pygame.Rect(100,300,400,50),
                pygame.Rect(500,250,100,50),
                pygame.Rect(300,190,100,50),
                pygame.Rect(100,130,100,50),
            ],
            entities = [
                #coins
                utils.makeCoin(100, 250),
                utils.makeCoin(300, 250),

                #players
                globals.player1,
                globals.player2 
            ],
            winFunc = wonLevel,
            loseFunc = lostLevel
        )
    
    #reset player
    for entity in globals.world.entities:
        entity.reset(entity)