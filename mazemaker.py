class MazeMaker():

    def __init__(self):
        pass

    def read_maze_from_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                maze = [list(line.strip()) for line in file.readlines()]
            return maze
        except FileNotFoundError:
            print(f"Dosya bulunamadı: {file_path}")
            return None

    def print_maze(self,maze):
        for row in maze:
            print(''.join(row))

    def convert_maze_to_image(self,maze, wall_char='#', path_char=' ',searched_char='0'):
        from PIL import Image

        wall_color = (0, 0, 0)  # Siyah
        path_color = (255, 255, 255)  # Beyaz
        searched_color = (255,255,0)

        cell_size = 30  # Her hücrenin boyutu (piksel cinsinden)

        width = len(maze[0]) * cell_size
        height = len(maze) * cell_size

        image = Image.new('RGB', (width, height), wall_color)

        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == path_char:
                    for dy in range(cell_size):
                        for dx in range(cell_size):
                            image.putpixel((x * cell_size + dx, y * cell_size + dy), path_color)
                elif cell == searched_char:
                    for ty in range(cell_size):
                        for tx in range(cell_size):
                            image.putpixel((x * cell_size + tx, y * cell_size + ty), searched_color)

        return image




def maze_to_image():
    maze_file = 'labirent.txt'  # Labirentin bulunduğu dosyanın adını değiştirin
    MazeApp = MazeMaker()
    maze = MazeApp.read_maze_from_file(maze_file)

    if maze:
        print("Labirent:")
        MazeApp.print_maze(maze)

        maze_image = MazeApp.convert_maze_to_image(maze)
        maze_image.save('labirent.png')  # Resmi kaydetmek için dosya adını değiştirin
        print("Labirent resmi oluşturuldu ve 'labirent.png' olarak kaydedildi.")


maze_to_image()