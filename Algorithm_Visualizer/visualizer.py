import math

import pygame
import random
pygame.init()

# defining color variables in a class to not cloudy the name space


class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255,255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = BLACK
    GRADIENTS = [
        (128,128,128),
        (160,160,160),
        (192,192, 192)
    ]
    TRANS = (1, 1, 1)
    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 40)

    # 50px padding on the left and the right. 100px in total
    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width: int, height: int, lst: []):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        # set window caption
        pygame.display.set_caption("Dawson's Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        # determining the amount of padding based on the length of the list  and the width of the window
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info: DrawInformation, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.WHITE)
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 5))
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.WHITE)
    # centering the text using bilt. using get_width to get the width of the controls text to then get an idea of its
    # center so I can center put the center of the text with the center of the page
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 55))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.WHITE)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 75))
    '''
    surf = pygame.surface.Surface((100, 50))
    txt_surf = draw_info.FONT.render("Speed", 1, draw_info.WHITE)
    txt_rect = txt_surf.get_rect(center=(50, 15))
    surf.fill((100, 100, 100))
    surf.blit(txt_surf, txt_rect)  # this surface never changes
    # dynamic graphics - button surface #
    button_surf = pygame.surface.Surface((20, 20))
    button_surf.fill(draw_info.TRANS)
    button_surf.set_colorkey(draw_info.TRANS)
    pygame.draw.circle(button_surf, draw_info.BLACK, (10, 10), 6, 0)
    pygame.draw.circle(button_surf, draw_info.GREEN, (10, 10), 4, 0)
    '''
    draw_list(draw_info)
    # updates the screen
    pygame.display.update()


def draw_list(draw_info: DrawInformation, color_positions= {}, clear_background= False):
    lst = draw_info.lst
    if clear_background:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, draw_info.width - draw_info.SIDE_PAD,
                      draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    # index and value in the list
    for i, val in enumerate(lst):
        # getting the start point for x, then multiplying the index by the width of the block_width
        x = draw_info.start_x + i * draw_info.block_width
        # cant use the value of the number in the list as the height because we have a range.
        # subtracting the value by the minimum value helps to get an idea of the height respective to all numbers
        # then multiply by the height
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        # always staying in range
        color = draw_info.GRADIENTS[i % 3]
        if i in color_positions:
            color = color_positions[i]
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))

    if clear_background:
        pygame.display.update()


def generate_starting_list(list_size, min_val, max_val):
    starting_list = []
    for _ in range(list_size):
        val = random.randint(min_val, max_val)
        starting_list.append(val)

    return starting_list


def bubble_sort(draw_info, ascending = True):
    lst = draw_info.lst
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j+1]

            if (num1> num2 and ascending) or (num1 < num2 and not ascending):
                # swapping the values in the array
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                # generator, similar ot an iterator and pause the execution of the function and wait to procesed.
                # yield pauses the current state of the
                # function so that the next time we call it to run it is going to start at the next item
                # if you dont yield to program wont respond while its sorting
                yield True

    return lst

def insertion_sort(draw_info, ascending):
    lst = draw_info.lst
    for index in range(1, len(lst)):
        current = lst[index]
        while True:
            ascending_sort = index > 0 and lst[index-1] > current and ascending
            descending_sort = index > 0 and lst[index - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break

            lst[index] = lst[index-1]
            index = index - 1
            lst[index] = current
            draw_list(draw_info, {index-1: draw_info.GREEN, index: draw_info.RED}, True)
            yield True
    return lst




def main():
    run = True
    clock = pygame.time.Clock()
    list_size = 50
    min_val = 0
    max_val = 100
    lst = generate_starting_list(list_size, min_val, max_val)

    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        # defining the number of frames that the clock will tick at thus defining how quickly this loop runs
        clock.tick(30)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            # render the display
            draw(draw_info, sorting_algo_name, ascending)
        # this returns a list of all of the that have occured since the last time it ran
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # clicking x to exit program
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_starting_list(list_size, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting is False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"

    pygame.quit()


if __name__ == "__main__":
    main()









