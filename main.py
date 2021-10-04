import pygame
import random

#Initializing Pygame and Music
pygame.init()
pygame.mixer.init()

class snake:
    def __init__(self):
        # Movement Related Variables
        self.diff_x=0
        self.diff_y=0

        #Snake position and size
        self.obj_x=200
        self.obj_y=200
        self.obj_size=20

    def dis(self, snake_size, snake_list):
        for xy in snake_list:
            pygame.draw.rect(win, green, [xy[0], xy[1], self.obj_size, self.obj_size])
class apple:
    def __init__(self):
        self.apple_x=100
        self.apple_y=100
        self.size=20

    def dis(self):
        pygame.draw.rect( win,red, [self.apple_x, self.apple_y, self.size, self.size])

class boundary:
    def __init__(self):
        self.width=20

    def bound_calc(self,var):
            n = var
            bound_final = 0
            c = 0

            while n > 0:
                bound_mid = n % 10
                if c > 0:
                    bound_final = bound_final * 10 + bound_mid
                n = n // 10
                c = c + 1

            bound_mid = 0
            bound_super_final = 0

            while bound_final > 0:
                bound_mid = bound_final % 10
                bound_super_final = bound_super_final * 10 + bound_mid
                bound_final = bound_final // 10

            return var//bound_super_final

    def disp(self):
        pygame.draw.rect(win, black, [0, 0, self.bound_calc(x), y])
        pygame.draw.rect(win, black, [0, 0, x, self.bound_calc(y)])
        pygame.draw.rect(win, black, [0, y-self.bound_calc(y), x, self.bound_calc(y)])
        pygame.draw.rect(win, black, [x-(self.bound_calc((x))*30), 0, self.bound_calc(x)*30, y])

class button:
    def __init__(self, x, y, color_1, color_2, button_width):
        self.x=x
        self.y=y

        self.width=button_width
        self.height=70

        self.diff=10

        self.color_1=color_1
        self.color_2=color_2

        self.mouse_click = pygame.mouse.get_pressed()
        self.mou_pos= pygame.mouse.get_pos()


    def disp(self, operation):
        global game_over
        global menu_on
        global credits

        #Loading Sound Effects
        hover_sound = pygame.mixer.Sound('hover.wav')
        click_sound = pygame.mixer.Sound('click_sound.wav')

        pygame.draw.rect(win, black, [self.x, self.y, self.width, self.height])

        box=pygame.draw.rect(win, self.color_1, [self.x + self.diff, self.y + self.diff, self.width - self.diff*2, self.height - self.diff*2])
        if self.mou_pos[0] > self.x + self.diff and self.mou_pos[0] < self.x + self.width - self.diff and self.mou_pos[1] > self.y + self.diff and self.mou_pos[1] < self.y + b1.height - self.diff:
            box = pygame.draw.rect(win, self.color_2, [self.x + self.diff, self.y + self.diff, self.width - self.diff * 2, self.height - self.diff * 2])
            hover_sound.play(0)

            if self.mouse_click[0] == True:
                click_sound.play(0)
                if operation == 1:
                    game_over = False


                elif operation==2:
                    credits = True
                    menu_on = False

                elif operation == 3:
                    pygame.quit()
                    quit()

                elif operation == 4:
                    credits = False
                    menu_on = True

class text:
    def disp(self, message, size, color, pos_x, pos_y):
        font = pygame.font.SysFont("segoe print", size, True)
        display_text = font.render(message, True, color)
        win.blit(display_text,[pos_x,pos_y])

quit_game = False
game_over = True
menu_on = True
retry = False
pause = False
credits = False

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
green = (0, 175, 0)
light_green = (0, 255, 0)
midnight_blue = (0,255,255)
orange = (255,140,0)
gold = (255, 215, 0)
maroon = (128, 0, 0)
yellowgreen = (154, 205, 50)
seablue = (0, 105, 148)
magenta = (255, 0, 255)

win=pygame.display.set_mode()
x,y=win.get_size()

snake_list=[]
snake_size=5

print("X=",x,"Y=",y)
test3=102

pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

pygame.mixer.music.load('music1.mp3')
pygame.mixer.music.play(-1)

while quit_game == False:
    obj_1 = snake()
    apple_obj = apple()
    draw_bound = boundary()

    score = 0

    snake_list = []

    button_width = 200
    button_x = x/2-(button_width/2)

    b1 = button(button_x, y/2, orange,midnight_blue, button_width)
    text_1 = text()

    b2 = button(button_x, y/2+100, orange, midnight_blue, button_width)
    text_2 = text()

    b3 = button(button_x, y/2+200, orange, midnight_blue, button_width)
    text_3 = text()

    text_retry_screen = text()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game=True

    if menu_on == True:
        win.fill(maroon)
        b1.disp(1)
        text_1.disp("Play", 40, red, button_x+55, y/2 )
        b2.disp(2)
        text_2.disp("Credits", 40, red, button_x+30, y/2+102)
        b3.disp(3)
        text_3.disp("Quit", 40, red, button_x+55, y/2+202)

        print(game_over)

    elif credits == True:
        win.fill(maroon)
        b_bttn_text=text()
        b_bttn_text.disp("Instructions: ", 50, yellowgreen, x / 3+100, 100)
        b_bttn_text.disp("Press 'Esc' To pause and 'p' to resume ", 50, midnight_blue, x / 4, 150)

        b_bttn_text.disp("Created By", 50, yellowgreen, x/3+100 , 300)
        b_bttn_text.disp("Pratham Pandey", 50, midnight_blue, x / 3+20, 350)
        b_bttn_text.disp("Music", 50, yellowgreen, x / 3+100, 500)
        b_bttn_text.disp("LINK", 50, midnight_blue, x / 3, 550)


        b_bttn=button(100, y-100, orange, midnight_blue, 200 )
        b_bttn.disp(4)
        b_bttn_text.disp("Back", 35, maroon, 150, y-100)

    elif retry == True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_over=False
                menu_on=False
                retry=False
            elif event.key == pygame.K_BACKSPACE:
                menu_on=True
                game_over=True
                retry=False

        win.fill(maroon)
        text_retry_screen.disp("Press Enter To Retry and Backspace To Go To Menu", 45, yellowgreen, x/11, y / 2)

    pygame.display.update()
    clock.tick(15)

    restrict_movment = [1, 1, 1, 1]

    while game_over == False:
        current_score_x = 1200
        current_score_y = 200

        high_score_x = 1160
        high_score_y = 500
        current_score_radius = 30
        score=str(score)
        current_score_text = text()
        high_score_text = text()

        current_score_text1 = text()
        high_score_text1 = text()

        win.fill(gold)
        apple_obj.dis()
        obj_1.dis(snake_size, snake_list)
        draw_bound.disp()

        # File Handling
        f = open("h_score.txt", "r")
        h_score = f.read()

        #Loading Sound Effects
        eat_sound = pygame.mixer.Sound('sound1.mp3')
        game_over_sound = pygame.mixer.Sound('game_over.wav')

        pygame.draw.rect(win, midnight_blue, pygame.Rect(high_score_x, current_score_y, 100, 50), 0, 5)
        current_score_text.disp(score, 45, magenta, current_score_x - 30, current_score_y -20)
        current_score_text1.disp("Score", 45, orange, current_score_x - 50, current_score_y - 70)


        pygame.draw.rect(win, midnight_blue, pygame.Rect(high_score_x, high_score_y, 115, 50), 0, 5)
        high_score_text.disp(h_score, 45, magenta, high_score_x+ 7, high_score_y-15)
        high_score_text1.disp("High-Score", 45, orange, high_score_x - 50, high_score_y -75)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game=True
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if restrict_movment[0] == 1:
                    if event.key == pygame.K_LEFT:
                        obj_1.diff_x = -10
                        obj_1.diff_y = 0
                        restrict_movment = [1,1,1,0]

                if restrict_movment[3] == 1:
                    if event.key == pygame.K_RIGHT:
                        obj_1.diff_x = 10
                        obj_1.diff_y = 0
                        restrict_movment = [0,1,1,1]

                if restrict_movment[2] == 1:
                    if event.key == pygame.K_DOWN:
                        obj_1.diff_y = 10
                        obj_1.diff_x = 0
                        restrict_movment = [1,0,1,1]
                if restrict_movment[1] == 1:
                    if event.key == pygame.K_UP:
                        obj_1.diff_y = -10
                        obj_1.diff_x = 0
                        restrict_movment = [1,1,0,1]

                if event.key == pygame.K_ESCAPE:
                    temp_diff_x = obj_1.diff_x
                    temp_diff_y = obj_1.diff_y
                    pause = True

                while pause == True:

                    obj_1.diff_x = 0
                    obj_1.diff_y = 0

                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_p:
                                pause=False
                                obj_1.diff_x = temp_diff_x
                                obj_1.diff_y = temp_diff_y

        if obj_1.obj_x == apple_obj.apple_x and obj_1.obj_y == apple_obj.apple_y:
            apple_obj.apple_x = int(round(random.randrange(draw_bound.bound_calc(x), x-(draw_bound.bound_calc(x) * 30) - apple_obj.size) / 10.0) * 10.0)
            apple_obj.apple_y = int(round(random.randrange(draw_bound.bound_calc(y), y-draw_bound.bound_calc(y) - apple_obj.size) / 10.0) * 10.0)
            snake_size += 1
            score = int(score)+1
            eat_sound.play(0)

            if score>int(h_score):
                h_score = score

        obj_1.obj_x += obj_1.diff_x
        obj_1.obj_y += obj_1.diff_y

        if obj_1.obj_x+obj_1.obj_size > x-(draw_bound.bound_calc((x))*30) or obj_1.obj_x < draw_bound.bound_calc(x) or obj_1.obj_y+obj_1.obj_size > y-draw_bound.bound_calc(y) or obj_1.obj_y < draw_bound.bound_calc(y):
            retry = True
            game_over = True
            menu_on = False
            game_over_sound.play(0)

        snake_head = []
        snake_head.append(obj_1.obj_x)
        snake_head.append(obj_1.obj_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_size:
            del snake_list[0]

        if snake_size >= 6:
            if snake_head in snake_list[:len(snake_list)-2]:
                snake_size = 5
                game_over = True
                menu_on = False
                retry = True

        f = open("h_score.txt", "w")
        f.write(str(h_score))
        print("H_SCORE: ", h_score)
        f.close()

        pygame.display.update()
        clock.tick(15)

pygame.quit()
quit()

