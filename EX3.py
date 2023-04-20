class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
   
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
                

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)

class InputBox_num(InputBox):
    def handle_event(self, event):
        
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
   
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else :
                    if event.unicode.isnumeric(): #ถ้าที่keyไปเป็น number (True)
                        self.text += event.unicode
                    
                        
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

class Rectangle:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,(120,20,220),(self.x,self.y,self.w,self.h))

class Button(Rectangle):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rectangle.__init__(self, x, y, w, h)
    def isMouseOn(self):
        if pg.mouse.get_pos()[0] > (self.x) and pg.mouse.get_pos()[0] < (self.x+self.w) and pg.mouse.get_pos()[1] > (self.y) and pg.mouse.get_pos()[1] < (self.y+self.h) :
            return True 
import sys
import pygame as pg

pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
make_rec = Button(600,230,100,100)

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 32)

input_box1 = InputBox(250, 100, 140, 32) # สร้าง InputBox1
input_box2 = InputBox(250, 200, 140, 32) # สร้าง InputBox2
input_box3 = InputBox_num(250, 300, 140, 32) # สร้าง InputBox2
input_boxes = [input_box1, input_box2, input_box3] # เก็บ InputBox ไว้ใน list เพื่อที่จะสามารถนำไปเรียกใช้ได้ง่าย

#Text Name
font = pg.font.Font('freesansbold.ttf', 32) # font and fontsize
text = font.render('Name', True, (120,20,220)) # (text,is smooth?,letter color,background color)
text_name = text.get_rect() # text size
text_name.center = (100,115)
#Text Lastname
text2 = font.render('Lastname', True, (120,20,220)) 
text_lastname = text.get_rect() 
text_lastname.center = (100,215)

#Text Lastname
text3 = font.render('Age', True, (120,20,220)) 
text_num = text.get_rect() 
text_num.center = (100,315)

#Text submit
text4 = font.render('Submit', True, (0,0,0)) 
text_sub = text.get_rect() 
text_sub.center = (640,200)
while 1:
  
    screen.fill((255, 255, 255))
    screen.blit(text, text_name)
    screen.blit(text2, text_lastname)
    screen.blit(text3, text_num)
    screen.blit(text4, text_sub)
  
    if make_rec.isMouseOn():
       if pg.mouse.get_pressed(num_buttons=3) == (1,0,0):
        txt = FONT.render("Hello " + input_box1.text + " "+ input_box2.text + " You are " + input_box3.text + " years old.", True, (120,20,220))
        screen.blit(txt, (100,400))
    make_rec.draw(screen)
    
    for box in input_boxes: # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update() # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen) # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen
        
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
      
    
    pg.time.delay(1)
    pg.display.update()