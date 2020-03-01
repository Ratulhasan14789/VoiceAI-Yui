from turtle import *
color('green', 'blue')
def Circle():
	#draw circle
    begin_fill()
    while True:
        forward(2)
        left(1)
        if abs(pos()) < 1:
            break
    end_fill()
    done()

def triangle():
    begin_fill()
    while True:
        forward(200)
        left(120)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    
def hexagon():
    begin_fill()
    while True:
        backward(200)
        left(60)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    
def line():
    begin_fill()
    while True:
        forward(200)
        left(180)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    
def square():
    begin_fill()
    while True:
        forward(200)
        left(270)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
"""begin_fill()
while True:
    forward(200)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()"""
#hexagon()
def convex_poly(n):
    x=90-180/n
    begin_fill()
    while True:
        forward(200)
        left(180-2*x)
        if abs(pos()) < 1:
            break
    end_fill()
    done()
    
#####################
#just put the number of gons in the pqrentesis
#####################
convex_poly(5)