from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()  # 3 segment snake created.
        self.head = self.segments[0]  # head of the snake.

        # Create Snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):  # position --> position to add the segment to.
        new_segment = Turtle("square")
        if len(self.segments) == 0:
            new_segment.color("red")  # head of the snake
        else:
            new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(
            self.segments[-1].position())  # new segment is added at the position of the last segment in self.segments

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # last item ---> 0 not included
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
            # if first segment is not moved, then all segments will go to the position of the first segment.
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT and self.head.heading() != LEFT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT and self.head.heading() != RIGHT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN and self.head.heading() != UP:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP and self.head.heading() != DOWN:
            self.head.setheading(DOWN)
