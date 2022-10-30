import pygame

class Button:
    """Create a button, then blit the surface in the while loop"""
 
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.original = text
        self.font = pygame.font.SysFont("Rockwell Condensed", font)
        self.on = False
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        originalText = self.font.render(text, 1, pygame.Color("White"))
        self.originalSize = originalText.get_size()
        self.change_text(text, bg)
        
 
    def change_text(self, text, bg="White"):
        """Change the text whe you click"""
        
        self.text = self.font.render(text, 1, pygame.Color("White"))
        # self.size = self.text.get_size()
        self.size = self.originalSize
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self, screen):
        screen.blit(self.surface, (self.x, self.y))
        pygame.display.flip()
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    if self.on:
                        self.change_text(self.original, bg="blue")
                    else:
                        self.change_text(self.feedback, bg="red")
                    self.on = not self.on
                    return True
        return False
        