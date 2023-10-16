class MazeMaker():

    def __init__(self):
        pass

    def print_maze(self, maze):
        for row in maze:
            print(''.join(row))

    def convert_maze_to_image(self, maze, wall_char='#', path_char=' ', searched_char='x',starting_char="A",ending_char="B"):
        from PIL import Image,ImageDraw

        wall_color = (0, 0, 0)
        path_color = (255, 255, 255)
        searched_color = (255, 255, 0)
        starting_color = (0,255,0)
        ending_color = (255,0,0)
        cell_size = 30 

        width = len(maze[0]) * cell_size
        height = len(maze) * cell_size

        image = Image.new('RGB', (width, height), wall_color)

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == path_char:
                    for dy in range(cell_size):
                        for dx in range(cell_size):
                            image.putpixel(
                                (x * cell_size + dx, y * cell_size + dy), path_color)
                elif cell == starting_char:
                    for gy in range(cell_size):
                        for gx in range(cell_size):
                            image.putpixel(
                                (x * cell_size + gx, y * cell_size + gy), starting_color)
                
                elif cell == ending_char:
                    for zy in range(cell_size):
                        for zx in range(cell_size):
                            image.putpixel(
                                (x * cell_size + zx, y * cell_size + zy), ending_color)
                

                elif cell == searched_char:
                    for ty in range(cell_size):
                        for tx in range(cell_size):
                            image.putpixel(
                                (x * cell_size + tx, y * cell_size + ty), searched_color)

        return image


def maze_to_image(maze_for_image: list):
    MazeApp = MazeMaker()
    maze = maze_for_image
    if maze:
        # MazeApp.print_maze(maze)
        maze_image = MazeApp.convert_maze_to_image(maze)
        maze_image.save('maze_solved.png')
        print("Maze solved and saved as maze_solved.png")
