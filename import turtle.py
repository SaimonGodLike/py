from turtle import*
Screen(), title("рисовашки"), pensize(2), color("black"), speed(1000), fillcolor("yellow")
def star(t, size):
    for i in range(6): forward(size), right(120), forward(size), left(60)
def squere(t, size):
    for i in range(4): forward(size), right(90)
penup(), goto(0,0), pendown(), star(0, 10), penup(), goto(50,-5), pendown(),  begin_fill(), squere(0, 20), end_fill(), penup(), goto(75,20), pendown(), squere(0, 20), penup(), goto(50,-5), pendown() ,squere(0, 20), penup(), goto(-10,-40), pendown(), begin_fill(), squere(0, 100), end_fill(), penup(), goto(30,-25), pendown(), squere(0, 15), penup(), goto(120,20), pendown(), squere(0, 50),penup(), goto(120,-120), pendown(), begin_fill(), goto(120,-50), goto(170,-120), goto(120,-120), end_fill(), penup(), goto(-10,-90), pendown(), forward(100), goto(90,-140), goto(20,-140), left(90) ,forward(100) ,right(90) ,forward(40) ,right(90), forward(100), penup()
def coloring(t, coordinates, fill_color):
    fillcolor(fill_color), penup()
    fcoord = coordinates[0]
    goto(fcoord[0], fcoord[1]), pendown(), begin_fill()
    for coord in coordinates[1:]: goto(coord[0], coord[1])
    goto(fcoord[0], fcoord[1]), end_fill(), penup()  
coord = [(20, -90), (60, -90), (60, -40), (20, -40)]
coloring(0, coord, "black")
coord = [(20,-140), (-10,-140), (-10,-90), (20,-90)]
coloring(0, coord, "black")
coord = [(90,-140), (60,-140), (60,-90), (90,-90)]
coloring(0, coord, "black"), done()