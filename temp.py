#-----
    #INPUT
    #-----

    #check for quit

    
    

    #control zoom level of the player camera
    #mais zoom
    # if keys[pygame.K_q]:
    #     player.camera.zoomLevel -= 0.01
    # #menos zoom
    # if keys[pygame.K_e]:
    #     player.camera.zoomLevel += 0.01

#------
#UPDATE
#------

if game_state == 'playing':

    #update animations
    for entity in globals.world.entities:
        entity.animations.animationList[entity.state].update()
    #coin_animation.update()

    

    
    #player_rect = pygame.Rect(int(player.position.rect.x), int(player.position.rect.y), player.position.rect.width, player.position.rect.height)
    # for c in coins:
    #     if c.colliderect(player_rect):
    #         coins.remove(c)
    #         score += 1

    #         if score == 2:
    #             game_state = 'win'

    #collection system
    # for entity in globals.world.entities:
    #     if entity.type == 'collectable':
    #         if entity.position.rect.colliderect(player_rect):
    #             globals.world.entities.remove(entity)
    #             player.score.score += 1
    #             # if player.score.score >= 2:
    #             #     game_state = 'win'
    
    #enemy system
    # for entity in globals.world.entities:
    #     if entity.type == 'dangerous':
    #         if entity.position.rect.colliderect(player_rect):
    #             player.battle.lives -= 1
    #             player.position.rect.x = 200
    #             player.position.rect.y = 0
    #             player_speed = 0

                # if player.battle.lives <= 0:
                #     game_state = 'lose'
    
    # if world.isWon():
    #     game_state = 'win'
    # if world.isLost():
    #     game_state = 'lose'

    
    # for e in enemies:
    #     if e.colliderect(player_rect):
    #         lives -= 1

    #         player_x = 200
    #         player_y = 0
    #         player_speed = 0

    #         if lives <= 0:
    #             game_state = 'lose'

#----
#DRAW
#----

#background
##screen.fill(SCREEN_COLOR)

##cameraSys.update(screen, world)

#draw system
# for entity in entities:
#     s = entity.state
#     a = entity.animations.animationList[s]
#     a.draw(screen, entity.position.rect.x, entity.position.rect.y, False if entity.direction == 'right' else True, False)

#player
# if player_direction == 'right':
#     # screen.blit(player_image, (player_x,player_y))
#     player_animations[player_state].draw(screen, player_x, player_y, False, False)
# elif player_direction == 'left':
#     # screen.blit(pygame.transform.flip(player_image, True, False), (player_x,player_y))
#     player_animations[player_state].draw(screen, player_x, player_y, True, False)

#HUD

# coin_animation.draw(screen, 10, 10, False, False)
# screen.blit(coin_image, (10, 10))
# utils.drawText(screen, str(score), 50, 10)
# score_text = font.render('Score: ' + str(score), True, (255,255,255), (0,0,0))
# score_text_rectangle = score_text.get_rect()
# score_text_rectangle.topleft = (10,10)
# screen.blit(score_text, score_text_rectangle)

# for index, live in enumerate(range(lives)):
#     screen.blit(heart_image, (200 + (index * 35),10))

# if game_state == 'win':
#     utils.drawText(screen, 'ganho', 300, 200)
    
# if game_state == 'lose':
#     utils.drawText(screen, 'perdeu', 300, 200)

#present screen
##pygame.display.flip()