"""
This module contains the board class and the related functionality
"""
from Node import Node

import pygame as pg
import queue

offset_y = 100


class Board:
    """
    The Board class allows to create board objects, on which everything happens
    """
    def __init__(self, rows, cols):

        self.rows = rows
        self.cols = cols
        self.edge = int(900 / self.rows)
        self.nodes = [[Node((int(x * self.edge), int(y * self.edge))) for x in range(cols)] for y in range(rows)]
        self.fringe = queue.PriorityQueue()

    def get_neighbors(self, current_node):
        """
        Returns a list of all viable neighbors of a Node
        :param current_node: Node
        :return: [Node, Node,...]
        """
        x = current_node.pos_to_ind()[1]
        y = current_node.pos_to_ind()[0]

        neighbors = []

        if 0 <= (x + 1) < self.cols:
            neighbors.append(self.nodes[y][x + 1])
        if 0 <= (y + 1) < self.rows:
            neighbors.append(self.nodes[y + 1][x])
        if 0 <= (x - 1) < self.cols:
            neighbors.append(self.nodes[y][x - 1])
        if 0 <= (y - 1) < self.rows:
            neighbors.append(self.nodes[y - 1][x])

        return neighbors

    def draw(self, screen):
        """
        Draws the board
        :return: None
        """
        # draw the grid
        color = (0, 0, 0)
        for i in range(self.cols + 1):
            pg.draw.line(screen, color, (i * self.edge, offset_y), (i * self.edge, 1500 + offset_y))
            pg.draw.line(screen, color, (0, i * self.edge + offset_y), (1500, i * self.edge + offset_y))
