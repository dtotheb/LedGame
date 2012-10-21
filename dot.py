import pygame


class Dot():
    def __init__(self, pos=(0, 0), radius=25, lit=False):
        self.pos = pos
        self.lit = lit
        self.radius = radius
        self.screen = pygame.display.get_surface()
        self.color = (0, 250, 0)

    def draw(self):
        pos_x = int(self.pos[0] * (self.radius * 2)) + (self.radius)
        pos_y = int(self.pos[1] * (self.radius * 2)) + (self.radius)

        if self.lit:
            thickness = 0
        else:
            thickness = 1

        pygame.draw.circle(self.screen,
                         self.color,
                        (pos_x, pos_y),
                        self.radius,
                        thickness)
