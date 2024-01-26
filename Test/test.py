import turtle

# 设置画布
screen = turtle.Screen()
screen.title("Turtle Heart")

# 创建一个画笔
pen = turtle.Turtle()
pen.color("red")
pen.begin_fill()

# 画爱心
pen.left(140)
pen.forward(224)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)

pen.end_fill()
pen.hideturtle()

# 保持画布打开状态
screen.mainloop()
