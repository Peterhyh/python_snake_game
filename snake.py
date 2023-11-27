from turtle import Turtle


class Snake:
    def __init__(self, length):
        self.length = length
        self.segments = []
        self.starting_pos = [(0, 0), (-20, 0), (-40, 0)]

    def move(self):
        for position in self.starting_pos:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

        for segment_idx in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment_idx - 1].xcor()
            y_cor = self.segments[segment_idx - 1].ycor()
            self.segments[segment_idx].goto(x_cor, y_cor)
            self.segments[0].forward(40)
            self.segments[0].left(90)
