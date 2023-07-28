import random


GameArea : list = [["N","N","N"],["N","N","N"],["N","N","N"]]

def display(GameArea : list) -> None:
    for row in GameArea:
        print(row)

def generatePossibleMoves(GameArea : list, move : int) -> list:
    newArea = [row[:] for row in GameArea]
    solutions : list = []
    for rowI in range(0,3):
        for boxI in range(0,3):
            if newArea[rowI][boxI] != "X" and newArea[rowI][boxI] != "O":
                newAreaEdited = [row[:] for row in newArea]
                if move == 0:
                    newAreaEdited[rowI][boxI] = "O"
                else:
                    newAreaEdited[rowI][boxI] = "X"
                solution : list= [row[:] for row in newAreaEdited]
                solutions.append(solution)
    return solutions

def CheckTurn(GameArea: list) -> int:
    sumX = sum(row.count("X") for row in GameArea)
    sumO = sum(row.count("O") for row in GameArea)
    if sumX>sumO:
        return 0
    else:
        return 1
    

def Heurstic(GameArea : list, move : int) -> int:
    score1 = 0
    score2 = 0
    for player in {"X"}:
        for row in range(0,3):
            if GameArea[row][0] == GameArea[row][1] == GameArea[row][2] == player:
                score1 += 100
            elif GameArea[row][0] == GameArea[row][1] == player and GameArea[row][2] == "N":
                score1 +=10
            elif GameArea[row][0] == GameArea[row][2] == player and GameArea[row][1] == "N":
                score1 +=10   
            elif GameArea[row][2] == GameArea[row][1] == player and GameArea[row][0] == "N":
                score1 +=10
            if GameArea[row].count("O") >1:
                score1-=10

        for col in range(0,3):
            if GameArea[0][col] == GameArea[1][col] == GameArea[2][col] == player:
                score1 += 100
            elif GameArea[0][col] == GameArea[1][col] == player and GameArea[2][col] == "N":
                score1 +=10
            elif GameArea[0][col] == GameArea[2][col] == player and GameArea[1][col] == "N":
                score1 +=10   
            elif GameArea[2][col] == GameArea[1][col] == player and GameArea[0][col] == "N":
                score1 +=10

        if GameArea[0][0] == GameArea[1][1] == GameArea[2][2] == player:
            score1 += 100
        elif GameArea[0][0] == GameArea[1][1] == player and GameArea[2][2] == "N":
            score1 += 10
        elif GameArea[1][1] == GameArea[2][2] == player and GameArea[0][0] == "N":
            score1 += 10
        elif GameArea[0][0] == GameArea[2][2] == player and GameArea[1][1] == "N":
            score1 += 10

        if GameArea[0][2] == GameArea[1][1] == GameArea[2][0] == player:
            score1 += 100
        elif GameArea[0][2] == GameArea[1][1] == player and GameArea[2][0] == "N":
            score1 += 10
        elif GameArea[1][1] == GameArea[2][0] == player and GameArea[0][2] == "N":
            score1 += 10
        elif GameArea[0][2] == GameArea[2][0] == player and GameArea[1][1] == "N":
            score1 += 10
        
    for player in {"O"}:
        for row in range(0,3):
            if GameArea[row][0] == GameArea[row][1] == GameArea[row][2] == player:
                score2 -= 100
            elif GameArea[row][0] == GameArea[row][1] == player and GameArea[row][2] == "N":
                score2 -=10
            elif GameArea[row][0] == GameArea[row][2] == player and GameArea[row][1] == "N":
                score2 -=10   
            elif GameArea[row][2] == GameArea[row][1] == player and GameArea[row][0] == "N":
                score2 -=10
            if GameArea[row].count("X") > 1:
                score2 +=10

        for col in range(0,3):
            if GameArea[0][col] == GameArea[1][col] == GameArea[2][col] == player:
                score2 -= 100
            elif GameArea[0][col] == GameArea[1][col] == player and GameArea[2][col] == "N":
                score2 -=10
            elif GameArea[0][col] == GameArea[2][col] == player and GameArea[1][col] == "N":
                score2 -=10   
            elif GameArea[2][col] == GameArea[1][col] == player and GameArea[0][col] == "N":
                score2 -=10
            

        if GameArea[0][0] == GameArea[1][1] == GameArea[2][2] == player:
            score2 -= 100
        elif GameArea[0][0] == GameArea[1][1] == player and GameArea[2][2] == "N":
            score2 -= 10
        elif GameArea[1][1] == GameArea[2][2] == player and GameArea[0][0] == "N":
            score2 -= 10
        elif GameArea[0][0] == GameArea[2][2] == player and GameArea[1][1] == "N":
            score2 -= 10

        if GameArea[0][2] == GameArea[1][1] == GameArea[2][0] == player:
            score2 -= 100
        elif GameArea[0][2] == GameArea[1][1] == player and GameArea[2][0] == "N":
            score2 -= 10
        elif GameArea[1][1] == GameArea[2][0] == player and GameArea[0][2] == "N":
            score2 -= 10
        elif GameArea[0][2] == GameArea[2][0] == player and GameArea[1][1] == "N":
            score2 -= 10
        
    return score1 + score2
        
def CheckForWin(GameArea : list) -> bool:
    # Column wins
    if GameArea[0][0] == GameArea[0][1] and GameArea[0][2] == GameArea[0][1] and GameArea[0][0] != "N":
        return True
    if GameArea[1][0] == GameArea[1][1] and GameArea[1][2] == GameArea[1][1] and GameArea[1][1] != "N":
        return True
    if GameArea[2][0] == GameArea[2][1] and GameArea[2][2] == GameArea[2][1] and GameArea[2][2] != "N":
        return True
    
    # Row wins
    if GameArea[0][0] == GameArea[1][0] and GameArea[2][0] == GameArea[1][0] and GameArea[0][0] != "N":
        return True
    if GameArea[0][1] == GameArea[1][1] and GameArea[2][1] == GameArea[1][1] and GameArea[1][1] != "N":
        return True
    if GameArea[0][2] == GameArea[1][2] and GameArea[2][2] == GameArea[1][2] and GameArea[2][2] != "N":
        return True
    
    # Diagonal wins
    if GameArea[0][0] == GameArea[1][1] and GameArea[2][2] == GameArea[1][1] and GameArea[0][0] != "N":
        return True
    if GameArea[0][2] == GameArea[1][1] and GameArea[1][1] == GameArea[2][0] and GameArea[1][1] != "N":
        return True
    
    return False

def greedy(GameArea : list, move: int, level : int, maxLevel : int,parents: list) -> list:
    parents.append(GameArea)

    if CheckForWin(GameArea):
        return [GameArea,parents]
    if level == maxLevel:
        return [GameArea,parents]
    turn : int = CheckTurn(GameArea)
    solutions : list = generatePossibleMoves(GameArea, CheckTurn(GameArea))
    HOfN : list = []
    for solution in solutions:
        oneSol = {Heurstic(solution,move):solution}
        HOfN.append(oneSol)
    if turn == 1:
        highest : int = -22222
        highestList = []
        for d in HOfN:
            for h in d.keys():
                if h > highest:
                    highest = h
                    highestList = d.get(h)
        return greedy(highestList,CheckTurn(highestList),level+1,maxLevel,parents)
    else :
        lowest : int = 2222222
        lowestList = []
        lowestMany = []
        for d in HOfN:
            for h in d.keys():
                if h < lowest:
                    lowest = h
        for d in HOfN:
            if next(iter(d)) == lowest:
                lowestMany.append(d.get(next(iter(d))))

        lowestList = random.choice(lowestMany)
        return greedy(lowestList,CheckTurn(lowestList),level+1,maxLevel,parents)

def CheckForDraw(GameArea : list) -> bool:
    nCount : int = sum(row.count("N") for row in GameArea)
    if nCount == 0:
        return True
    else: 
        return False
    
def play(GameArea: list):

    while True:
        display(GameArea)
        row = int(input("Enter row: "))-1
        col = int(input("Enter col: "))-1
        GameArea[row][col] = "X"
        if CheckForWin(GameArea) or CheckForDraw(GameArea):
            print("Game ended")
            break
        GameArea = greedy(GameArea,CheckTurn(GameArea),1,16,[])[1][1]
        if CheckForWin(GameArea) or CheckForDraw(GameArea):
            display(GameArea)
            print("Game ended")
            break
play(GameArea)
# BFS(GameArea)
