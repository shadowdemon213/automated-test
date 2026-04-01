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
# Координаты частей облака (без смещения)
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
STEM_START_Y = -300
FLOOR_DIRECTION = 90
STEM_LENGTH = 120
PETAL_COLOR = "pink"
PETAL_COUNT = 8
PETAL_ANGLE_STEP = 45
PETAL_RADIUS = 30
PETAL_ARC_ANGLE = 180
CENTER_COLOR = "yellow"
CENTER_RADIUS = 20
CENTER_X = 0
CENTER_Y = -185

# ДЕКОР (СЕРДЕЧКО + ТЕКСТ)
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

HEART_COLOR = "red"
HEART_START_X = -300
HEART_START_Y = 50
HEART_ANGLE = 140
HEART_FORWARD = 62
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
GRASS_ROWS = 6
GRASS_ROW_OFFSET_Y = -25

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
def draw_flower(x_offset, y_offset):
    # Смещение цветка
    stem_x = STEM_START_X + x_offset
    stem_y = STEM_START_Y + y_offset
    center_x = CENTER_X + x_offset
    center_y = CENTER_Y + y_offset

    t.color(STEM_COLOR)
    t.width(STEM_WIDTH)
    t.penup()
    t.goto(stem_x, stem_y)
    t.pendown()
    t.setheading(FLOOR_DIRECTION)
    t.forward(STEM_LENGTH)

    t.width(1)
    t.color(PETAL_COLOR)
    for i in range(PETAL_COUNT):
        t.penup()
        t.goto(center_x, center_y)
        t.pendown()
        t.setheading(i * PETAL_ANGLE_STEP)
        t.begin_fill()
        t.circle(PETAL_RADIUS, PETAL_ARC_ANGLE)
        t.circle(PETAL_RADIUS, PETAL_ARC_ANGLE)
        t.end_fill()

    t.penup()
    t.goto(center_x, center_y - 15)  # небольшое смещение для центра
    t.setheading(0)
    t.pendown()
    t.color(CENTER_COLOR)
    t.begin_fill()
    t.circle(CENTER_RADIUS)
    t.end_fill()

# Сердечко
def draw_heart(x_offset, y_offset, color=HEART_COLOR):
    t.penup()
    t.goto(HEART_START_X + x_offset, HEART_START_Y + y_offset)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(HEART_ANGLE)
    t.forward(HEART_FORWARD)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.setheading(HEART_TURN_ANGLE)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.forward(HEART_FORWARD)
    t.end_fill()

# Декор (текст)
def draw_decor():
    # Текст
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

# Сердечко с возможностью смещения
def draw_heart(x_offset, y_offset, color=HEART_COLOR):
    t.penup()
    t.goto(HEART_START_X + x_offset, HEART_START_Y + y_offset)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.setheading(HEART_ANGLE)
    t.forward(HEART_FORWARD)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.setheading(HEART_TURN_ANGLE)
    t.circle(HEART_CIRCLE_RADIUS, HEART_CIRCLE_ANGLE)
    t.forward(HEART_FORWARD)
    t.end_fill()

# Трава
def draw_grass():
    for row in range(GRASS_ROWS):
        start_y = GRASS_START_Y + row * GRASS_ROW_OFFSET_Y
        t.color(GRASS_COLOR)
        for i in range(GRASS_COUNT):
            t.penup()
            t.goto(GRASS_START_X + i * GRASS_STEP_X, start_y)
            t.pendown()
            d = 1 if i % 2 == 0 else -1
            t.setheading(GRASS_BASE_ANGLE + (i % 5) * GRASS_ANGLE_VARIATION)
            t.width(GRASS_WIDTH_MAX - (i % 2))
            n = GRASS_LENGTH_BASE + (i % GRASS_STEP_VARIATION)
            for j in range(int(n / GRASS_STEP_LENGTH)):
                t.forward(GRASS_STEP_LENGTH)
                t.left(GRASS_TURN_ANGLE * d)
            t.width(1)


draw_sun()
draw_cloud(0, 0)  # Первое облако
draw_cloud(-220, 30)  # Второе облако
draw_cloud(-380, -10)  # Третье облако

draw_flower(0, 0)
draw_flower(-150, -50)
draw_flower(150, -70)

draw_heart(0, 0)
draw_heart(550, 0)

draw_decor()
draw_grass()

turtle.done()