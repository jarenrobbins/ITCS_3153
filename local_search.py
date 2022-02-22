import nqueens
import random
import math

def schedule(T, decayRate):

    return T*decayRate

def simulatedAnnealing(initBoard, decayRate, T_Threshold):
    T = 100
    current = initBoard
    current.h = nqueens.numAttackingQueens(current)

    while (T > 0):
        T = schedule(T, decayRate)

        if (T < T_Threshold):
            return current

        neighbors = nqueens.getSuccessorStates(current)
        next = random.choice(neighbors)
        E_diff = nqueens.numAttackingQueens(next) - current.h

        if (E_diff > 0):
            current = next
        else:
            num1 = random.random()
            num2 = math.exp(E_diff/T)

            if (num1 < num2):
                current = next
            
        
        
    