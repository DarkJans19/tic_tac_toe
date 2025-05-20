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
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("Tic Tac Toe")

# Set the images we'll use
wallpaper = pygame.image.load(r'static\tictactoe_background.png')
ex = pygame.image.load(r'static\hatsune_pear.png')
circle = pygame.image.load(r'static\teto_pear.png')

# Scale the images
wallpaper = pygame.transform.scale(wallpaper, (450, 450))
ex = pygame.transform.scale(ex, (110, 110))
circle = pygame.transform.scale(circle, (110, 110))

coord_matrix = [[(40,50), (150,50), (260,50)],
        [(40,160), (150,160), (260,160)],
        [(40,270), (150,270), (260,270)]
        ]

table = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]

turn = 'X'
game_over = False
clock = pygame.time.Clock()
while not game_over:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX > 40 and mouseX < 360) and (mouseY > 50 and mouseY < 380):
                col = (mouseX - 40) // 110
                row = (mouseY - 50) // 110
                if table[row][col] == "":
                    table[row][col] = turn
                if check_winner(turn, table):
                    game_over = True
                turn = 'O' if turn == 'X' else 'X'
    graph_coord(coord_matrix, table)
    pygame.display.update()

pygame.quit()