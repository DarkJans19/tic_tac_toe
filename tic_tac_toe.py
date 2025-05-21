import pygame
from pathlib import Path

def graph_coord(coord_matrix, table):
    screen.blit(wallpaper, (0,0))
    for row in range(len(coord_matrix)):
        for col in range(len(coord_matrix)):
            if table[row][col] == "X":
                graph_x(row, col, coord_matrix)
            elif table[row][col] == "O":
                graph_o(row, col, coord_matrix)


def graph_x(row, col, coord_matrix):
    screen.blit(ex, coord_matrix[row][col])


def graph_o(row, col, coord_matrix):
    screen.blit(circle, coord_matrix[row][col])


def check_winner(turn, matrix):
    for i in range(len(matrix)):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == turn:
            return True
        if matrix[0][i] == matrix[1][i] == matrix[2][i] == turn:
            return True
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == turn:
        return True
    if matrix[0][2] == matrix [1][1] == matrix[2][0] == turn:
        return True
    return False

def reset_game(matrix):
    turn = "X"
    turn_count = 0
    game_over = False
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            matrix[row][col] = ""
    return matrix, turn, turn_count, game_over

# Initialize pygame and set a size of the screen
pygame.init()

width, height = 768, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Set the images we'll use using path for other systems too
wallpaper = pygame.image.load(str(Path('.') / 'static' / 'tictactoe_background.png'))
ex = pygame.image.load(str(Path('.') / 'static' / 'hatsune_pear.png'))
circle = pygame.image.load(str(Path('.') / 'static' / 'teto_pear.png'))

# Size of the icons
cell_size = width // 3
icon_margin = 40
image_size = cell_size - icon_margin

# Scale the pictures
wallpaper = pygame.transform.scale(wallpaper, (width, height))
ex = pygame.transform.scale(ex, (image_size, image_size))
circle = pygame.transform.scale(circle, (image_size, image_size))

# Calculate the coords
coord = []
for row in range(3):
    row_cords = []
    for col in range(3):
        x = col * cell_size + (cell_size - image_size) // 2
        y = row * cell_size + (cell_size - image_size) // 2
        row_cords.append((x, y))
    coord.append(row_cords)

table = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

font = pygame.font.Font(None, 60)

# Make reset button
width_reset_button = 200
height_reset_button = 50

position_button_x = (width - width_reset_button)//2
position_button_y = height - height_reset_button - 10
rect_button = pygame.Rect(position_button_x, position_button_y, width_reset_button, height_reset_button)
# Crear una Surface con canal alfa (RGBA)
button_surface = pygame.Surface((width_reset_button, height_reset_button), pygame.SRCALPHA)
button_surface.fill((255, 255, 255, 30))  # 120 es el nivel de transparencia (0=transparente, 255=opaco)
button_text_surface = font.render("Reset", True, (0, 0, 0))
button_text_rect = button_text_surface.get_rect(center=(width_reset_button // 2, height_reset_button // 2))

# Variables
turn = 'X'
game_over = False
game_ended = False
running = True
turn_count = 0
message = ""

clock = pygame.time.Clock()
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if position_button_x <= mouseX <= position_button_x + width_reset_button and position_button_y <= mouseY <= position_button_y + height_reset_button:
                table, turn, turn_count, game_over = reset_game(table)
                game_ended = False
                continue
            if not game_over and 0 <= mouseX < width and 0 <= mouseY < height:
                col = mouseX // cell_size
                row = mouseY // cell_size
                if table[row][col] == "":
                    table[row][col] = turn
                    turn_count += 1
                    if check_winner(turn, table):
                        message = f"{"Miku" if turn == 'X' else 'Teto'} wins!"
                        game_over = True
                        game_ended = True
                    elif turn_count == 9:
                        message = "Draw!"
                        game_over = True
                        game_ended = True
                    else:
                        turn = 'O' if turn == 'X' else 'X'
    graph_coord(coord, table)
    screen.blit(button_surface, rect_button.topleft)
    screen.blit(button_text_surface, rect_button.move(button_text_rect.topleft))
    if game_over:
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)
    pygame.display.update()
    if game_ended:
        pygame.time.delay(2000)
        game_ended = False


pygame.quit()
