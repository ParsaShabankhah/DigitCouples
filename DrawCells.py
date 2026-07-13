import pygame

def draw(cells, screen, font, health, main_is_found):
    screen.fill((89, 236, 255) if main_is_found else (160, 160, 160))
    screen.blit(health, (20, 20))
    for pair in cells:
        pygame.draw.rect(screen, (0, 0, 0), cells[pair]["rect"])
        color = (0, 255, 0) if not cells[pair]["hide"] else (0, 0, 0)
        text = font.render(str(cells[pair]["val"]), True, color)
        screen.blit(text, text.get_rect(center=cells[pair]["rect"].center))
    programmer_text = font.render("Made by Parsa Shabankhah", True, (50, 50, 50))
    rect = programmer_text.get_rect(center=(400, 560))
    screen.blit(programmer_text, rect)