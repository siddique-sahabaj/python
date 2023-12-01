from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self, segment_shape):
        self.segments = []
        self.segment_shape = segment_shape
        self.speed = 0.1
        self.create_snake(STARTING_POSITION)
        self.head = self.segments[0]

    def create_snake(self, starting_position):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        snake_segment = Turtle(self.segment_shape)
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)  # Adding the snake_segment to the snake_segments list

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].position())
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def game_reset(self):
        # Making the previous snake disappear
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake(STARTING_POSITION)
        self.head = self.segments[0]