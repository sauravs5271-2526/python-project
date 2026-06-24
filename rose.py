import turtle
import colorsys

def create_unique_art():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("black")
    screen.tracer(10)
    screen.title("unique mirrored fractal mandala")
    
    
    turtles = []
    colors = [] 
    num_colors = 100
    
    for i in range(num_colors):
        oyp = colorsys.hsv_to_rgb(i / num_colors, 0.8, 1)
        colors.append(oyp)
    for i in range(4):
        new_t = turtle.Turtle()
        new_t.speed(0)
        new_t.width(2)
        new_t.hideturtle()
        turtles.append(new_t)
    
    for i in range(200):
        current_color = colors[i % num_colors]
        for index, t in enumerate(turtles):
            t.pencolor(current_color)
            angle_offset = index * 90
            
            
            t.penup()
            t.goto(0, 0) 
            t.setheading(angle_offset + (i * 2.5))
            t.pendown()
            
            
            t.circle(i * 1.2, 90)
            t.left(60)
            t.circle(i * 0.6, 90)   
   
    screen.update()
    screen.exitonclick() 
 
if __name__ == "__main__":
    create_unique_art()