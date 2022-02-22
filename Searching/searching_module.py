#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:59:08 2021

@author: jarenrobbins
"""

import uninformed_search as us
import read_and_write as rw
import informedSearchGroup as isg
import heapq
import localsearch as ls
import nqueens
    

def uninformedSearch(grid,start,goal,bfs=True):
    
    openList = [start]
    closedList = []
    while(True):
        if openList == []:
            return
        if(bfs):
            node = openList.pop(0)
        else:
            node = openList.pop(len(openList)-1)
        if node.value == goal.value:
            break
        closedList.append(node)
        us.expandNode(node, grid, closedList, openList)
    path = []
    while node.parent != None:
        path.append(node.value)
        node = node.parent
    path.append(node.value)
    path_costs = []
    for node in path:
        path_costs.append(grid[node[0]][node[1]])
    pathCost = sum(path_costs)
    print("Uninformed Search\nExpanded nodes: %s\nPath cost: %s" % (len(closedList), pathCost))
    return path


def informedSearch(grid,start,goal):
    
    openList = [start]
    closedList = []
    while(True):
        if openList == []:
            return
        node = heapq.heappop(openList)
        if node.value == goal.value:
            break
        closedList.append(node)
        children = us.getNeighbors(node.value, grid)
        open_list_locations = [nodes.value for nodes in openList]
        closed_list_locations = [nodes.value for nodes in closedList]
        for c in children:
            new_node = isg.Node(grid[c[0]][c[1]], isg.heuristic(c, goal.value), c, node)
            if c in open_list_locations:
                new_g = new_node.g
                old_g = node.g
                if new_g < old_g:
                    openList.remove(node)
                    heapq.heappush(openList, new_node)
                    if c in closed_list_locations:
                        closedList.remove(node)
            elif c not in closed_list_locations:
                heapq.heappush(openList, new_node)
    path = []
    while node != start:
        path.append(node.value)
        node = node.parent
    path.append(node.value)
    path_costs = []
    for node in path:
        path_costs.append(grid[node[0]][node[1]])
    pathCost = sum(path_costs)
    print("Informed Search\nExpanded nodes: %s\nPath cost: %s" % (len(closedList), pathCost))
    return path


def localSearch():
    print('**********************************')
    print('Board size: 4')
    print('**********************************')
    print('######################################')
    print('Decay rate 0.9 T Threshold: 1e-06')
    print('######################################')
    h1 = []
    for i in range(10):
        print('Run ',i)
        print('Initial board:')
        board = nqueens.Board(4)
        nqueens.Board.rand(board)
        nqueens.Board.printBoard(board)
        print('h-value: ', nqueens.numAttackingQueens(board))
        new_board = ls.simulatedAnnealing(board, 0.9, 0.000001)
        final = nqueens.numAttackingQueens(new_board)
        print('Final board h value: ', final)
        h1.append(final)
    total_h1 = sum(h1)
    print('Average h-cost of final solutions: ', total_h1/10)
    print('**********************************')
    print('Board size: 8')
    print('**********************************')
    print('######################################')
    print('Decay rate 0.9 T Threshold: 1e-06')
    print('######################################')
    h2 = []
    for i in range(10):
        print('Run ',i)
        print('Initial board:')
        board = nqueens.Board(8)
        nqueens.Board.rand(board)
        nqueens.Board.printBoard(board)
        print('h-value: ', nqueens.numAttackingQueens(board))
        new_board = ls.simulatedAnnealing(board, 0.9, 0.000001)
        final = nqueens.numAttackingQueens(new_board)
        print('Final board h value: ', final)
        h2.append(final)
    total_h2 = sum(h2)
    print('Average h-cost of final solutions: ', total_h2/10)
    print('**********************************')
    print('Board size: 16')
    print('**********************************')
    print('######################################')
    print('Decay rate 0.9 T Threshold: 1e-06')
    print('######################################')
    h3 = []
    for i in range(10):
        print('Run ',i)
        print('Initial board:')
        board = nqueens.Board(16)
        nqueens.Board.rand(board)
        nqueens.Board.printBoard(board)
        print('h-value: ', nqueens.numAttackingQueens(board))
        new_board = ls.simulatedAnnealing(board, 0.9, 0.000001)
        final = nqueens.numAttackingQueens(new_board)
        print('Final board h value: ', final)
        h3.append(final)
    total_h3 = sum(h3)
    print('Average h-cost of final solutions: ', total_h3/10)
    
    
grid = rw.readGrid('grid.txt')
us_start = us.Node()
us_goal = us.Node([9,9])
is_goal = isg.Node(1,0,[9,9])
is_start = isg.Node(1,0,[0,0])
is_start.h = isg.heuristic(is_start.value, is_goal.value)
us_path = uninformedSearch(grid, us_start, us_goal)
is_path = informedSearch(grid, is_start, is_goal)
rw.outputGrid(grid, us_start.value, us_goal.value, us_path)
##rw.outputGrid(grid, is_start.value, is_goal.value, is_path)