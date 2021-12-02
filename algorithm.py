import random
import pygame as pg


def reconstruct_path(node_history, current_node, screen):
    """
    Reconstructs the best possible path from the initial node to the goal node using the node history
    and the current node (which is the goal node at the initial call of this function)
    :param screen: screen
    :param node_history: map
    :param current_node: Node (goal node)
    :return: list
    """
    total_path = [current_node]
    # visualization
    current_node.path = True
    current_node.draw_change(screen)
    pg.display.update()
    pg.time.delay(30)

    while current_node.position in node_history.keys():
        current_node = node_history[current_node.position]
        total_path.insert(0, current_node)

        # visualization
        current_node.path = True
        current_node.draw_change(screen)
        pg.display.update()
        pg.time.delay(30)

    return total_path


def a_star(initial_node, goal_node, board, screen):
    """
    Pathfinder Visualization - pathfinding algorithm
    :param initial_node: Node (initial)
    :param goal_node: Node (goal)
    :param board: Board
    :param screen: screen
    :return: None
    """
    node_history = {}

    # all nodes g and f values have been set to infinity per default
    # now we set the first node's values appropriately
    initial_node.g = 0
    initial_node.f = initial_node.get_distance(goal_node)
    board.fringe.put(initial_node)

    while not board.fringe.empty():
        current_node = board.fringe.get()

        # visualization
        current_node.draw_change(screen)
        pg.display.update()
        pg.time.delay(10)

        if current_node.pos_to_ind() == goal_node.pos_to_ind():
            return reconstruct_path(node_history, current_node, screen)

        neighbors = board.get_neighbors(current_node)
        random.shuffle(neighbors)

        for neighbor_node in neighbors:
            # g is distance from start to neighbor through current
            g = current_node.get_distance(initial_node) + current_node.get_distance(neighbor_node)

            # visualization
            current_node.visited = True
            current_node.draw_change(screen)
            neighbor_node.draw_change(screen, (175, 0, 188))
            pg.display.update()
            pg.time.delay(10)

            if g < neighbor_node.g:
                node_history[neighbor_node.position] = current_node
                neighbor_node.g = g
                h_val = neighbor_node.get_distance(goal_node)
                neighbor_node.set_h(h_val)
                neighbor_node.update_f()
                if neighbor_node not in board.fringe.queue:
                    board.fringe.put(neighbor_node)
    return False


def dijkstra(initial_node, goal_node, board, screen):
    """
    Dijkstra's pathfinding algorithm
    :param initial_node: Node (initial)
    :param goal_node: Node (goal)
    :param board: Board
    :param screen: screen
    :return: None
    """
    y, x = initial_node.pos_to_ind()
    board.nodes[y][x].g = 0
    board.nodes[y][x].f = 0
    board.fringe.put(board.nodes[y][x])
    node_history = {}

    # all nodes g values have been set to infinity per default; now we set the first node's values appropriately
    while board.fringe.queue:

        current_node = board.fringe.get()

        # visualization
        current_node.draw_change(screen)
        pg.display.update()
        pg.time.delay(0)

        if current_node.pos_to_ind() == goal_node.pos_to_ind():
            return reconstruct_path(node_history, current_node, screen)

        neighbors = board.get_neighbors(current_node)
        random.shuffle(neighbors)

        for neighbor_node in neighbors:
            # g is distance from start to neighbor through current
            g = current_node.get_distance(initial_node) + current_node.get_distance(neighbor_node)

            # visualization
            current_node.visited = True
            current_node.draw_change(screen)
            neighbor_node.draw_change(screen, (175, 0, 188))
            pg.display.update()
            pg.time.delay(0)

            if g < neighbor_node.g:
                node_history[neighbor_node.position] = current_node
                neighbor_node.g = g
                neighbor_node.f = g
                board.fringe.put(neighbor_node)
    return False
