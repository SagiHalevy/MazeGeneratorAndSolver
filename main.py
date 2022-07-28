import random
import turtle
from turtle import Screen
from tkinter import *
mazeSize = 7 # size of the maze X by X
sectionSize = 20 # size of each wall's tile

stack = [] # stack for creating the maze
amountVisited = 0 # tracking how many tiles visited
maze = [[[1,1,1,1] for i in range(mazeSize)] for i in range(mazeSize)] #[1,1,1,1] => [top,right,down,left]
r = mazeSize-1 # start row
c = 0 # start col

solveStack = [] # stack for solving the maze
visited = [] #track visited tiles of solver
chosenHeur = ''

player = turtle.Turtle() # drawer

#inseting to the stack all the next possible moves from the current tile
def RandomInsertPossibleMoves(currentTile):
    #get current tile row and col
    r = currentTile[0]
    c = currentTile[1]
    #check possible moves from current tile
    moves = []
    if c+1 < mazeSize and maze[r][c+1]==[1,1,1,1]: # can move right (not overflow and not visited yet)
       moves += [[r,c+1,'right']]
    if c-1 >= 0 and maze[r][c-1] == [1, 1, 1, 1]:  # can move left (not overflow and not visited yet)
        moves +=[[r,c - 1,'left']]
    if r-1 >= 0 and maze[r-1][c] == [1, 1, 1, 1]:  # can move up (not overflow and not visited yet)
        moves +=[[r-1,c,'up']]
    if r + 1 < mazeSize and maze[r + 1][c] == [1, 1, 1, 1]:  # can move down (not overflow and not visited yet)
        moves +=[[r+1,c,'down']]

    #insert in random order
    movesLen = len(moves)
    for i in range(movesLen):
        j = random.randint(0,len(moves)-1)
        stack.append(moves[j])
        del moves[j]

#removing the wall after going to next tile
def RemoveWall(currentTile):
    #get current tile row and col
    if not currentTile: return
    direction = currentTile[2]
    r = currentTile[0]
    c = currentTile[1]
    if maze[r][c] != [1,1,1,1]: return False # if the tile was visited previously - don't do anything
    match direction:
        case 'up':
            maze[r][c][2] = 0
            maze[r + 1][c][0] = 0
        case 'right':
            maze[r][c][3] = 0
            maze[r][c - 1][1] = 0
        case 'down':
            maze[r][c][0] = 0
            maze[r - 1][c][2] = 0
        case 'left':
            maze[r][c][1] = 0
            maze[r][c + 1][3] = 0
    global amountVisited
    amountVisited+=1
    return True

#will draw the maze line by line
def drawMaze(startXPos,startYPos,speed):
    player.speed(speed)
    startX = startXPos
    startY = startYPos
    xPos = startX # this var used while updating the x position
    yPos = startY # this var used while updating the y position

    player.penup()
    player.setpos(startX, startY)
    player.pendown()

    for i in [0, 2, 3]:  # [top,bottom,left]
        if i == 2:  # drawing the bottom walls
            player.forward(sectionSize * mazeSize)
            continue
        if i == 3:#initialzing before drawing left walls
            maze[mazeSize-1][0][3] = 0 #open the maze's entrance
            yPos = startY
            player.penup()
            player.setpos(startX, startY)
            player.pendown()
            player.right(90)

        for row in maze:
            for tile in row:
                if i == 0:#drawing top walls
                    if tile[i] == 1:
                        player.forward(sectionSize)
                    else:# skip to next position
                        player.penup()
                        player.forward(sectionSize)
                        player.pendown()
                elif i == 3:#drawing left walls
                    if tile[i] == 1:
                        player.forward(sectionSize)
                        player.penup()
                        xPos += sectionSize
                        player.setpos(xPos, yPos)
                        player.pendown()
                    else:# skip to next position
                        player.penup()
                        player.forward(sectionSize)
                        xPos += sectionSize
                        player.setpos(xPos, yPos)
                        player.pendown()
            if i == 0:# go to next line
                player.penup()
                yPos -= sectionSize
                player.setpos(startX, yPos)
                player.pendown()
            elif i == 3:# go to next line
                if yPos != startY: # don't draw on the exit(goal) wall
                    player.forward(sectionSize)  # drawing the right wall
                player.penup()
                yPos -= sectionSize
                xPos = startX
                player.setpos(startX, yPos)
                player.pendown()
    #set to maze starting position
    player.penup()
    player.left(90)
    player.setpos(startX-sectionSize/2, startY - (mazeSize-1)*sectionSize - sectionSize/2)
    player.pendown()

#create the maze
def createMaze():
    firstTile = [r, c]
    RandomInsertPossibleMoves(firstTile)
    global amountVisited
    amountVisited += 1

    while amountVisited < mazeSize * mazeSize:
        if stack:  # gets the row and col of the current tile
            nextTile = stack.pop()
            if RemoveWall(nextTile):
                RandomInsertPossibleMoves(nextTile)

#heuristic value for a specific tile using manhattan distance
def heuristic(tile, heur):
    match heur:
        case "Manhatten":
            #target location
            targetRow = 0
            targetCol = mazeSize-1
            #current tile location
            r = tile[0]
            c = tile[1]
            newR = abs(r-targetRow)
            newC = abs(c-targetCol)
            return newR+newC
        case "Backtracking":
            return
#solve the maze and draw it
def solve():
    solveButton["state"] = DISABLED
    global chosenHeur
    chosenHeur = heuristicChosen.get()
    player.speed(2)
    player.color('green')
    solveStack.append([r, c, heuristic([r, c],chosenHeur)]) # inserting the starting tile
    #initialization of row and col to the starting tile
    row = r
    col = c-1
    while True:
        nextTile = solveStack.pop()
        # if a big step should be taken, don't draw over. (until draw steps that goes one tile)
        if not(abs(nextTile[1]-col) + abs(nextTile[0]-row) <=1):
            player.penup()
        #move accordingly to last change in coordiantes
        player.setpos(player.xcor() + (nextTile[1] - col) * sectionSize,
                      player.ycor() + -(nextTile[0] - row) * sectionSize)
        #update row and col to current tile
        row = nextTile[0]
        col = nextTile[1]
        player.pendown() # for a case where penup() were used

        #if goal tile reached
        if nextTile[0] == 0 and nextTile[1] == mazeSize-1:
            # we don't want the player to stop at the end tile - but to actually get out of the maze
            player.setpos(player.xcor() + sectionSize, player.ycor())
            break # goal found

        InsertPossibleMoves(nextTile)

        if chosenHeur == 'Manhatten':  # sort the stack so the closest tile will be at top (lowest heuristic value) (x[2]) is the heuristic value
            solveStack.sort(key = lambda x : x[2] ,reverse=True)



#add to solving stack all the possible moves
def InsertPossibleMoves(nextTile):
    r = nextTile[0]
    c = nextTile[1]
    #visited is used so we don't go back to visited tiles
    global visited
    visited += [[r,c]]
    #get current tile and investigate where it can go - up/right/down/left
    currentTile = maze[r][c]
    for i, direction in enumerate(currentTile):
        if i ==0 and direction ==0 and [r-1,c] not in visited:# upward
            solveStack.append([r-1,c,heuristic([r-1,c],chosenHeur)])
        elif i ==1 and direction ==0 and [r,c+1] not in visited: #right
            solveStack.append([r,c+1,heuristic([r,c+1],chosenHeur)])
        elif i ==2 and direction ==0 and [r+1,c] not in visited: #down
            solveStack.append([r+1,c,heuristic([r+1,c],chosenHeur)])
        elif i ==3 and direction ==0 and [r,c-1] not in visited : #left
            if c-1 != -1: # this is prevent from inserting negative columns to the stack (since player starts at negative column [outside the maze])
                 solveStack.append([r,c-1,heuristic([r,c-1],chosenHeur)])

createMaze()

for i in maze:
    print (i)



canvas = Screen().getcanvas()
solveButton = Button(canvas.master, text="Solve", command=solve)
solveButton["state"] = DISABLED
solveButton.pack()
solveButton.place(x=300, y=50)  # place the button anywhere on the screen

heuristicChosen = StringVar(canvas.master)
heuristicChosen.set("Manhatten") # default value
heurisitcsList = OptionMenu(canvas.master, heuristicChosen, "Manhatten", "Backtracking")
heurisitcsList.pack()
heurisitcsList.place(x=400,y=50)
drawMaze(-400,300,10)
solveButton["state"] = NORMAL
turtle.done()