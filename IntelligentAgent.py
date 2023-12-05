import random
import math
from BaseAI import BaseAI


class IntelligentAgent(BaseAI):

    def evaluate(self, grid):
        #print (grid.map)
        sumGrid = 0
        #return len(grid.getAvailableCells())
        # if row number is odd go the other way 
        for i in range(len(grid.map)):
            for j in range(len(grid.map)):
                if (i % 2 == 0): # even row
                    if (i != 0): #if i = 2
                        sumGrid += grid.map[i][j] * pow(4, (15 // i) - j)
                    else: # if i = 0
                        sumGrid += grid.map[i][j] * pow(4, 15 - j)
                
                else: #odd row
                    if (i == 1): 
                       sumGrid += grid.map[i][j] * pow(4, math.ceil(15 / 2) + j)
                     
                    else: # i = 3
                        sumGrid += grid.map[i][j]* pow(4, j)
                
        return sumGrid
        #loop through grid.map and multiply by heuristic
        #grid.map is a 2d list



    def minimize(self, grid, depth, alpha, beta):
        # if depth of tree greater than some number also return heuristic
        # when calling minimize/maximize increase depth of tree
        if not grid.getAvailableCells() or depth > 3:
            return (None, self.evaluate(grid))

        minChild = None
        minUtility = math.inf
        info = (minChild, minUtility)

        for child in grid.getAvailableCells():
            #print(child[0])
            #print(child[1])
            copy1 = grid.clone()
            copy2 = grid.clone()
            
            copy1.insertTile(child, 2)
            copy2.insertTile(child, 4)
            #print(child)
            
            max1 = self.maximize(copy1, depth + 1, alpha, beta)
            max2 = self.maximize(copy2, depth + 1, alpha, beta)
            # print(max1, max2)
            utility = 0.9 * max1[1] + 0.1 * max2[1]

            if utility < minUtility:
                minChild = child
                minUtility = utility
                info = (minChild, minUtility)
                
            if minUtility <= alpha:
                break
            
            if minUtility < beta:
                beta = minUtility
        
        return info

    def maximize(self, grid, depth, alpha, beta):
        if not grid.getAvailableMoves() or depth > 3:
            return (None, self.evaluate(grid))

        maxChild = None
        maxUtility = -math.inf
        info = (maxChild, maxUtility)

        for child in grid.getAvailableMoves():
            #print(child[1])
    
            utility = self.minimize(child[1], depth + 1, alpha, beta)[1]

            if utility > maxUtility:
                maxUtility = utility
                info = (child[0], utility)
                
            if maxUtility >= beta:
                break
            
            if maxUtility > alpha:
                alpha = maxUtility

        return info

    def getMove(self, grid):
        # Selects a random move and returns it
        #moveset = grid.getAvailableMoves()
        # return random.choice(moveset)[0] if moveset else None
        child = self.maximize(grid, 0, -math.inf, math.inf)
        return child[0]
