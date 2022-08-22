import random

class Button:
    def __init__(self, x, y, image, type_mode, screen, PG):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.screen = screen
        self.PG = PG
        self.type_mode = type_mode
    def draw(self):
        mouse_pos = self.PG.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.PG.mouse.get_pressed()[0] == 1:
                if self.type_mode == "start":
                    return 1
        
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        return 0

class Rock_Images:
    def __init__(self, x, y, scale, strech, image, screen, PG):
        self.image = image
        #print(self.image.get_width(),self.image.get_height(),scale)
        self.image = PG.transform.scale(self.image,(int(self.image.get_width() * scale + strech),int(self.image.get_height() * scale)))
        #print(self.image.get_width(),self.image.get_height(),scale)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.PG = PG
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x - (self.width // 2)
        self.rect.y = y - (self.height)
    def draw(self):
        #print(self.rect.x,self.rect.y)
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

class Enemy:
    
    def __init__(self, x, y, location, scale, strech, image, bullet_image, firing_image, vikram, screen, PG):
        self.image = PG.transform.scale(image,(int(image.get_width() * scale + strech), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.PG = PG
        self.rect.x = x - (self.image.get_width() // 2)
        self.rect.y = y - (self.image.get_height())
        self.flip = False
        self.flag = 0
        self.bullet_image = bullet_image
        self.bullet_list = []
        self.firing_image = firing_image
        self.health_count = 2
        self.isalive = True
        self.idle_key = 0
        self.run_key = 0
        self.jump_key = 0
        self.distance_range = random.randint(100,150)
        self.velocity = 0
        self.gravity = 0.5
        self.inair = False
        self.temp_boolean_1 = True
        self.stone = None
        self.current_stone = location
        self.shoot = False
        self.shooting = False
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = y
        self.vikram = vikram
        self.bullet_timer = 0
        self.death = []
        self.i = 0
    
    def Jump(self, enemy, start_jump, jump, index, surface): #e_in_air do nothing at all
        if jump:
            if start_jump[index]:
                enemy[0][0].velocity = -20
                start_jump[index] = False
                enemy[0][0].inair = True
            jump = surface.jump(enemy)
        return jump
                
    def move(self, enemy, enemy_state, index1, vikram, distance):
        if enemy[0][0].rect.x > vikram[0].rect.x:
            #print(8)
            for i in enemy:
                for j in i:
                    j.flip = True
            if enemy[0][0].rect.x not in range(vikram[0].rect.x, vikram[0].rect.x + distance):
                #print(9)
                enemy_state[index1][1] = True
                enemy_state[index1][0] = False
                for i in enemy:
                    for j in i:
                        j.rect.x -= 1
            else:
                #print(10)
                enemy_state[index1][1] = False
                enemy_state[index1][0] = True
                return True
                                
        elif enemy[0][0].rect.x < vikram[0].rect.x:
            #print(11)
            for i in enemy:
                for j in i:
                    j.flip = False
            if enemy[0][0].rect.x not in range(vikram[0].rect.x - distance, vikram[0].rect.x):
                #print(12)
                enemy_state[index1][1] = True
                enemy_state[index1][0] = False
                for i in enemy:
                    for j in i:
                        j.rect.x += 1
            else:
                #print(13)
                enemy_state[index1][1] = False
                enemy_state[index1][0] = True
                return True
        else:
            #print(14)
            enemy_state[index1][1] = False
            enemy_state[index1][0] = True
            return True
        return False
    
    def check_to_jump(self, enemy, base_list, boolean, enemy_state, index1, start_jump, surface, vikram):
        base_list_name = ['big_rock_1a', 'float_rock_1a', 'float_rock_1b', 'float_rock_2a', 'float_rock_2b', 'float_rock_2c', 'float_rock_3a', 'float_rock_3b', 'float_rock_3c', 'main_rock_1a']
        if not enemy[0][0].inair:
            direction = []
            miny = 80
            miny_list = []
            enemy[0][0].stone = base_list[1]
            for i in base_list:
                if i == base_list[9]:
                    if miny > abs(i.rect.top - enemy[0][0].rect.y + 40) and (i.rect.top - enemy[0][0].rect.y + 40) < 0 and (i.rect.bottom - 54) not in range(enemy[0][0].rect.bottom - 60, enemy[0][0].rect.y + 60):
                            #print(index1, base_list_name[base_list.index(i)])
                            miny_list.append(i)
                else:
                    if miny > abs(i.rect.top - enemy[0][0].rect.y + 40) and (i.rect.top - enemy[0][0].rect.y + 40) < 0 and (i.rect.top not in range(enemy[0][0].rect.y - 60, enemy[0][0].rect.y + 60)):
                            #print(index1, base_list_name[base_list.index(i)])
                            miny_list.append(i)
            #print(len(miny_list))
            if len(miny_list):
                minx = abs(miny_list[0].rect.x + (miny_list[0].width//2) - enemy[0][0].rect.x)
            for i in miny_list:
                if minx > abs(i.rect.x + (i.width//2) - enemy[0][0].rect.x) - (vikram[0].rect.x - enemy[0][0].rect.x):
                    minx = abs(i.rect.x + (i.width//2) - enemy[0][0].rect.x)
                    enemy[0][0].stone = i
            #print('me')
            enemy[0][0].temp_boolean_1 = False
            
        if True:
            #print(base_list_name[base_list.index(enemy[0][0].stone)])
            boolean_2 = self.move(enemy, enemy_state, index1, [enemy[0][0].stone], 50)
            if boolean_2:
                enemy[0][0].temp_boolean_1 = True
                if not enemy[0][0].inair:
                    start_jump[index1] = True
                jump = self.Jump(enemy, start_jump, True, index1, surface)
                boolean_3 = self.move(enemy, enemy_state, index1, [enemy[0][0].stone], 0)

    def is_collide(self, bullet, enemy):
        if bullet.bullet_rect.x in range(enemy[0].rect.x, enemy[0].rect.x + enemy[0].width):
            for i in self.vikram:
                for j in i:
                    j.health_count -= 1
            return True

    def Shoot(self, limit, shoot, i, player, enemy):
        if shoot:
            i.bullet_rect.y = player.rect.y + ((player.height // 2) - 2)
            firing = self.PG.transform.scale(self.firing_image,(int(self.image.get_width() * 0.2),int(self.image.get_height() * 0.1)))

            if player.flip:
                self.flag = 1
                i.bullet_rect.x = (player.rect.x + 2)
                self.screen.blit(self.PG.transform.flip(firing, player.flip, False), (i.bullet_rect.x - 10.5, i.bullet_rect.y-0.8))
            else:
                player.flag = 0
                i.bullet_rect.x = (player.rect.x + player.width) - 2
                self.screen.blit(self.PG.transform.flip(firing, player.flip, False), (i.bullet_rect.x, i.bullet_rect.y-0.8))
                
        if player.flag:
            i.bullet_rect.x -= 7
        else:
            i.bullet_rect.x += 7
        local_boolean = self.is_collide(i, enemy)
        if i.bullet_rect.x > limit + 250 or i.bullet_rect.x < limit - 250 or local_boolean:
            #print("i am Staying here")
            player.bullet_list = []
            return False
        self.screen.blit(self.PG.transform.flip(i.bullet, self.flip, False), (i.bullet_rect.x, i.bullet_rect.y))
        return True

    def start_shoot(self, vikram, enemy):
        if (vikram[1][0].shoot or vikram[1][0].shooting):
            #print(2)            
            if vikram[1][0].inair == False:
                if vikram[1][0].shoot and vikram[1][0].bullet_list == []: 
                    bullet = Bullet(vikram[1][0], [], True, self.bullet_image, self.PG)
                    vikram[1][0].bullet_list.append(bullet)
            if vikram[1][0].bullet_list != []:
                    vikram[1][0].shooting = vikram[1][0].Shoot(vikram[1][0].rect.x + vikram[1][0].width, vikram[1][0].shoot, vikram[1][0].bullet_list[0], vikram[1][0], enemy)
            vikram[1][0].shoot = False
                
    #Artificial Intelligence for Enemy 
    def AI(self, enemy_list, vikram, enemy_state, surface, e_start_jump, e_jump, e_inair):

        for index1, enemy in enumerate(enemy_list):
            if enemy[0][0].isalive:
                #used to detect direction if enemy and hero not in same y
                local_temp_boolean_1 = False
                
                if enemy[0][0].rect.y < vikram[0].rect.top and enemy[0][0].rect.y not in range(vikram[0].rect.y - 40, vikram[0].rect.y + 40) and not enemy[0][0].inair:
                    #print(1)
                    if enemy[0][0].rect.y not in range(vikram[0].rect.y - 40, vikram[0].rect.y + 40) and not surface.vikram_inair:
                        #print(2)
                        if enemy[0][0].rect.x > vikram[0].rect.x - 600 and enemy[0][0].rect.x < vikram[0].rect.x + 600:
                            #print(3)
                            temp_boolean_1 = self.move(enemy, enemy_state, index1, vikram, 50)
                            
                        else:
                            #print(4)
                            enemy_state[index1][1] = True
                            enemy_state[index1][0] = False
                            for i in enemy:
                                for j in i:
                                    j.rect.x -= 1
                                    j.flip = True
                    else:
                        #print(6)
                        enemy_state[index1][1] = False
                        enemy_state[index1][0] = True
                    #used to check whether we have to find nearby stone or already did
                    enemy[0][0].temp_boolean_1 = True
                
                elif enemy[0][0].rect.y in range(vikram[0].rect.y - 40, vikram[0].rect.y + 40) and not enemy[0][0].inair:
                        #print(7)
                        local_temp_boolean_1 = self.move(enemy, enemy_state, index1, vikram, self.distance_range)
                        #used to check whether we have to find nearby stone or already did
                        enemy[0][0].temp_boolean_1 = True
                        #if enemy[0][0].x in range((location.rect.x + (location.width//2) - 10
                        #change_location()
                        temp = surface.on_surface(enemy, 0)
                        if enemy[1][0].bullet_list == [] and temp == [] and enemy[1][0].bullet_timer > 120:
                            enemy[1][0].shoot = True
                            enemy[1][0].bullet_timer = 0
                        enemy[1][0].bullet_timer += 3
                        enemy[1][0].start_shoot(enemy, vikram)
                else:
                    #print(15)
                    '''if enemy[0].temp_boolean_1:
                        print('if')
                        #local_temp_boolean_1 = self.move(enemy, enemy_state, index1, vikram, self.distance_range)'''
                    if True:
                        #print('else')
                        self.check_to_jump(enemy, surface.base_list, enemy[0][0].temp_boolean_1, enemy_state, index1, e_start_jump, surface, vikram)
                        enemy[0][0].temp_boolean_1 = False  
            else:
                enemy_state[index1][2] = False
                enemy_state[index1][1] = False
                enemy_state[index1][0] = False
                if enemy[0][0].i < 47:
                    enemy[0][0].death[int(enemy[0][0].i//6)].draw()
                    enemy[0][0].i += 1
                else:
                    enemy_list.remove(enemy)
    def draw(self):
        self.screen.blit(self.PG.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))

    
    
class Player:
    
    def __init__(self, x, y, scale, strech, image, bullet_image, firing_image, health_image, screen, PG):
        
        self.image = image
        self.image = PG.transform.scale(self.image,(int(self.image.get_width() * scale + strech),int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.PG = PG
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = x - (self.width // 2)
        self.rect.y = y - (self.height)
        self.x = x
        self.y = y
        self.flip = True
        self.flag = 0
        self.bullet_image = bullet_image
        self.bullet_list = []
        self.firing_image = firing_image
        self.health_image = health_image
        self.health_count = 5
        self.p_health = PG.transform.scale(health_image,(int(self.image.get_width() * 0.6),int(self.image.get_height() * 0.6)))
        self.h_rect = self.image.get_rect()
        self.h_rect.x = 0
        self.h_rect.y = 10
        self.isalive = True
        self.gravity = 0.5
        self.velocity = 0
        self.inair = False
        self.scale = scale
        self.strech = strech
        self.score = 0

        
    def Shoot(self, limit, shoot, i, player, enemy_list):
        if shoot:
            i.bullet_rect.y = player.rect.y + ((player.height // 2) - 2)
            firing = self.PG.transform.scale(self.firing_image,(int(self.image.get_width() * 0.2),int(self.image.get_height() * 0.1)))

            if self.flip:
                self.flag = 1
                i.bullet_rect.x = (player.rect.x + 2)
                self.screen.blit(self.PG.transform.flip(firing, self.flip, False), (i.bullet_rect.x - 10.5, i.bullet_rect.y-0.8))
            else:
                self.flag = 0
                i.bullet_rect.x = (player.rect.x + player.width) - 2
                self.screen.blit(self.PG.transform.flip(firing, self.flip, False), (i.bullet_rect.x, i.bullet_rect.y-0.8))
        if self.flag:
            i.bullet_rect.x -= 15
        else:
            i.bullet_rect.x += 15
        local_boolean = self.iscollide(i, enemy_list, player)
        if i.bullet_rect.x > limit + 350 or i.bullet_rect.x < limit - 400 or local_boolean:
            #print("i am Staying here")
            if self.flag == 1:
                i.bullet_rect.x = (player.rect.x + 2)
            else:
                i.bullet_rect.x = (player.rect.x + self.width) - 2
            i.bullet_rect.y = player.rect.y + ((player.height // 2) - 2)
            player.bullet_list.remove(i)
            return False
        self.screen.blit(self.PG.transform.flip(i.bullet, self.flip, False), (i.bullet_rect.x, i.bullet_rect.y))
        return True
    
    def iscollide(self, bullet, enemy_list, player):
        for enemy in enemy_list:
            if bullet.bullet_rect.x in range(enemy[0][0].rect.x, enemy[0][0].rect.x + enemy[0][0].width) and bullet.bullet_rect.y in range(enemy[0][0].rect.top, enemy[0][0].rect.bottom) and enemy[0][0].isalive:
                enemy[0][0].isalive = False
                player.score += 1
                return True
    def health(self):
        x = 10
        for i in range(self.health_count):
            self.screen.blit(self.p_health, (self.h_rect.x + x, self.h_rect.y))
            x = x + 25
        if self.health_count < 1:
            self.isalive = False

    def draw(self):
        #print(self.rect.x,self.rect.y)
        self.screen.blit(self.PG.transform.flip(self.image, self.flip, False), (self.rect.x, self.rect.y))

class Bullet:
    def __init__(self, player, enemy, boolean, bullet_image, PG):
        self.player = player
        self.enemy = enemy
        self.bullet_image = bullet_image
        self.bullet = PG.transform.scale(self.bullet_image,(int(player.image.get_width() * 0.2),int(player.image.get_height() * 0.05)))
        self.bullet_rect = self.bullet.get_rect()
        self.bullet_rect.x = (player.rect.x + player.width) - 2
        self.bullet_rect.y = player.y - ((player.height // 2) + 3)
    

class Surface:
    
    def __init__(self, vikram, base_list, big_rock_1a, float_rock, main_rock_1a, screen, PG):
        self.vikram = vikram
        self.base_list = base_list
        self.screen = screen
        self.PG = PG
        self.vikram_inair = False
        self.gravity = 0.5
        self.velocity = 0
        self.big_rock_1a = big_rock_1a
        self.float_rock = float_rock
        self.main_rock_1a = main_rock_1a
        self.health_rock = False
        self.is_health_appeared = False
        self.health_appear_count = 0
        self.take_down_count = 0
        #self.health_image = health_image
    #Check player on floor, returns player if not in floor
    def on_surface(self, vikram, special_case):
        not_in_surface = []
        for i in self.base_list:
            #print(2)
            if int(vikram[0][0].rect.x) in range(i.rect.x - 25, (i.rect.x + i.width) - 20):
                #print(vikram[0][0].rect.y, i.rect.y, i.rect.top)
                if special_case:
                    if i == self.big_rock_1a:
                        if int(vikram[0][0].rect.y - vikram[0][0].velocity) < i.rect.y and int(vikram[0][0].rect.y + vikram[0][0].velocity) > i.rect.y:
                            vikram[0][0].velocity = vikram[0][0].rect.y - i.rect.top - 3
                            break
                    elif i in self.float_rock[1]:
                        if int(vikram[0][0].rect.bottom - vikram[0][0].velocity) < i.rect.top + 12 and int(vikram[0][0].rect.bottom + vikram[0][0].velocity) > i.rect.top + 12:
                            #print(vikram[0][0].rect.bottom, i.rect.top, self.velocity)
                            vikram[0][0].velocity = (vikram[0][0].rect.y - i.rect.top) + 10
                            break
                    elif i in self.float_rock[0]:
                        if int(vikram[0][0].rect.bottom - vikram[0][0].velocity) < i.rect.top and int(vikram[0][0].rect.bottom + vikram[0][0].velocity) > i.rect.top:
                            vikram[0][0].velocity = (vikram[0][0].rect.y - i.rect.top) + 10
                            break
                    elif i in self.float_rock[2]:
                        if int(vikram[0][0].rect.bottom - vikram[0][0].velocity) < i.rect.top and int(vikram[0][0].rect.bottom + vikram[0][0].velocity) > i.rect.top:
                            vikram[0][0].velocity = (vikram[0][0].rect.y - i.rect.top)
                            break
                    elif i == self.main_rock_1a:
                        if int(vikram[0][0].rect.bottom - vikram[0][0].velocity) < (i.rect.bottom - 54) and int(vikram[0][0].rect.bottom + vikram[0][0].velocity) > (i.rect.bottom - 54):
                            vikram[0][0].velocity = (vikram[0][0].rect.y - (i.rect.bottom-54))
                            break
                else:
                    if i == self.big_rock_1a:
                        #print(2)
                        if int(vikram[0][0].rect.y) in range(i.rect.top - 6, i.rect.top + 6):
                            #print(0)
                            break
                    elif i in self.float_rock[1]:
                        if int(vikram[0][0].rect.bottom) in range(i.rect.top + 10, i.rect.top + 14):
                            #print(vikram[0][0].rect.bottom, i.rect.top)
                            #print(0)
                            break
                    elif i in self.float_rock[0]:
                        if int(vikram[0][0].rect.bottom) in range(i.rect.top + 10, i.rect.top + 14):
                            #print(vikram[0][0].rect.bottom, i.rect.top)
                            #print(0)
                            break
                    elif i in self.float_rock[2]:
                        if int(vikram[0][0].rect.bottom) in range(i.rect.top +28, i.rect.top + 37):
                            #print("i am else")
                            if i == self.float_rock[2][2] and vikram[0][0] == self.vikram[0][0]:
                                self.take_down_count += 1
                                self.health_rock = True
                            break
                    elif i == self.main_rock_1a:
                        #print(vikram[0][0].rect.bottom, i.rect.bottom - 53)
                        if int(vikram[0][0].rect.bottom) in range(i.rect.bottom - 55, i.rect.bottom - 50):
                            #print("main")
                            break

        else:
            #print(1)
            not_in_surface.append('player')
        if self.health_rock:
            #print(1)
            if self.take_down_count > 100:
                self.float_rock[2][2].rect.y += 3
                #print(self.float_rock[2][2].rect.y)
                if self.float_rock[2][2].rect.y > 550:
                    #print(1)
                    self.float_rock[2][2].rect.y = 550
                    self.health_rock = False
        else:
            self.take_down_count = 0
            #print(0)
            self.float_rock[2][2].rect.y -= 1
            if self.float_rock[2][2].rect.y < 130:
                #print(0)
                self.float_rock[2][2].rect.y = 130
        return not_in_surface
    
    def jump(self, vikram):
        temp = self.on_surface(vikram, 1)
        
        if vikram[0][0].inair:
            #print(temp, self.velocity)
            if 'player' not in temp:
                vikram[0][0].inair = False
                #print('done')
                return False
            for i in vikram:
                for j in i:
                    #print(self.velocity)
                    j.rect.y += vikram[0][0].velocity
            vikram[0][0].velocity += vikram[0][0].gravity
            if vikram[0][0].rect.y > 650:
                for i in vikram:
                    for j in i:
                        #print(self.velocity)
                        j.health_count -= 1
                        j.rect.y = 0
                return False
            #print(temp)
            
            return True
    def extra_health(self):
        self.health_appear_count += 1
        #print(self.health_appear_count)
        if not self.is_health_appeared:
            if self.health_appear_count > 360:
                self.health_appear_count = 0
                self.is_health_appeared = True
        else:
            #print('heart')
            self.screen.blit(self.vikram[0][0].p_health,(int(self.float_rock[2][2].rect.x + (self.float_rock[2][2].width//2) - 10 ),int(self.float_rock[2][2].rect.y)-10))
            #print(self.vikram[0][0].rect.x, self.float_rock[2][2].rect.x + (self.float_rock[2][2].width//2) - 10, self.vikram[0][0].rect.bottom, self.float_rock[2][2].rect.y-10)
            if self.vikram[0][0].rect.x in range(int(self.float_rock[2][2].rect.x + (self.float_rock[2][2].width//2) - 38 ),int(self.float_rock[2][2].rect.x + (self.float_rock[2][2].width//2) - 18 )) and int(self.vikram[0][0].rect.bottom) in range(self.float_rock[2][2].rect.top +28, self.float_rock[2][2].rect.top + 57):
                self.is_health_appeared = False
                self.health_appear_count = 0
                self.vikram[0][0].health_count += 1
            if self.health_appear_count > 200:
                self.is_health_appeared = False
                self.health_appear_count = 0
                
