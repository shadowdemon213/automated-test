import turtle

# =====================================================
# КОНСТАНТЫ
# =====================================================

# СОЛНЫШКО
SUN_LINES_COLOR = "orange"
SUN_LINES_WIDTH = 6
COUNT_OF_SUN_LINES = 16
SUN_LINE_X = 300
SUN_LINE_Y = 250
BETWEEN_SUN_LINES = 22.5
LINES_LENGTH = 90
SUN_CENTER_X = 280
SUN_CENTER_Y = 195
SUN_COLOR = "yellow"
SUN_RADIUS = 60

# ОБЛАКО
CLOUD_COLOR = "white"
CORDS = [
    (100, 280, 40),
    (70, 290, 30),
    (130, 290, 30),
    (50, 270, 25),
    (150, 270, 25),
    (100, 260, 35)
]

# ЦВЕТОК
STEM_COLOR = "darkgreen"
STEM_WIDTH = 4
STEM_START_X = 0
STEM_START_Y = -400
FLOWER_DIRECTION = 90
STEM_LENGTH = 180
PETAL_CENTER_X = 0
PETAL_CENTER_Y = -185
PETAL_ANGLE = 45
PETAL_RADIUS = 30
PETAL_EXTENT = 180
CORE_CENTER_X = -15
CORE_CENTER_Y = -200
CORE_COLOR = "yellow"
CORE_RADUIS = 20

# ДЕКОР
MARCH_TEXT_CENTER_X = 0
MARCH_TEXT_CENTER_Y = 15
MARCH_TEXT_COLOR = "purple"
MARCH_TEXT_THICKNESS = 36
WOMAN_TEXT_CENTER_X = 0
WOMAN_TEXT_CENTER_Y = -12
WOMAN_TEXT_COLOR = "deeppink"
WOMAN_TEXT_THICKNESS = 20
DAY_TEXT_CENTER_X = 0
DAY_TEXT_CENTER_Y = -37
DAY_TEXT_COLOR = "blue"
DAY_TEXT_THICKNESS = 14
# Сердце
HEART_COLOR = "red"
HEART_START_X = -250
HEART_START_Y = 0
HEART_ANGLE = 140
HEART_FORWARD = 68
HEART_CIRCLE_RADIUS = -35
HEART_CIRCLE_ANGLE = 200
HEART_TURN_ANGLE = 60

# ТРАВА
GRASS_COLOR = "green"
GRASS_COUNT = 12
GRASS_START_X = -390
GRASS_START_Y = -325
GRASS_STEP_X = 25
GRASS_BASE_ANGLE = 75
GRASS_ANGLE_VARIATION = 10
GRASS_WIDTH_MAX = 3
GRASS_LENGTH_BASE = 70
GRASS_STEP_LENGTH = 10
GRASS_TURN_ANGLE = 5
GRASS_STEP_VARIATION = 30

# =====================================================
# НАСТРОЙКИ ЭКРАНА
# =====================================================

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=800, height=700)


# =====================================================
# ФУНКЦИИ
# =====================================================
# Солнце
def draw_sun():
    t.color(SUN_LINES_COLOR)
    t.width(SUN_LINES_WIDTH)
    for i in range(COUNT_OF_SUN_LINES):
        t.penup()
        t.goto(SUN_LINE_X, SUN_LINE_Y)
        t.pendown()
        t.setheading(i * BETWEEN_SUN_LINES)
        t.forward(LINES_LENGTH)
    t.penup()
    t.goto(SUN_CENTER_X, SUN_CENTER_Y)
    t.pendown()
    t.color(SUN_COLOR)
    t.begin_fill()
    t.circle(SUN_RADIUS)
    t.end_fill()

# Облако
def draw_cloud(X_OFFSET, Y_OFFSET):
    t.color(CLOUD_COLOR)
    for CLOUD_X, CLOUD_Y, RADIUS in CORDS:
        t.penup()
        t.goto(CLOUD_X + X_OFFSET, CLOUD_Y + Y_OFFSET - RADIUS)
        t.pendown()
        t.begin_fill()
        t.circle(RADIUS)
        t.end_fill()

# Цветок
def draw_flower(FLOWER_OFFSET_X, FLOWER_OFFSET_Y, PETAL_COLOR):
    t.color(STEM_COLOR)
    t.width(STEM_WIDTH)
    t.penup()
    t.goto(STEM_START_X + FLOWER_OFFSET_X, STEM_START_Y + FLOWER_OFFSET_Y)
    t.pendown()
    t.setheading(FLOWER_DIRECTION)
    t.forward(STEM_LENGTH)

    t.color(PETAL_COLOR)
    for i in range(8):
        t.penup()
        t.goto(PETAL_CENTER_X + FLOWER_OFFSET_X, PETAL_CENTER_Y + FLOWER_OFFSET_Y)
        t.pendown()
        t.setheading(i * PETAL_ANGLE)
        t.begin_fill()
        t.circle(PETAL_RADIUS, PETAL_EXTENT)
        t.circle(PETAL_RADIUS, PETAL_EXTENT)
        t.end_fill()

    t.penup()
    t.goto(CORE_CENTER_X + FLOWER_OFFSET_X, CORE_CENTER_Y + FLOWER_OFFSET_Y)
    t.pendown()
    t.color(CORE_COLOR)
    t.begin_fill()
    t.circle(CORE_RADUIS)
    t.end_fill()

# Сердце
def draw_heart(HEART_OFFSET_X, HEART_OFFSET_Y):
    t.penup()
    t.goto(HEART_START_X + HEART_OFFSET_X, HEART_START_Y + HEART_OFFSET_Y)
    t.pendown()
    t.color(HEART_COLOR)
    t.begin_fill()
    t.setheading(HEART_ANGLE)
    t.forward(HEART_FORWARD)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.setheading(HEART_TURN_ANGLE)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.forward(HEART_FORWARD)
    t.end_fill()

# Текст
def draw_text():
    t.penup()
    t.goto(MARCH_TEXT_CENTER_X, MARCH_TEXT_CENTER_Y)
    t.pendown()
    t.color(MARCH_TEXT_COLOR)
    t.write("С 8 Марта!", align="center", font=("Arial", MARCH_TEXT_THICKNESS, "bold"))

    t.penup()
    t.goto(WOMAN_TEXT_CENTER_X, WOMAN_TEXT_CENTER_Y)
    t.pendown()
    t.color(WOMAN_TEXT_COLOR)
    t.write("Дорогие женщины!", align="center", font=("Arial", WOMAN_TEXT_THICKNESS, "italic"))

    t.penup()
    t.goto(DAY_TEXT_CENTER_X, DAY_TEXT_CENTER_Y)
    t.pendown()
    t.color(DAY_TEXT_COLOR)
    t.write("Пусть каждый день будет ярким!", align="center", font=("Arial", DAY_TEXT_THICKNESS, "normal"))

# Трава
def draw_grass(X_GRASS_OFFSET, Y_GRASS_OFFSET):
    t.color(GRASS_COLOR)
    for i in range(GRASS_COUNT):
        t.penup()
        t.goto(GRASS_START_X + X_GRASS_OFFSET + i * GRASS_STEP_X, GRASS_START_Y + Y_GRASS_OFFSET)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(GRASS_BASE_ANGLE + (i % 5) * GRASS_ANGLE_VARIATION)
        t.width(GRASS_WIDTH_MAX - (i % 2))
        n = GRASS_LENGTH_BASE + (i % GRASS_STEP_VARIATION)
        for j in range(int(n / GRASS_STEP_LENGTH)):
            t.forward(GRASS_STEP_LENGTH)
            t.left(GRASS_TURN_ANGLE * d)


# =====================================================
# ОТРИСОВКА
# =====================================================

draw_sun()
draw_cloud(15, -50)
draw_cloud(-175, -30)
draw_cloud(-380, -10)
draw_flower(0, -20, "pink")
draw_flower(-270, -20, "blue")
draw_flower(270, -20, "red")
draw_heart(0, 0)
draw_heart(500, 0)
draw_text()
draw_grass(-70, -13)
draw_grass(10, -13)
draw_grass(173, -13)
draw_grass(317, -13)
draw_grass(456, -13)
draw_grass(500, -13)
turtle.done()