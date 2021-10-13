import turtle
import time


# App Variable
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# window
screen = turtle.Screen()
screen.title('Animation')
screen.bgcolor('lightgreen')
screen.setup(width=SCREEN_WIDTH,height=SCREEN_HEIGHT)
screen.tracer(0)



# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.penup()
ball.speed(0)
ball.goto(200,200)
ball.dx = 5
ball.dy = 5


# brick
brick = turtle.Turtle()
brick.shape('square')
BRICK_SCALE_FACTOR_LENGTH = 5
BRICK_SCALE_FACTOR_WIDTH = 1.5
brick.shapesize(stretch_len=BRICK_SCALE_FACTOR_LENGTH,stretch_wid=BRICK_SCALE_FACTOR_WIDTH)


def top_bottom_collisions():
	top_bottom_collisons = [
		ball.ycor() > SCREEN_HEIGHT//2 - 10,
		ball.ycor() < -SCREEN_HEIGHT//2 + 10,
	]

	if any(top_bottom_collisons):
		return True

	return False


def right_left_collison():
	right_left_collisons = [
		ball.xcor() > SCREEN_WIDTH//2 - 10,
		ball.xcor() < -SCREEN_WIDTH//2 + 10,
	]

	if any(right_left_collisons):
		return True

	return False



while True:

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)



	if top_bottom_collisions():
		ball.dy *= -1

	if  right_left_collison():
		ball.dx *= -1


	x_hit = ball.xcor() < brick.xcor() + (BRICK_SCALE_FACTOR_LENGTH * 10) + 10 and ball.xcor() > brick.xcor() - ((BRICK_SCALE_FACTOR_LENGTH * 10) + 10)
	y_hit = ball.ycor() < brick.ycor() + (BRICK_SCALE_FACTOR_WIDTH * 10) + 10 and ball.ycor() > brick.ycor() - ((BRICK_SCALE_FACTOR_WIDTH * 10) + 10)


	if x_hit and y_hit:
		if ball.xcor() > brick.xcor() + (BRICK_SCALE_FACTOR_LENGTH * 10) or ball.xcor() < brick.xcor() - (BRICK_SCALE_FACTOR_LENGTH * 10):
			ball.dx *= -1

		elif ball.ycor() > brick.xcor() + (BRICK_SCALE_FACTOR_WIDTH * 10) or ball.ycor() < brick.ycor() - (BRICK_SCALE_FACTOR_WIDTH * 10):
			ball.dy *= -1 



	screen.update()
	time.sleep(1/240)
