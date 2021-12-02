"""
This module contains the Node class which makes up a board; and Node-related functionality
"""
import math
import pygame as pg

offset_y = 100


class Node:
    """
    The individual nodes and corresponding functionality
    """
    def __init__(self, position, g=math.inf, h=math.inf, f=math.inf):

        self.position = position
        self.f = f
        self.g = g
        self.h = h
        self.color = (0, 0, 0)
        self.edge = 20
        self.visited = False
        self.path = False
        self.moving = False

    def __eq__(self, other):
        """
        Custom set to allow PriorityQueue to work properly
        :param other: Node
        :return: Boolean
        """
        if self.f == other.f and self.h == other.h:
            return True
        return False

    def __lt__(self, other):
        """
        Custom set to allow PriorityQueue to work properly
        :param other: Node
        :return: Boolean
        """
        if self.f == other.f:
            return self.h < other.h
        return self.f < other.f

    def __le__(self, other):
        """
        Custom set to allow PriorityQueue to work properly
        :param other: Node
        :return: Boolean
        """
        if self.f == other.f:
            return self.h <= other.h
        return self.f < other.f

    def __gt__(self, other):
        """
        Custom set to allow PriorityQueue to work properly
        :param other: Node
        :return: Boolean
        """
        if self.f == other.f:
            return self.h > other.h
        return self.f > other.f

    def __ge__(self, other):
        """
        Custom set to allow PriorityQueue to work properly
        :param other: Node
        :return: Boolean
        """
        if self.f == other.f:
            return self.h >= other.h
        return self.f >= other.f

    def update_f(self):
        """
        Updates the f-value by summing the g and h values
        :return: None
        """
        self.f = self.g + self.h

    def set_g(self, val):
        """
        Sets the g-value
        :param val: int (value that g is to be set to)
        :return: None
        """
        self.g = val

    def set_h(self, val):
        """
        Sets the h-value
        :param val: int (value that h is to be set to)
        :return: None
        """
        self.h = val

    def pos_to_ind(self):
        """
        Returns the index in the Node matrix of a Board from its absolute x,y position
        :return: (y, x) as integers
        """
        x_ind = int(self.position[0] / self.edge)
        y_ind = int(self.position[1] / self.edge)
        return y_ind, x_ind

    def get_distance(self, other_node):
        """
        Calculates the distance of the current node to another node, not allowing diagonals
        :param other_node: Node
        :return: int (distance)
        """
        x_diff = abs(self.position[0] - other_node.position[0])
        y_diff = abs(self.position[1] - other_node.position[1])
        d = x_diff + y_diff

        return d

    def is_over(self, pos):
        """
        Detects if the mouse is hovering over the Node
        :param pos: (x,y) mouse position
        :return: Boolean
        """
        bug_offset_y = self.edge * 5
        pos = (pos[0], pos[1] - bug_offset_y)

        if self.position[0] <= pos[0] <= (self.position[0] + self.edge):
            if (self.position[1] - offset_y) <= pos[1] <= (self.position[1] + self.edge - offset_y):
                return True
        return False

    def draw_change(self, screen, color=(255, 255, 255)):
        """
        Draws color changes of Nodes on the board
        :param screen: Surface
        :param color: (R,G,B) color coding
        :return: None
        """
        # if self.selected: not necessary, is it?
        if self.visited:
            color = (0, 239, 255)  # make lighter blue
        if self.path:
            color = (0, 255, 68)  # light green

        pg.draw.rect(screen, color, (self.position[0] + 1, self.position[1] + offset_y + 1,
                                     self.edge - 1, self.edge - 1))
