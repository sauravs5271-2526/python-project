from turtle import * 
import colorsys
speed(70)
bgcolor("black")

h = 10

for i in range(16):
     for j in range(8):
         c = colorsys.hsv_to_rgb(h,  1, 1)
         color(c)
         h += 0.005
         
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)    
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)   
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90) 
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
         rt(360)
         circle(150 - j * 6, 90)
         lt(90)
         circle(150 - j * 6, 90)
        
        
        
        


circle(40, 24)
    

done()