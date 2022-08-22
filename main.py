import pygame as PG
import random
import Resources.Modules.Resource as R

PG.init()

Screen_width = 800
Screen_height = 580

screen = PG.display.set_mode([Screen_width,Screen_height])

clock = PG.time.Clock()
FPS = 60
def highscore():
    f = open('Resources\Temp\Cache.txt', mode = 'r')
    score = f.read()
    hscore = int(score.split("= ")[1])
    return hscore
def Resume_page():
    uncracked = PG.font.Font(r'Resources\Fonts\uncracked.otf',122)
    tmd = PG.font.Font(r'Resources\Fonts\TMD.ttf',22)
    running = True

    while running:
        new_record = uncracked.render("RESUME",True,(255,255,255))
        screen.blit(new_record,[285,230])
        new_record = tmd.render("PRESS ENTER TO CONTINUE",True,(255,255,255))
        screen.blit(new_record,[285,320])
        for event in PG.event.get():
            if event.type == PG.KEYDOWN:
                    if event.key == PG.K_RETURN:
                        running = False
        PG.display.update()            
    return 0
def Game():

    background_image = PG.image.load('Resources\Images\Backgrounds\Background.png')
    bg_rect = background_image.get_rect()
    background_image = PG.transform.scale(background_image, (Screen_width+55, Screen_height+30))
    smallfont = PG.font.SysFont("comicsansms",18)
    avalon = PG.font.Font("Resources\Fonts\Avalon.otf",72)
    uncracked = PG.font.Font(r'Resources\Fonts\uncracked.otf',122)
    sp = PG.font.Font(r'Resources\Fonts\sp.ttf',100)
    tmd = PG.font.Font(r'Resources\Fonts\TMD.ttf',24)
    
    #rocks images    
    big_rock_1a = PG.image.load('Resources\Images\Backgrounds\Big_rock.png')
    main_rock_1a = PG.image.load('Resources\Images\Backgrounds\Main_rock.png')
    float_rock_1a = PG.image.load('Resources\Images\Backgrounds\Floating rock 1.png')
    float_rock_1b = PG.image.load('Resources\Images\Backgrounds\Floating rock 1.png')
    float_rock_2a = PG.image.load('Resources\Images\Backgrounds\Floating rock 2.png')
    float_rock_2b = PG.image.load('Resources\Images\Backgrounds\Floating rock 2.png')
    float_rock_2c = PG.image.load('Resources\Images\Backgrounds\Floating rock 2.png')
    float_rock_3a = PG.image.load('Resources\Images\Backgrounds\Floating rock 3.png')
    float_rock_3b = PG.image.load('Resources\Images\Backgrounds\Floating rock 3.png')
    float_rock_3c = PG.image.load('Resources\Images\Backgrounds\Floating rock 3.png')
    bullet_img = PG.image.load('Resources\Images\Action\Bullet.png')
    firing_img = PG.image.load('Resources\Images\Action\Firing.png')
    health_img = PG.image.load('Resources\Images\Health\Health.png')
    #big_rock_1 = PG.transform.scale(big_rock_1,(200,300))



    #creating rocks
    big_rock_1a = R.Rock_Images(Screen_width // 2, Screen_height, 0.3, 250, big_rock_1a, screen, PG)
    float_rock_1a = R.Rock_Images(100, Screen_height - 120, 0.5, 50, float_rock_1a, screen, PG)
    float_rock_1b = R.Rock_Images(100, Screen_height - 320, 0.5, 50, float_rock_1b, screen, PG)
    float_rock_2a = R.Rock_Images(300, Screen_height - 210, 0.4, 50, float_rock_2a, screen, PG)
    float_rock_2b = R.Rock_Images(550, Screen_height - 210, 0.4, 50, float_rock_2b, screen, PG)
    float_rock_2c = R.Rock_Images(1000, Screen_height - 250, 0.4, 50, float_rock_2c, screen, PG)
    float_rock_3a = R.Rock_Images(750, Screen_height - 120, 0.4, 50, float_rock_3a, screen, PG)
    float_rock_3b = R.Rock_Images(750, Screen_height - 300, 0.4, 50, float_rock_3b, screen, PG)
    float_rock_3c = R.Rock_Images(1305, 230, 0.4, 50, float_rock_3c, screen, PG)
    main_rock_1a = R.Rock_Images(Screen_width + 300, Screen_height, 0.3, 250, main_rock_1a, screen, PG)
    screen.fill((255, 255, 255))
    global running
    running = True
    #rocklist
    base_list = [big_rock_1a, float_rock_1a, float_rock_1b, float_rock_2a, float_rock_2b, float_rock_2c, float_rock_3a, float_rock_3b, float_rock_3c, main_rock_1a]
    float_rock_1 = [float_rock_1a, float_rock_1b]
    float_rock_2 = [float_rock_2a, float_rock_2b, float_rock_2c]
    float_rock_3 = [float_rock_3a, float_rock_3b, float_rock_3c]
    float_rock = [float_rock_1, float_rock_2, float_rock_3]
    
    #player list
    #vikram_boolean = [idle, run, jump, shooting, crouch]
    vikram_boolean = [True, False, False]
    vikram_idle = []
    vikram_run = []
    vikram_jump = []
    vikram_death = []
    global jump    
    moving_left = False
    moving_right = False
    jump = False
    
    on_going_bullet = []     
    not_in_surface = []
    e_not_in_surface = []
    global start_jump
    global vikram_idle_key
    global vikram_run_key
    global vikram_jump_key
    global vikram_death_key
    global shooting, previous_score
    previous_score = 0
    
    shooting = False

    vikram_idle_key = 0
    vikram_run_key = 0
    vikram_jump_key = 0
    vikram_death_key = 0
    
    global ec
    global enemy_creation_count
    global enemy_creation_time
    global enemy_creation_location
    global enemy_limit
    #Enemy
    enemy_limit = 6
    ec = 120
    enemy_creation_count = 110
    enemy_creation_time = random.randint(ec,ec+2)
    enemy_creation_location = random.randint(0,len(base_list)-1)
    enemy_list = []
    enemy_idle = []
    enemy_run = []
    enemy_jump = []
    e_jump = []
    e_start_jump = []
    enemy_state = []

    
    def score(score):
        global ec, running, vikram_death_key, enemy_limit, previous_score
        text = tmd.render("Score:"+str(score),True,(255,255,255))
        
        screen.blit(text,[700,10])
        if (score%11 == 0) and score!=1 and score != 0 and previous_score != score:
            ec -= 2
            if ec < 1:
                ec = 1
            enemy_limit += 3
            previous_score = score
        #print(ec)
        if not vikram[0][0].isalive and vikram_death_key >= 47:
            high_score = highscore()
            re_start_img = PG.image.load('Resources\Images\Main\Restart.png').convert_alpha()
            re_start_img = PG.transform.scale(re_start_img, (int(re_start_img.get_width() * 0.1), int(re_start_img.get_height() *0.1)))
            re_start_button = R.Button(620 , 480 , re_start_img, 'start', screen, PG)
            while running:
                for event in PG.event.get():
                    if event.type == PG.QUIT:
                        running = False
                    if event.type == PG.KEYDOWN:
                        if event.key == PG.K_RETURN:
                            Game()
                screen.fill((255,255,255))
                if high_score < score:
                    
                    new_record = uncracked.render("NEW RECORD",True,(0,0,0))
                    screen.blit(new_record,[225,175])
                    new_record = tmd.render("High Score : " + str(score),True,(0,0,0))
                    screen.blit(new_record,[340,275])
                    f = open('Resources\Temp\Cache.txt', mode = 'w')
                    f.write("High Score = " + str(score))
                    f.close()
                else:
                    string = 'SCORE  ' + str(score)
                    new_record = uncracked.render(string,True,(0,0,0))
                    screen.blit(new_record,[280,175])
                    new_record = tmd.render("HIGH SCORE : " + str(high_score),True,(0,0,0))
                    screen.blit(new_record,[340,275])
                start_key = re_start_button.draw()
                if start_key:
                    running = False
                    Game()
                PG.display.update()
                
    for i in range(5):
        vikram = PG.image.load('Resources\Images\Vikram\Idle\%d.png' % i)
        #print('Resources\Images\Vikram\Idle\%d.png' % i)
        vikram = R.Player(250, Screen_height-53, 0.7, 0, vikram, bullet_img, firing_img, health_img, screen, PG)
        vikram_idle.append(vikram)
        
    for i in range(6):
        vikram = PG.image.load('Resources\Images\Vikram\Run\%d.png' % i)
        #print('Resources\Images\Vikram\Run\%d.png' % i)
        vikram = R.Player(250, Screen_height-53, 0.7, 0, vikram, bullet_img, firing_img, health_img, screen, PG)
        vikram_run.append(vikram)

    for i in range(3):
        vikram = PG.image.load('Resources\Images\Vikram\Jump\%d.png' % i)
        #print('Resources\Images\Vikram\Run\%d.png' % i)
        vikram = R.Player(250, Screen_height-53, 0.7, 0, vikram, bullet_img, firing_img, health_img, screen, PG)
        vikram_jump.append(vikram)
    for i in range(8):
        vikram = PG.image.load('Resources\Images\Vikram\Death\%d.png' % i)
        #print('Resources\Images\Vikram\Run\%d.png' % i)
        vikram = R.Player(250, Screen_height-53, 0.7, 0, vikram, bullet_img, firing_img, health_img, screen, PG)
        vikram_death.append(vikram)
        
    vikram = [vikram_idle, vikram_run, vikram_jump, vikram_death]
    surface = R.Surface(vikram, base_list, big_rock_1a, float_rock, main_rock_1a, screen, PG)
    def Image_draw():
        
        big_rock_1a.draw()
        #print(big_rock_1a.rect.bottom, vikram_idle[0].rect.bottom, main_rock_1a.rect.bottom)
        float_rock_1a.draw()
        float_rock_1b.draw()
        float_rock_2a.draw()
        float_rock_2b.draw()
        float_rock_2c.draw()
        float_rock_3a.draw()
        float_rock_3b.draw()
        float_rock_3c.draw()
        main_rock_1a.draw()
        vikram_idle[0].health()
        global vikram_run_key
        global vikram_idle_key
        global vikram_jump_key
        global vikram_death_key
        
        if vikram_boolean[0]:
            if vikram_idle_key > 24:
                vikram_idle_key = 0
            vikram[0][int(vikram_idle_key//5)].draw()
            vikram_idle_key += 1
            vikram_run_key = 0
            vikram_jump_key = 0
            
        if vikram_boolean[1]:
            if vikram_run_key > 17:
                vikram_run_key = 0
            vikram[1][int(vikram_run_key)//3].draw()
            vikram_run_key += 1
            vikram_idle_key = 0
            vikram_jump_key = 0
            
        if vikram_boolean[2]:
            global start_jump
            if start_jump:
                vikram_jump_key = 0
            else:
                vikram_jump_key = 1
            vikram[2][int(vikram_jump_key)].draw()
            vikram_jump_key += 1
            vikram_idle_key = 0
            vikram_run_key = 0

        if not vikram[0][0].isalive:
            if vikram_death_key > 47:
                vikram_death_key = 47
            vikram[3][int(vikram_death_key//6)].draw()
            vikram_death_key += 1

        for index1, i in enumerate(enemy_list):
            for index2, j in enumerate(i):
                if index2 == 0:
                    if enemy_state[index1][index2]:
                        if j[0].idle_key > 24:
                            j[0].idle_key = 0
                        j[int(j[0].idle_key//5)].draw()
                        j[0].idle_key += 1
                        j[0].run_key = 0
                        j[0].jump_key = 0
                if index2 == 1:
                    if enemy_state[index1][index2]:
                        if j[0].run_key > 17:
                            j[0].run_key = 0
                        #print(j[0].run_key)
                        j[int(j[0].run_key//3)].draw()
                        j[0].run_key += 1
                        j[0].idle_key = 0
                        j[0].jump_key = 0
                if index2 == 2:
                    #print(enemy_state[index1])
                    if enemy_state[index1][index2]:
                        #print('here')
                        if e_start_jump[index1]:
                            j[0].jump_key = 0
                        else:
                            j[0].jump_key = 1
                        j[j[0].jump_key].draw()
                        j[0].run_key = 0
                        j[0].idle_key = 0
        score(vikram_run[0].score)
            
    def vikram_movement(moving_left, moving_right, shoot, base_list, vikram_idle, vikram_run, virkam_jump):
        global vikram_run_key
        global shooting
        if vikram_idle[0].isalive:
            if moving_left:
                if vikram_idle[0].rect.x < 200:
                    for i in base_list:
                        i.rect.x += 2
                    for i in enemy_list:
                        for j in i:
                            for k in j:
                                k.rect.x += 2
                                #print(k.rect.x)
                    for i in vikram_idle:
                        i.flip = True
                    for i in vikram_run:
                        i.flip = True
                    for i in vikram_jump:
                        i.flip = True
                    for i in vikram_death:
                        i.flip = True
                else:
                    for i in vikram_idle:
                        i.rect.x -= 2
                        #i.bullet_rect.x -=2
                        i.flip = True
                    for i in vikram_run:
                        i.rect.x -= 2
                        i.flip = True
                    for i in vikram_jump:
                        i.rect.x -= 2
                        i.flip = True
                    for i in vikram_death:
                        i.rect.x -= 2
                        i.flip = True
                
            elif moving_right:
                if vikram_idle[0].rect.x > 500:
                    for i in base_list:
                        i.rect.x -= 2
                    for i in enemy_list:
                        for j in i:
                            for k in j:
                                k.rect.x -= 2
                                #print(k.rect.x)
                    for i in vikram_idle:
                        i.flip = False
                    for i in vikram_run:
                        i.flip = False
                    for i in vikram_jump:
                        i.flip = False
                    for i in vikram_death:
                        i.flip = False
                else:
                    for i in vikram_idle:
                        i.rect.x += 2
                        #i.bullet_rect.x +=2
                        i.flip = False
                    for i in vikram_run:
                        i.rect.x += 2
                        i.flip = False
                    for i in vikram_jump:
                        i.rect.x += 2
                        i.flip = False
                    for i in vikram_death:
                        i.rect.x += 2
                        i.flip = False    
            if (shoot or shooting or vikram[1][0].bullet_list != []):
                
                if surface.vikram_inair == False:
                    if shoot and len(vikram[1][0].bullet_list) < 2: 
                        bullet = R.Bullet(vikram[1][0], [], True, bullet_img, PG)
                        vikram[1][0].bullet_list.append(bullet)
                if vikram[1][0].bullet_list != []:
                    for i in vikram[1][0].bullet_list:
                        shooting = vikram_run[0].Shoot(vikram_run[0].rect.x + vikram_run[0].width, shoot, i, vikram_run[0], enemy_list)
                shoot = False

            if len(enemy_list):
                enemy_list[0][0][0].AI(enemy_list, vikram_idle, enemy_state, surface, e_start_jump, e_jump, e_inair)

            surface.extra_health()
    def vikram_do_jump(jump):
        global start_jump
        if jump:
            if start_jump:
                vikram[0][0].velocity = -14
                start_jump = False
                vikram[0][0].inair = True
            jump = surface.jump(vikram)
        return jump
    
    def enemy_on_surface(jump):
        for index, vikram in enumerate(enemy_list):
            if not jump[index]:
                not_in_surface_temp = surface.on_surface(vikram, 0)
                
                for i in not_in_surface_temp:
                    if i not in not_in_surface:
                        not_in_surface.append(i)
                        
                if vikram not in not_in_surface_temp:
                    enemy_state[index][2] = False
                    if vikram in not_in_surface:
                        not_in_surface.remove(vikram)
                
                for i in not_in_surface:
                    if i == 'player' and 'player' in not_in_surface_temp:
                        for j in vikram:
                            for i in j:
                                i.rect.y += 3
                                #print('me')
                                if i.rect.y > 650:
                                    i.health_count -= 1
                                    i.rect.y = 0
            else:
                if vikram in not_in_surface:
                        not_in_surface.remove(vikram)

        
        '''if jump == []:
            e_not_in_surface_temp = surface.enemy_on_surface(enemy_list, 0)
            
            for i in e_not_in_surface_temp:
                if i not in e_not_in_surface:
                    e_not_in_surface.append(i)
            for e in range(len(enemy_list)):
                if e not in e_not_in_surface_temp:
                    #vikram_boolean[2] = False
                    if e in e_not_in_surface:
                        e_not_in_surface.remove(e)
            
                for i in e_not_in_surface:
                    if i in range(len(enemy_list)) and i in e_not_in_surface_temp:
                        for j in enemy_list[i]:
                            for k in j:
                                k.rect.y += 3
                                #print('me')
            print(e_not_in_surface_temp, e_not_in_surface)
        else:
            for i in range(len(enemy_list)):
                if i in e_not_in_surface:
                        e_not_in_surface.remove()'''
                        
    def on_surface(jump):
        #print(jump)
        #print(not_in_surface)
        if not jump:
            not_in_surface_temp = surface.on_surface(vikram, 0)
            
            for i in not_in_surface_temp:
                if i not in not_in_surface:
                    not_in_surface.append(i)
                    
            if vikram not in not_in_surface_temp:
                vikram_boolean[2] = False
                if vikram in not_in_surface:
                    not_in_surface.remove(vikram)
            
            for i in not_in_surface:
                if i == 'player' and 'player' in not_in_surface_temp:
                    for j in vikram:
                        for i in j:
                            i.rect.y += 3
                            #print('me')
                            if i.rect.y > 650:
                                i.health_count -= 1
                                i.rect.y = 0
        else:
            if vikram in not_in_surface:
                    not_in_surface.remove(vikram)
    e_inair = []
    def create_enemy(e_c_c, e_c_t):
        global enemy_creation_count, enemy_creation_time, ec, enemy_limit
        #print(e_c_c, e_c_t)
        if e_c_c > e_c_t and len(enemy_list) < enemy_limit:
             #print(1)
             enemy_creation_count = 0
             enemy_creation_time = random.randint(ec, ec+2)
             enemy_creation_location = random.randint(0,len(base_list)-1)
             location = base_list[enemy_creation_location]
             enemy_idle, enemy_run, enemy_jump, Death = [], [], [], []
             for i in range(5):
                enemy = PG.image.load('Resources\Images\Enemy\Idle\%d.png' % i)
                #print('Resources\Images\Vikram\Idle\%d.png' % i)
                enemy = R.Enemy(location.rect.x + (location.width // 2), location.rect.top, location, 0.7, 0, enemy, bullet_img, firing_img, vikram, screen, PG)
                enemy_idle.append(enemy)
                
             for i in range(6):
                enemy = PG.image.load('Resources\Images\Enemy\Run\%d.png' % i)
                #print('Resources\Images\Vikram\Run\%d.png' % i)
                enemy = R.Enemy(location.rect.x + (location.width // 2) , location.rect.top, location, 0.7, 0, enemy, bullet_img, firing_img, vikram, screen, PG)
                enemy_run.append(enemy)

             for i in range(2):
                enemy = PG.image.load('Resources\Images\Enemy\Jump\%d.png' % i)
                #print('Resources\Images\Vikram\Run\%d.png' % i)
                enemy = R.Enemy(location.rect.x + (location.width // 2) , location.rect.top, location, 0.7, 0, enemy, bullet_img, firing_img, vikram, screen, PG)
                enemy_jump.append(enemy)

             for i in range(8):
                enemy = PG.image.load('Resources\Images\Enemy\Death\%d.png' % i)
                enemy = R.Enemy(location.rect.x + (location.width // 2) , location.rect.top, location, 0.7, 0, enemy, bullet_img, firing_img, vikram, screen, PG)
                Death.append(enemy)

             enemy_idle[0].death = Death
             enemy_list.append([enemy_idle, enemy_run, enemy_jump, Death])
             enemy_state.append([False, True, False])
             e_start_jump.append(False)
             e_jump.append(False)
             e_inair.append(False)
             #print(*enemy_list, sep="\n\n")
        #print(ec, e_c_c, len(enemy_list))
             
    while running:
        clock.tick(FPS)
        enemy_creation_count += 1
        screen.blit(background_image,(-30,0))
        shoot = False
        for event in PG.event.get():
            
            if event.type == PG.QUIT:
                running = False
            #print(vikram[0][0].isalive)
            if vikram[0][0].isalive:
                if event.type == PG.KEYDOWN:
                    if event.key == PG.K_a or event.key == PG.K_LEFT:
                        moving_left = True
                        vikram_boolean[0] = False
                        vikram_boolean[1] = True
                    if event.key == PG.K_d or event.key == PG.K_RIGHT:
                        moving_right = True
                        vikram_boolean[0] = False
                        vikram_boolean[1] = True
                    if event.key == PG.K_f:
                        shoot = True
                    if event.key == PG.K_SPACE or event.key == PG.K_UP:
                        jump = True
                        if not vikram[0][0].inair:
                            start_jump = True
                        vikram_boolean[0] = False
                        vikram_boolean[1] = False
                        vikram_boolean[2] = True
                        
                if event.type == PG.KEYUP:
                    if event.key == PG.K_a or event.key == PG.K_LEFT:
                        moving_left = False
                        vikram_boolean[0] = True
                        vikram_boolean[1] = False
                    if event.key == PG.K_d or event.key == PG.K_RIGHT:
                        moving_right = False
                        vikram_boolean[0] = True
                        vikram_boolean[1] = False
                    
                keys=PG.key.get_pressed()
                if keys[PG.K_ESCAPE]:
                    Resume_page()
                if keys[PG.K_a] or keys[PG.K_LEFT] :
                    moving_left = True
                    vikram_boolean[0] = False
                    vikram_boolean[1] = True

                elif keys[PG.K_d] or keys[PG.K_RIGHT]:
                    moving_right = True
                    vikram_boolean[0] = False
                    vikram_boolean[1] = True

                elif keys[PG.K_SPACE] or keys[PG.K_UP]:
                    if not vikram[0][0].inair:
                        start_jump = True
                    jump = True
                    vikram_boolean[0] = False
                    vikram_boolean[1] = False
                    vikram_boolean[2] = True
                elif keys[PG.K_f]:
                    shoot = True
                    
                else:
                    moving_left = False
                    moving_right = False
                    vikram_boolean[0] = True
                    vikram_boolean[1] = False
                    vikram_boolean[2] = False
        if not vikram[0][0].isalive:
                vikram_boolean[0] = False
                vikram_boolean[1] = False
                vikram_boolean[2] = False
                
                
        #print(vikram_idle[0].rect.x,vikram_idle[0].rect.y, big_rock_1a.rect.x, big_rock_1a.rect.y, big_rock_1a.width )
        #print(vikram_boolean)
        enemy_on_surface(e_jump)
        on_surface(jump)
        jump = vikram_do_jump(jump)
        
        vikram_movement(moving_left, moving_right, shoot, base_list, vikram_idle, vikram_run,vikram_jump)
        Image_draw()
        create_enemy(enemy_creation_count, enemy_creation_time)
        PG.display.update()













def MainMenu():
    tmd = PG.font.Font(r'Resources\Fonts\TMD.ttf',24)
    main_menu_image = PG.image.load('Resources\Images\Main\Mainmenu Image.png')
    main_menu_image = PG.transform.scale(main_menu_image, (650,600))
    start_img = PG.image.load('Resources\Images\Main\play.png').convert_alpha()
    start_img = PG.transform.scale(start_img, (int(start_img.get_width() * 0.1), int(start_img.get_height() *0.1)))
    start_button = R.Button(640 , 480 , start_img, 'start', screen, PG)
    running = True
    while running:
        high_score = highscore()
        screen.fill((255,255,255))
        start_key = start_button.draw()
        if start_key:
            Game()
        for event in PG.event.get():
            if event.type == PG.QUIT:
                running = False
            if event.type == PG.KEYDOWN:
                if event.key == PG.K_RETURN:
                    Game()
        new_record = tmd.render("High Score : " + str(high_score),True,(0,0,0))
        screen.blit(new_record,[20,540])
        screen.blit(main_menu_image,(75, -20))
        PG.display.update()
        

MainMenu()

PG.quit()
