"""
GUI component that does everything related to the pygame loops and the GUI
"""
import sys
from Board import Board
from Button import Button
import legend
import algorithm

import pygame as pg
pg.init()


def set_titlebar():
    """
    Sets the titlebar
    :return: None
    """
    pg.display.set_caption("Path Finding Visualization Tool")


def write_text(text, font, color, x, y):
    """
    Function to write text in the GUI
    :param text: String
    :param font: pg.font.SysFont
    :param color: RGB tuple
    :param y: int (vertical position)
    :return: None
    """
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)


def write_legend():

    font = pg.font.SysFont('montserrat', 17)
    write_text('unvisited Node', font, black, 370, 67)
    write_text('checked Node', font, black, 472, 67)
    write_text('visited Node', font, black, 577, 67)
    write_text('path Node', font, black, 682, 67)
    write_text('Start Node', font, black, 778, 67)
    write_text('Goal Node', font, black, 882, 67)


def draw_game_menu():
    """
    Draws the screen and the buttons for the home-menu
    :return:
    """
    # draw all other game menu buttons here
    run_algorithm_button.draw(screen)
    drop_down_button.draw(screen)


def draw_drop_down_menu():
    """
    Draws the buttons in the drop-down menu
    :return: None
    """
    astar_button.draw(screen)
    dijkstra_button.draw(screen)


def close_drop_down_menu():
    """
    Closes the drop-down menu by redrawing the screen
    :return: None
    """
    screen.fill((255, 255, 255))
    board.draw(screen)
    draw_icons(screen, start_pos, goal_pos)
    draw_game_menu()
    write_legend()
    legend.draw_legend(screen)
    pg.display.update()
    drop_down_button.selected = False


def initiate_icons():
    """
    Loads icons and modifies them appropriately for further processing
    :return: (Surface, Surface, (x,y), (x,y)) icons and their positions
    """
    raw_corner = pg.image.load('corner.png')
    sized_corner = pg.transform.scale(raw_corner, (board.edge - 8, board.edge - 8))
    initial = pg.transform.rotate(sized_corner, 225)

    raw_flag = pg.image.load('flag.png')
    goal = pg.transform.scale(raw_flag, (board.edge - 4, board.edge - 4))

    first = board.nodes[int((board.rows / 3) * 1.5)][int(board.cols / 3)]
    last = board.nodes[int((board.rows / 3) * 1.5)][int((board.cols / 3) * 2)]
    start_pos = (first.position[0], first.position[1] + offset_y)
    goal_pos = (last.position[0], last.position[1] + offset_y)

    return initial, goal, start_pos, goal_pos


def draw_icons(screen, start_pos, goal_pos):
    """
    Draws the stars on random spots on the board
    :return: None
    """
    offset_x = board.edge * 1
    offset_y = board.edge * 4

    screen.blit(start, (start_pos[0] - offset_x + 1, start_pos[1] + offset_y + 3, board.edge - 3, board.edge - 3))
    screen.blit(end, (goal_pos[0] - offset_x + 3, goal_pos[1] + offset_y + 3, board.edge - 3, board.edge - 3))
    start_pos = (start_pos[0] + (board.edge / 2), start_pos[1] - 2 + (board.edge / 2))
    goal_pos = (goal_pos[0] - 3 + (board.edge / 2), goal_pos[1] - 3 + (board.edge / 2))

    return start_pos, goal_pos


def set_initial_node(start_pos):
    """
    Sets the initial node according to the icon position
    :return: Node (initial)
    """
    icon_pos = start.get_rect(center=start_pos)
    node_x = int((icon_pos.x - (icon_pos[3] / 2)) // board.edge)
    node_y = int((icon_pos.y - (icon_pos[3] / 2)) // board.edge)
    node = board.nodes[node_y][node_x]

    return node


def set_goal_node(goal_pos):
    """
    Sets the goal node
    :return: Node (goal)
    """
    icon_pos = end.get_rect(center=goal_pos)
    node_x = int((icon_pos.x - (icon_pos[3] / 2)) // board.edge)
    node_y = int((icon_pos.y - (icon_pos[3] / 2)) // board.edge)
    node = board.nodes[node_y][node_x]

    return node


offset_y = 100
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
light_blue = (0, 255, 255)
light_blue_plus = (102, 178, 255)
light_grey = (192, 192, 192)
light_grey_plus = (150, 150, 150)

board = Board(45, 75)
screen = pg.display.set_mode((1500, 1000))
clock = pg.time.Clock()
start, end, start_pos, goal_pos = initiate_icons()

# draw buttons and initiate other stuff here
run_algorithm_button = Button((1250, 25, 175, 50), light_blue, "Run Algorithm", black)
drop_down_button = Button((100, 25, 220, 50), light_grey, "Choose Algorithm", black)
# drop-down menu buttons
astar_button = Button((100, 75, 220, 50), light_grey, "A*", black, True)
dijkstra_button = Button((100, 125, 220, 50), light_grey, "dijkstra", black, True)


def game_menu():
    """
    Game loop
    :return: None
    """
    global start_pos, goal_pos

    set_titlebar()
    screen.fill((255, 255, 255))
    board.draw(screen)
    write_legend()
    legend.draw_legend(screen)
    draw_icons(screen, start_pos, goal_pos)
    initial_node = set_initial_node(start_pos)
    goal_node = set_goal_node(goal_pos)
    selected_node = None

    while True:

        draw_game_menu()
        pg.display.update()
        clock.tick(60)

        for event in pg.event.get():
            pos = (pg.mouse.get_pos()[0], pg.mouse.get_pos()[1] - offset_y)
            button_pos = pg.mouse.get_pos()

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if run_algorithm_button.is_over(button_pos):
                    if drop_down_button.text == 'A*' or drop_down_button.text == 'Choose Algorithm':
                        algorithm.a_star(initial_node, goal_node, board, screen)
                    if drop_down_button.text == 'dijkstra':
                        algorithm.dijkstra(initial_node, goal_node, board, screen)

                # dropdown menu functionality
                if drop_down_button.is_over(button_pos):
                    draw_drop_down_menu()
                    drop_down_button.selected = True
                if not drop_down_button.is_over(button_pos) and not astar_button.dropdown:
                    close_drop_down_menu()
                if astar_button.is_over(button_pos):
                    drop_down_button.text = 'A*'
                    astar_button.dropdown = True
                    close_drop_down_menu()
                if dijkstra_button.is_over(button_pos):
                    drop_down_button.text = 'dijkstra'
                    astar_button.dropdown = True
                    close_drop_down_menu()

                elif initial_node.is_over(pos):
                    selected_node = initial_node
                    selected_offset_x = initial_node.position[0] - pos[0] + board.edge
                    selected_offset_y = initial_node.position[1] - pos[1] - 3 * board.edge
                    initial_node.moving = True
                elif goal_node.is_over(pos):
                    selected_node = goal_node
                    selected_offset_x = goal_node.position[0] - pos[0] + board.edge
                    selected_offset_y = goal_node.position[1] - pos[1] - 3 * board.edge
                    goal_node.moving = True

            if event.type == pg.MOUSEMOTION:
                if selected_node is not None:
                    new_x = int((pos[0] + selected_offset_x) // board.edge)
                    new_y = int((pos[1] + selected_offset_y) // board.edge)

                    # move icons along
                    if initial_node.moving:
                        screen.fill((255, 255, 255))
                        board.draw(screen)
                        write_legend()
                        legend.draw_legend(screen)
                        start_pos = (new_x * board.edge, new_y * board.edge + offset_y)
                        draw_icons(screen, start_pos, goal_pos)
                    elif goal_node.moving:
                        screen.fill((255, 255, 255))
                        board.draw(screen)
                        write_legend()
                        legend.draw_legend(screen)
                        goal_pos = (new_x * board.edge, new_y * board.edge + offset_y)
                        draw_icons(screen, start_pos, goal_pos)

                # change button colors
                if run_algorithm_button.is_over(button_pos):
                    run_algorithm_button.color = light_blue_plus
                elif not run_algorithm_button.is_over(button_pos):
                    run_algorithm_button.color = light_blue
                if drop_down_button.is_over(button_pos):
                    drop_down_button.color = light_grey_plus
                elif not drop_down_button.is_over(button_pos) and not drop_down_button.selected:
                    drop_down_button.color = light_grey

            # set drag-and-drop locations and update nodes
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    selected_node = None
                    initial_node.moving = False
                    goal_node.moving = False
                    goal_node = set_goal_node(goal_pos)
                    initial_node = set_initial_node(start_pos)
