import pygame


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


# Initialize pygame and set a size of the screen
pygame.init()

width, height = 768, 768
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")

# Set the images we'll use
wallpaper = pygame.image.load(r'static\tictactoe_background.png')
ex = pygame.image.load(r'static\hatsune_pear.png')
circle = pygame.image.load(r'static\teto_pear.png')

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

turn = 'X'
message = "Uy"
game_over = False
turn_count = 0
clock = pygame.time.Clock()
font = pygame.font.Font(None, 60)
while not game_over:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if 0 <= mouseX < width and 0 <= mouseY < height:
                col = mouseX // cell_size
                row = mouseY // cell_size
                if table[row][col] == "":
                    table[row][col] = turn
                    turn_count += 1
                    if check_winner(turn, table):
                        message = f"{"Miku" if turn == 'X' else 'Teto'} wins!"
                        game_over = True
                    elif turn_count == 9:
                        message = "Draw!"
                        game_over = True
                    else:
                        turn = 'O' if turn == 'X' else 'X'
    graph_coord(coord, table)
    
    if game_over:
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width // 2, height // 2))
        screen.blit(text_surface, text_rect)

    pygame.display.update()
pygame.time.delay(1000)
pygame.quit()