# Tasnim Sikder
# The Paint Project

""" A simple drawing program similar to Microsoft Paint. It allows the user to choose from a
 variety of tools such as pencil, brush, spray paint, to draw on the program. They are also
 free to utilise the stickers provided in the program and save their work as they please."""

from pygame import *
from random import *
from math import *
from tkinter import*
from tkinter import filedialog

root = Tk()             # this initializes the Tk engine
root.withdraw()         # hides the little window that pops up
undolist = []   # list for the canvas images for undo
redolist = []   # list for the canvas images for undo
points = []     # list for the polygon vertices




screen = display.set_mode((1000,700))   # screen size
background_pic = image.load("bg.png") # background picture loading
screen.blit(background_pic,(0,0))       # displays the background image

font.init()
comicFont = font.SysFont("Times New Roman", 17)   # sets font & size

draw.line(screen, (224,211,97), (0, 335), (250, 335), 5) # seperator line between tools and stamps

# All tool images are loaded here-----------------------------------
pen = image.load("pencil.png") # loads image from computer folder
screen.blit(pen,(15,50))  # displays image on program
eraser = image.load("eraser.png")
screen.blit(eraser,(90,50))
brush = image.load("brush.png")
screen.blit(brush,(170,50))
oval_fill = image.load("ovalfill.png")
screen.blit(oval_fill,(15,120))
oval_unfill = image.load("ovalunfill.png")
screen.blit(oval_unfill,(90,120))
line = image.load("line.png")
screen.blit(line,(170,120))
rect_fill = image.load("rectfill.png")
screen.blit(rect_fill,(15,190))
rect_unfill = image.load("rectunfill.png")
screen.blit(rect_unfill,(90,190))
spray = image.load("spray.png")
screen.blit(spray,(170,190))
calligraphy = image.load("calligraphy.png")
screen.blit(calligraphy,(15,260))
highlighter = image.load("highlighter.png")
screen.blit(highlighter,(90,260))
polygon = image.load("polygon.png")
screen.blit(polygon,(170,260))
undo = image.load("undo.png")
screen.blit(undo,(412,610))
redo = image.load("redo.png")
screen.blit(redo,(412,655))
eyedropper = image.load("eyedropper.png")
screen.blit(eyedropper,(462,632))
load = image.load("load.png")
screen.blit(load,(510,610))
save = image.load("save.png")
screen.blit(save,(510,655))
clear = image.load("clear.png")
screen.blit(clear,(560,627))

# loads images for stamps------------------------------------------------------------
moonmosque = image.load("moonmosque.png") # loads image from computer folder
moonmosquesmall = transform.scale(moonmosque,(60,60))  # transforms the stamp picture to the desired size
kettle = image.load("kettle.png")
kettlesmall = transform.scale(kettle,(60,60))
stars = image.load("stars.png")
starssmall = transform.scale(stars,(60,60))
lantern = image.load("lantern.png")
lanternsmall = transform.scale(lantern,(60,60))
quran = image.load("quran.png")
quransmall = transform.scale(quran,(60,60))
moon = image.load("moon.png")
moonsmall = transform.scale(moon,(60,60))

# this shows what color the mouse is on
circle = draw.circle(screen,(255,0,255),(125,590),94)  # creates a circle behind the color wheel for the mouse to hover over
c =(15,40,125) # the initial color that all the tools start with
size = 2 # initial size that all the tools start with

color_wheel = image.load("colorwheel.png") #loads the image for the color wheel
screen.blit(color_wheel,(-60,480))   # displays the color wheel

# Makes the rectangles for the tools, stamps and canvas-------------------------------------------
canvasRect = Rect(250,50,700,550)

pencilRect = Rect(15,50,60,60)
eraserRect = Rect(90,50,60,60)
brushRect = Rect(170,50,60,60)

ovalfillRect = Rect(15,120,60,60)
ovalunfillRect = Rect(90,120,60,60)
lineRect = Rect(170,120,60,60)

rectfillRect = Rect(15,190,60,60)
rectunfillRect = Rect(90,190,60,60)
sprayRect = Rect(170,190,60,60)

calligraphyRect = Rect(15,260,60,60)
highlighterRect = Rect(90,260,60,60)
polygonRect = Rect(170,260,60,60)


loadRect = Rect(510,610,35,35)
saveRect = Rect(510,655,35,35)

clearRect = Rect(560,627,50,50)
eyedropperRect = Rect(462,632,33,33)
undoRect = Rect(412,610,35,35)
redoRect = Rect(412,655,35,35)


moonmosqueRect = Rect(15,350,60,60)
kettleRect = Rect(90,350,60,60)
starsRect = Rect(170,350,60,60)
lanternRect = Rect(15,420,60,60)
quranRect = Rect(90,420,60,60)
moonRect = Rect(170,420,60,60)





mx,my = 0,0

draw.rect(screen,(255,255,255),canvasRect,0) #the drawing canvas


tool = "pencil"  # intial tool is set to pencil
back3 = screen.subsurface(canvasRect).copy()  # takes a picture of the empty canvas
undolist.append(back3)  # adds empty canvas picture to undo list

cover = Surface((50,50)).convert()  # make blank Surface
cover.set_alpha(9) # sets the transparency level
cover.fill((255,0,255)) 
cover.set_colorkey((255,0,255)) 
draw.line(cover,c,(mx,my+50),(mx,my-10),24) # draws the line

running = True
while running:
    click = False # initializes click variable
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONUP:
             back2 = screen.subsurface(canvasRect).copy()  # takes a picture of the canvas
             if mb[0]:
                if canvasRect.collidepoint(mx,my):  # if the user is drawing on the canvas
                    undolist.append(back2)  # it adds the picture with the drawings to the undolist
                    
        if e.type == MOUSEBUTTONDOWN:
            back = screen.copy() # takes a picture of the entire screen
            if e.button == 1:
                start = e.pos  # position of mouse
                click = True   # indicates mouse is clicked
            
    # Gets the mouse position
    mb = mouse.get_pressed()
    omx,omy = mx,my
    mx,my = mouse.get_pos()

    


   
    


    # THE RECTANGLES FOR ALL TOOLS AND STAMPS-----------------------------------------------    
    #The rectangles for the pencil and eraser tool (row 1)
    draw.rect(screen,(254,208,68),pencilRect,2)
    draw.rect(screen,(254,208,68),eraserRect,2)
    draw.rect(screen,(254,208,68),brushRect,2)

    #The rectangles for oval unfill, fill & line (row 2)
    draw.rect(screen,(254,208,68),ovalfillRect,2)
    draw.rect(screen,(254,208,68),ovalunfillRect,2)
    draw.rect(screen,(254,208,68),lineRect,2)
    
    #The rectangles for rectangle unfill, fill & spray (row 3)
    draw.rect(screen,(254,208,68),rectfillRect,2)
    draw.rect(screen,(254,208,68),rectunfillRect,2)
    draw.rect(screen,(254,208,68),sprayRect,2)

    # The rectangles for calligraphy, highlighter and polygon
    draw.rect(screen,(254,208,68),calligraphyRect,2)
    draw.rect(screen,(254,208,68),polygonRect,2)
    draw.rect(screen,(254,208,68),highlighterRect,2)
    
    #The blue background color for all the stamp buttons
    draw.rect(screen,(10,27,78),moonmosqueRect)
    draw.rect(screen,(10,27,78),kettleRect)
    draw.rect(screen,(10,27,78),starsRect)
    draw.rect(screen,(10,27,78),lanternRect)
    draw.rect(screen,(10,27,78),quranRect)
    draw.rect(screen,(10,27,78),moonRect)
    
    #Displays the small stamp pictures on the buttons
    screen.blit(moonmosquesmall, moonmosqueRect)
    screen.blit(kettlesmall, kettleRect)
    screen.blit(starssmall, starsRect)
    screen.blit(lanternsmall, lanternRect)
    screen.blit(quransmall, quranRect)
    screen.blit(moonsmall, moonRect)

    # The rectangles for the stamps
    draw.rect(screen,(254,208,68),moonmosqueRect,2)
    draw.rect(screen,(254,208,68),kettleRect,2)
    draw.rect(screen,(254,208,68),starsRect,2)
    draw.rect(screen,(254,208,68),lanternRect,2)
    draw.rect(screen,(254,208,68),quranRect,2)
    draw.rect(screen,(254,208,68),moonRect,2)

    # The rectangles for the rest of the tools
    draw.rect(screen,(254,208,68),loadRect,2)
    draw.rect(screen,(254,208,68),saveRect,2)
    draw.rect(screen,(254,208,68),clearRect,2)
    draw.rect(screen,(254,208,68),eyedropperRect,2)
    draw.rect(screen,(254,208,68),undoRect,2)
    draw.rect(screen,(254,208,68),redoRect,2)
    

#THICKNESS SIZE CIRCLES-----------------------------------------------------------
    size_1 = draw.circle(screen,(254,208,68),(228,650),9)
    size_2 = draw.circle(screen,(254,208,68),(253,650),13)
    size_3 = draw.circle(screen,(254,208,68),(286,650),17)
    size_4 = draw.circle(screen,(254,208,68),(328,650),21)
    size_5 = draw.circle(screen,(254,208,68),(380,650),27)   
    
    
    


        
    # Selects the tool based on mouse click---------------------------------------------
    if pencilRect.collidepoint(mx,my): # if the mouse is on the pencil button rectangle
        draw.rect(screen,(136,188,235),pencilRect,2)  # hover highlight colors
        if click:  # if mouse is clicked
            tool = "pencil"  # the tool will become pencil
    if tool == "pencil":
        draw.rect(screen,(63,137,201),pencilRect,2)  #selected highligt
        
                
    if eraserRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),eraserRect,2)
        if click:
            tool = "eraser"     
    if tool == "eraser":       
        draw.rect(screen,(63,137,201),eraserRect,2)
                

    if brushRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),brushRect,2)
        if click:
            tool = "brush"
    if tool == "brush":        
        draw.rect(screen,(63,137,201),brushRect,2)


    if ovalfillRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),ovalfillRect,2)
        if click:
            tool = "oval fill"
    if tool == "oval fill":        
        draw.rect(screen,(63,137,201),ovalfillRect,2)

    if ovalunfillRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),ovalunfillRect,2)
        if click:
            tool = "oval unfill"
    if tool == "oval unfill":        
        draw.rect(screen,(63,137,201),ovalunfillRect,2)
                

    if lineRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),lineRect,2)
        if click:
             tool = "line"
    if tool == "line":         
        draw.rect(screen,(63,137,201),lineRect,2)

    if rectfillRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),rectfillRect,2)
        if click:
            tool = "rect fill"
    if tool == "rect fill":        
        draw.rect(screen,(63,137,201),rectfillRect,2)

    if rectunfillRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),rectunfillRect,2)
        if click:
            tool = "rect unfill"
    if tool == "rect unfill":        
        draw.rect(screen,(63,137,201),rectunfillRect,2)

    if sprayRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),sprayRect,2)
        if click:
            tool = "spray"
    if tool == "spray":        
        draw.rect(screen,(63,137,201),sprayRect,2)


    if clearRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),clearRect,2)
        if click:
            draw.rect(screen,(63,137,201),clearRect,2)
            draw.rect(screen,(255,255,255), canvasRect)  # clears the canvas by drawing a white rectangle of canvas size
            points = [] # clears the vertices for the polygon tool if clear is done

    if eyedropperRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),eyedropperRect,2)
        if click:
            tool = "eyedropper"
    if tool == "eyedropper":        
        draw.rect(screen,(63,137,201),eyedropperRect,2)


    if calligraphyRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),calligraphyRect,2)
        if click:
            tool = "calligraphy"
    if tool == "calligraphy":        
        draw.rect(screen,(63,137,201),calligraphyRect,2)

    
    if highlighterRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),highlighterRect,2)
        if click:
            tool = "highlighter"
    if tool == "highlighter":        
        draw.rect(screen,(63,137,201),highlighterRect,2)

    if polygonRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),polygonRect,2)
        if click:
            tool = "polygon"
    if tool == "polygon":        
        draw.rect(screen,(63,137,201),polygonRect,2)
        draw.rect(screen,(224,211,97),(650,620,301,60),3) # draws the pop up text rectangle when polygon is selected
        txtPic = comicFont.render("Right click to connect and end polygon", True, (224,211,97)) # writes the instructions
        screen.blit(txtPic,(660,640)) # displays the text above (instructions for polygon)

    if tool != "polygon": # checks if the tool is no longer polygon
        draw.rect(screen,(0,0,0),(650,620,301,60)) # draws a black rectangle over the pop up instruction text
        

    if circle.collidepoint(mx,my): # checks if the cursor is on the color wheel
        if click: # if the mouse is clicked
            c = screen.get_at((mx,my)) # it gets the color of where the mouse pos is
    draw.circle(screen,c,(125,590),100,10) # changes the ring around the color wheel to the color that was selected

    # The hovering and selected tool highlight for stamps--------------------------------
    if moonmosqueRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),moonmosqueRect,2)  
        if click:
            tool = "moon mosque"
    if tool == "moon mosque":
        draw.rect(screen,(63,137,201),moonmosqueRect,2)

    if kettleRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),kettleRect,2)  
        if click:
            tool = "kettle"
    if tool == "kettle":
        draw.rect(screen,(63,137,201),kettleRect,2)

    if starsRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),starsRect,2)  
        if click:
            tool = "stars"
    if tool == "stars":
        draw.rect(screen,(63,137,201),starsRect,2)

    if lanternRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),lanternRect,2)  
        if click:
            tool = "lantern"
    if tool == "lantern":
        draw.rect(screen,(63,137,201),lanternRect,2)

    if quranRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),quranRect,2)  
        if click:
            tool = "quran"
    if tool == "quran":
        draw.rect(screen,(63,137,201),quranRect,2)

    if moonRect.collidepoint(mx,my):
        draw.rect(screen,(136,188,235),moonRect,2)  
        if click:
            tool = "moon"
    if tool == "moon":
        draw.rect(screen,(63,137,201),moonRect,2)
        
    # The following few lines change the size based of what sized circle is clicked on-----
    if size_1.collidepoint(mx,my):
        if click:
            size = 3

    if size_2.collidepoint(mx,my):
        if click:
            size = 7

    if size_3.collidepoint(mx,my):
        if click:
            size = 11

    if size_4.collidepoint(mx,my):
        if click:
            size = 16

    if size_5.collidepoint(mx,my):
        if click:
            size = 22

    # UNDO AND REDO CODE BELOW--------------------------------------------------------------        
    if undoRect.collidepoint(mx,my): # checks if the mouse is on the undo button
        draw.rect(screen,(136,188,235),undoRect,2) # draws a highlight color for hovering over the button
        if click: # checks if mouse button is clicked on the undo button
            draw.rect(screen,(63,137,201),undoRect,2) # draws the selected highlight color rectangle
            if len(undolist)> 1: # checks if there are new images in the undo list
                screen.blit((undolist[-2]), canvasRect) # displays the the canvas image that is 2nd last in the list ()
                redolist.append(undolist.pop()) # moves the canvas image from the undo list to the redo list (removes from undo)

    
    if redoRect.collidepoint(mx,my):# checks if the mouse is on the redo button
        draw.rect(screen,(136,188,235),redoRect,2)
        if click: # checks if the redo button is clicked
            if len(redolist)> 0: # checks if there are any images in the redo list
                draw.rect(screen,(63,137,201),redoRect,2) # draws the selected tool highlight rectangle
                screen.blit((redolist[-1]), canvasRect) # displays the last image in the redo list onto the canvas
                undolist.append(redolist.pop()) # moves the image to undolist from redolist
      

        
    #-------------------------------------------------------
    if loadRect.collidepoint(mx,my):  # checks if the cursor is on the load button
        draw.rect(screen,(136,188,235),loadRect,2) # shows the hover highlight
        if click: # checks if the mouse button is clicked...
            load_result = filedialog.askopenfilename(filetypes = [("Picture files", "*.png;*.jpg")]) #opens file dialog
            if load_result != "": # cheks if a file is selected
                load = image.load(load_result) # it loads the selected image
                screen.set_clip(canvasRect) # sets the clipping area to be the canvas
                screen.blit(load,(canvasRect)) # loads the image onto the canvas
                screen.set_clip(None)  # resets the clipping
           
            
    if saveRect.collidepoint(mx,my): # checks if the cursor is on the save button
        draw.rect(screen,(136,188,235),saveRect,2)  # shows the hover highlight
        if click: # checks if save button is clicked
            save_result = filedialog.asksaveasfilename() # opens the dialog to save a file
            if save_result != "": # checks if the file was named
                image.save((screen.subsurface(canvasRect)),save_result) # saves the file
          
        

    
     
               
        

            
    # Draws on the canvas if the mouse is clicked in the area of the canvas---------------    
    if mb[0] and (canvasRect.collidepoint(mx,my) or canvasRect.collidepoint(omx,omy)): # checks if the mouse button is pressed on the canvas
        screen.set_clip(canvasRect) # sets the clipping area to the canvas
        if len(redolist) > 0 : # checks if there are images in the redo list
            redolist=[] # clears the redo list if something new is drawn
            
        if tool == "pencil": # checks if tool is pencil
            draw.line(screen, c, (omx, omy), (mx, my), 2) # draws a simple line
            
        elif tool == "eraser":
            ex = mx-omx # gets the x vector distance from last x point to new x point
            ey = my-omy # gets the  vector distance from last y point to new y point
            e = hypot(ex,ey) # gets the distance of the hypotenuse
            for r in range(int(e)): 
                ex2 = omx + ex*r/e # gets the x coordinate along the path of the eraser
                ey2 = omy + ey*r/e # gets the y coordinate along the path of the eraser
                draw.circle(screen, (255, 255, 255), (ex2, ey2), size) # draws a white circle (the eraser)
            draw.circle(screen, (255, 255, 255), (mx, my), size) # draws the eraser when the mouse is pressed but doesn't move

        # SAME CODE AS ERASER TOOL
        elif tool == "brush":
            dx = mx-omx
            dy = my-omy
            d = hypot(dx,dy)
            for i in range(int(d)):
                x = omx + dx*i/d
                y = omy + dy*i/d
                draw.circle(screen, c, (x, y), size)
            draw.circle(screen, c, (mx, my), size)

        elif tool == "oval fill":
            screen.blit(back, (0,0))
            ex = mx-start[0] # gets the width of the oval
            ey = my-start[1] # gets the height of the oval
            ova = Rect(start[0], start[1],ex,ey) # makes a rectangle that suits the size of the oval
            ova.normalize() # allows the user to draw the shape in any direction of desire
            draw.ellipse(screen,c,ova) # draws the oval

        # CODE IS SAME AS OVAL FILL
        elif tool == "oval unfill":
            screen.blit(back, (0,0))
            ex2 = mx-start[0]
            ey2 = my-start[1]
            ova2 = Rect(start[0], start[1],ex2,ey2)
            ova2.normalize()
            draw.ellipse(screen,c,ova2,size)

        elif tool == "line":
            screen.blit(back, (0,0))
            draw.line(screen, c, start, (mx, my), size) # draws a line from the starting point to the current mouse pos
                

        elif tool == "rect fill":
            screen.blit(back, (0,0))
            rx = mx-start[0]   # gets the width of the rectangle
            ry = my-start[1]   # gets the height of the rectangle
            rec = Rect(start[0], start[1],rx,ry) # makes a rectangle that suits the size the user created
            rec.normalize() # allows the user to draw the shape in any direction of desire
            draw.rect(screen,c,rec) # draws the rectangle

        # CODE IS SAME AS RECT FILL
        elif tool == "rect unfill":
            screen.blit(back, (0,0))
            rx2 = mx-start[0]
            ry2 = my-start[1]
            rec2 = Rect(start[0], start[1],rx2,ry2)
            rec2.normalize()
            draw.rect(screen,c, rec2,size)

        elif tool == "spray":
            x = randint(-20,20) # generates a  random x point from the range -20 to 20
            y = randint(-20,20) # generates arandom y point from the range -20 to 20
            radius = size # sets the spray radius size to whatever size is currently selected
            dist = hypot(x,y) # calculates the distance 
            if dist < radius: # checks if the distance is less than the radius size 
                draw.circle(screen, c, (mx+x, my+y), 2) # draws that circle
    

        elif tool == "eyedropper":
            c = screen.get_at((mx,my)) # gets the color at the mouse position when it is click ont the canvas

        # CODE IS SAME AS BRUSH AND ERASER
        elif tool == "calligraphy":
            gx = mx-omx
            gy = my-omy
            dg = hypot(gx,gy)*2
            for g in range(int(dg)):
                xx = omx + gx*g/dg
                yy = omy + gy*g/dg
                draw.line(screen, c, (xx+size, yy-size), (xx-size, yy+size), 3)
            draw.line(screen, c, (mx+size, my-size), (mx-size, my+size), )

        elif tool == "highlighter":
            screen.blit(cover,(mx-5,my-5))
            draw.line(cover,c,(mx+size,my-size),(mx+size,my-size),24)

            
        elif tool == "moon mosque":
            screen.blit(back, (0,0))
            screen.blit(moonmosque, (mx-60,my-60)) # centers the stamp on mouse pos

        elif tool == "kettle":
            screen.blit(back, (0,0))
            screen.blit(kettle, (mx-60,my-60))

        elif tool == "stars":
            screen.blit(back, (0,0))
            screen.blit(stars, (mx-60,my-60))

        elif tool == "lantern":
            screen.blit(back, (0,0))
            screen.blit(lantern, (mx-60,my-60))

        elif tool == "quran":
            screen.blit(back, (0,0))
            screen.blit(quran, (mx-60,my-60))

        elif tool == "moon":
            screen.blit(back, (0,0))
            screen.blit(moon, (mx-60,my-60))


# COOL THING- that i accidentally made in the process of making polygon code, wanted to show you but forgot to :D
##            elif tool == "polygon":
##                if click:
##                    points.append((mx,my))
##                    print(points)
##                if len(points) >= 3:
##                    for i in range(len(points)):
##                        start_vertex = points[i]
##                    
##                        draw.line(screen, c, start_vertex, (mx,my), size)
            
        




        elif tool == "polygon":
            if click:  # when the mouse button is clicked
                points.append((omx,omy))  # it adds the current mouse pos to a list
                
                
                if len(points) > 1:   # if there are more than one points in the list
                    for i in range(len(points)-1):  # loop through all points except the last one to prevent index erroe
                        start_vertex = points[i] # makes start vertex the first point
                        end_vertex = points[i+1] # makes end vertex the next point                   
                        draw.line(screen, c, start_vertex, end_vertex, size)
                        
    if mb[2] and len(points) >= 1: # checks if right mouse button is pressed and if theres more than 1 vertices in the points list
        draw.line(screen, c, points[-1], points[0], size) # draws a line connecting the last vertex to the first vertex
        points = [] # clears the polygon vertices 

        
            

    screen.set_clip(None) 

    display.flip()



quit()
