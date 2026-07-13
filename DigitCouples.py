from GameMenus import start_menu, start_game

state = "menu"

while True:
    match state:
        case "menu":
            state = start_menu()
        case ("game", mode):
            state = start_game(mode)
        case None:
            break