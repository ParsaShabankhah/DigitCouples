import pygame
from DrawCells import draw
from GameLogic import GameLogic
from Sound import Sound

pygame.init()
#pygame.mixer.init()
sound = Sound()
pygame.display.set_caption("Digit Couples")
screen = pygame.display.set_mode((800, 600))
screen.fill((160, 160, 160))
pygame.display.update()

modes = {
    "Easy_Peasy": 6,
    "Oh_Ok": 10,
    "Oh_Lord!": 14
}

button_color = (157, 115, 65)
hover_color = (230, 115, 65)
font = pygame.font.Font('CascadiaCode-VariableFont_wght.ttf', 24)


def start_game(mode: int):

    run = True
    game = GameLogic(mode)
    cells = {}
    temp = []
    main_is_found = False

    grid_size = mode // 2
    cell_size = 400 // (grid_size)
    gap = 10

    total_size = (cell_size * grid_size) + ((grid_size - 1) * gap)
    x_start = (800 - total_size) // 2
    y_start = (600 - total_size) // 2

    # building blocks
    for row in game.blocks:
        val = game.blocks[row]

        if isinstance(val[0], tuple):
            for pair in val:
                x = x_start + pair[1] * (cell_size + gap)
                y = y_start + pair[0] * (cell_size + gap)

                cells[pair] = {
                    "rect": pygame.Rect(x, y, cell_size, cell_size),
                    "val": row,
                    "hide": True,
                }
        else:
            x = x_start + val[1] * (cell_size + gap)
            y = y_start + val[0] * (cell_size + gap)

            cells[val] = {
                "rect": pygame.Rect(x, y, cell_size, cell_size),
                "val": row,
                "hide": True,
            }

    while run:
        # draw
        health = font.render(f"health = {game.health}", True, (0, 0, 0))
        draw(cells, screen, font, health, main_is_found)

        # logic
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                for pair, item in cells.items():
                    if item["rect"].collidepoint(mouse_pos):
                        sound.select_block()
                        if item["val"] in game.saving_points:
                            continue
                        if game.check_main(item["val"]):
                            sound.main_item()
                            game.health += game.mode//2 
                            main_is_found = True
                            item["hide"] = False
                            pygame.display.update()
                        else:
                            temp.extend([item["val"], pair])
                            item["hide"] = False

                            if len(temp) < 4:
                                pass

                            else:
                                draw(cells, screen, font, health, main_is_found)
                                pygame.display.update()
                                pygame.time.wait(250)
                                res = game.check_match(*temp)
                                temp_cells = (temp[1], temp[3])

                                if res:
                                    sound.correct()
                                    cells[temp_cells[0]]["hide"] = False
                                    cells[temp_cells[1]]["hide"] = False

                                    if game.check_victory():
                                        screen.fill((255, 238, 140))
                                        winning_text = font.render("Congratulations!", True, (0, 0, 0))
                                        screen.blit(winning_text, (290, 240)) 
                                        sound.victory()
                                        pygame.display.update()
                                        pygame.time.wait(1500)
                                        return "menu"

                                        
                                else:
                                    cells[temp_cells[0]]["hide"] = True
                                    cells[temp_cells[1]]["hide"] = True
                                    sound.wrong()
                                    if not game.check_health():
                                        screen.fill((161, 41, 25))
                                        losing_text = font.render("Game Over!", True, (255, 255, 255))
                                        screen.blit(losing_text, (320, 240))
                                        sound.game_over()
                                        pygame.display.update()
                                        pygame.time.wait(1500)
                                        return "menu"

                                temp = []

        pygame.display.update()

    pygame.quit()


def start_menu():
    
    run = True
    game_name = font.render("Welcome to the Digit Couples!", True, (0, 0, 0))

    while run:
        screen.fill((160, 160, 160))
        screen.blit(game_name, (200, 130))
        mouse = pygame.mouse.get_pos()

        easy_rect = pygame.Rect(300, 220, 200, 60)
        ok_rect = pygame.Rect(300, 300, 200, 60)
        lord_rect = pygame.Rect(300, 380, 200, 60)

        pygame.draw.rect(screen, hover_color if easy_rect.collidepoint(mouse) else button_color, easy_rect)
        pygame.draw.rect(screen, hover_color if ok_rect.collidepoint(mouse) else button_color, ok_rect)
        pygame.draw.rect(screen, hover_color if lord_rect.collidepoint(mouse) else button_color, lord_rect)

        easy_text = font.render("Easy Peasy", True, (0, 0, 0))
        ok_text = font.render("Oh Ok", True, (0, 0, 0))
        lord_text = font.render("Oh Lord", True, (0, 0, 0))
        programmer_text = font.render("Made by Parsa Shabankhah", True, (50, 50, 50))
        rect = programmer_text.get_rect(center=(400, 560))

        screen.blit(easy_text, easy_text.get_rect(center=easy_rect.center))
        screen.blit(ok_text, ok_text.get_rect(center=ok_rect.center))
        screen.blit(lord_text, lord_text.get_rect(center=lord_rect.center))
        screen.blit(programmer_text, rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(mouse):
                    sound.click_menu()
                    return ("game",modes["Easy_Peasy"])

                if ok_rect.collidepoint(mouse):
                    sound.click_menu()
                    return ("game", modes["Oh_Ok"])

                if lord_rect.collidepoint(mouse):
                    sound.click_menu()
                    return ("game", modes["Oh_Lord!"])

        pygame.display.update()

    pygame.quit()