import pygame


class Button():
    def __init__(self, text, pos, size=(100, 30), color=(0, 0, 200), hilight=(0, 200, 200)):
        """
        Creates a button
        """
        self.normal = color
        self.hilight = hilight
        self.rect = pygame.Rect(pos, size)
        self.mouseover = False
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.text_image = self.font.render(text, 1, (255, 255, 255))
        w, h = self.font.size(text)  # size of font image
        self.text_pos = (pos[0] + size[0] / 2 - w / 2, pos[1] + size[1] / 2 - h / 2)  # center text
        self.buttondown = False

    def draw(self, surface):
        """
        draws the button
        """
        rectout = self.rect.inflate(2, 2)
        rectin = self.rect.inflate(1, 1)
        if self.buttondown:
            pygame.draw.rect(surface, (0, 0, 0), rectout)
            pygame.draw.rect(surface, (255, 255, 255), rectin)
        else:
            pygame.draw.rect(surface, (255, 255, 255), rectout)
            pygame.draw.rect(surface, (0, 0, 0), rectin)
        if self.mouseover:
            pygame.draw.rect(surface, self.hilight, self.rect)
        else:
            pygame.draw.rect(surface, self.normal, self.rect)
        surface.blit(self.text_image, self.text_pos)
