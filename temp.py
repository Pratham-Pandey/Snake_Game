import pygame

pygame.init()
win=pygame.display.set_mode((800,600))
pygame.display.set_caption("Trial")

game=True
m1=0

while game==True:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        m1=pygame.mouse.get_pos()
    print(m1)
    win.fill((0,0,255))
    pygame.display.update()
