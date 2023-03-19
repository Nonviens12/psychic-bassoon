import game
import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))

difficultySelector = None

def set_difficulty(value, difficulty):
    print(value, difficulty)
    
    
    
def show_scoreboard():
    global menu
    menu.clear()
    with open('scoreboard.txt', 'r') as file:
        text = file.read()
        menu.add.label(text, max_char=-1, font_size=20)


def start_the_game():
    Value = print(difficultySelector.get_value())
    myGame = game.game(Value = Value)
    myGame.play()


menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
difficultySelector = menu.add.selector('Difficulty :', [('Easy', 1), ('Normal', 2), ('Hard', 3), ('Expert', 4), ('Expert+', 5)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Scoreboard', show_scoreboard)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
 
    if menu.is_enabled():
        menu.update(events)
        menu.draw(surface)

    pygame.display.update()