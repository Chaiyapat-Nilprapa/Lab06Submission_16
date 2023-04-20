class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))
import sys 
import pygame as pg
pg.init()
run = True
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
make_rec = Rectangle(400,240,100,100)

while(run):
    screen.fill((255, 255, 255))
    make_rec.draw(screen) #สั่งวาดใน screen
    for event in pg.event.get(): #ตรวจหา event
        print (event)
        
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.KEYUP and event.key == pg.K_w: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key W up")
            make_rec.y -= 10

        if event.type == pg.KEYUP and event.key == pg.K_a: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key A left")
            make_rec.x -= 10

        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            print("Key D right")
            make_rec.x += 10
           
        if event.type == pg.KEYUP and event.key == pg.K_s: #ปุ่มถูกปล่อยและเป็นปุ่ม A
            print("Key S down")
            make_rec.y += 10
    pg.display.update()
   
