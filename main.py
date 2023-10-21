from mazemaker import maze_to_image

class maze_solver:
    def __init__(self) -> None:
        self.labirent_vec = []
        with open("labirent.txt", "r") as file:
            for line in file:
                self.labirent_vec.append(line)
        self.start = ()
        self.end = ()
        self.mazedone = False
        self.nodes = []
        self.current = []
        self.explored = []
        # print(self.raw_file)
    # if " ", can go
    # if "#" can't pass

    def StartEndFind(self):
        for y, row in enumerate(self.labirent_vec):
            for x, col in enumerate(row):
                if col == "A":
                    print(f"Start:  {x}. column {y} .row")
                    # self.labirent_vec[y][x] == "A"
                    self.start = (x, y)
                    self.current = (x, y)
                elif col == "B":
                    print(f"End:  {x}. column {y} .row")
                    self.end = (x, y)

    def CheckSurround(self):
        x, y = self.current
        neighbors = [(x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1)]

        for neighbor_x, neighbor_y in neighbors:
            if 0 <= neighbor_x < len(self.labirent_vec[y]) and 0 <= neighbor_y < len(self.labirent_vec):
                neighbor_char = self.labirent_vec[neighbor_y][neighbor_x]

                if neighbor_char != "#" and (neighbor_x, neighbor_y) not in self.nodes and (neighbor_x, neighbor_y) not in self.explored:
                    self.nodes.append((neighbor_x, neighbor_y))


    def Move(self, search="Depth"):
        while not self.mazedone:
            self.CheckSurround()
            if self.current == self.end:
                print("Done.")
                break
            self.explored.append(self.current)
            try:
                self.nodes.remove(self.current)
            except:
                pass
            if not self.nodes:  # if cannot find any nodes, there isnt any end
                print("Couldn't find any end point.")
                break
            if search == "Depth":
                self.current = self.nodes.pop()  # current is the next node
            else:
                if len(self.nodes) > 1:
                    self.current = self.nodes[0]
                    self.nodes = self.nodes[1:]
                else:
                    self.current = self.nodes.pop()

    def FinalImage(self, show_explored=False):
        foo = []
        # replacing " " with "x" to show explored
        for y, row in enumerate(self.labirent_vec):
            foo.append((list(row)))
            for x, col in enumerate(row):
                dull = (x, y)
                if dull in self.explored and foo[y][x] != "A":
                    foo[y][x] = "x"
        maze_to_image(maze_for_image=foo)


Solver = maze_solver()
Solver.StartEndFind()
Solver.Move(search="Depth")
Solver.FinalImage()
