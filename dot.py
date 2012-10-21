import pygame


class Dot():
    def __init__(self, pos=(0, 0), radius=25, lit=False):
        self.pos = pos
        self.lit = lit
        self.radius = radius
        self.screen = pygame.display.get_surface()
        self.color = (0, 250, 0)
        self.pos_x = int(self.pos[0] * (self.radius * 2)) + (self.radius)
        self.pos_y = int(self.pos[1] * (self.radius * 2)) + (self.radius)

    def draw(self):

        if self.lit:
            thickness = 0
        else:
            thickness = 1

        pygame.draw.circle(self.screen,
                         self.color,
                        (self.pos_x, self.pos_y),
                        self.radius,
                        thickness)

    def clicked(self, grid):

        if self.lit:
            self.lit = False
            grid.setPixel(self.pos[0], self.pos[1], 0)
        else:
            self.lit = True
            grid.setPixel(self.pos[0], self.pos[1])
