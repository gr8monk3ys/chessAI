"""
This is the main game and where the board is drawn as well as the functionality for the game working
"""

import pygame as p
import ChessEngine
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"

WIDTH = HEIGHT = 512
DIMENSION = 8
SQUARE_SIZE = HEIGHT // DIMENSION
MAX_FPS = 30
IMAGES = {}

''' 
Initializes a global dictionary of images, will be called once in main
'''
def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("Images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))

'''
Main driver for the code and updating the graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)    
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Renders the game state with the pieces and the board
'''
def drawGameState(screen, gs):
    drawBoard(screen)
    drawPieces(screen, gs.board)

'''
Draw the board depending on the game state
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            p.draw.rect(screen, color, p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

'''
Draw the pieces on top of the board
'''
def drawPieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board [row][col]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



if __name__ == "__main__":
    main()