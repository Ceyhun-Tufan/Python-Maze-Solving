from time import sleep

class maze_solver:
    def __init__(self) -> None:
        self.labirent_vec = []
        with open("labirent.txt","r") as file:
            for line in file:
                self.labirent_vec.append(line)
        self.start = ()
        self.end = ()
        self.mazedone = False
        self.nodes = []
        self.current = []
        self.explored = []
        #print(self.raw_file)
    #eğer " " ise geçilebilir
    #eğer # ise duvar

    def StartEndFind(self):
        for y,row in enumerate(self.labirent_vec):
            for x,col in enumerate(row):
                if col == "A":
                    print(f"Başlangıç noktası:  {x}. column {y} .row")
                    #self.labirent_vec[y][x] == "A"
                    self.start = (x,y)
                    self.current = (x,y)
                elif col == "B":
                    print(f"Bitiş noktası:  {x}. column {y} .row")
                    self.end = (x,y)
        

    def CheckSurround(self,search="None"):     
        x, y = self.current
        # Kontrolleri daha doğru bir şekilde yapın
        if x - 1 >= 0 and self.labirent_vec[y][x - 1] != "#":
            neighbor = (x - 1, y)
            if neighbor not in self.nodes and neighbor not in self.explored:
                self.nodes.append(neighbor)
                #print(f"left and ---CURRENT---> {self.current}")
        if x + 1 < len(self.labirent_vec[y]) and self.labirent_vec[y][x + 1] != "#":
            neighbor = (x + 1, y)
            if neighbor not in self.nodes and neighbor not in self.explored:
                self.nodes.append(neighbor)
                #print(f"right and ---CURRENT---> {self.current}")
        if y - 1 >= 0 and self.labirent_vec[y - 1][x] != "#":
            neighbor = (x, y - 1)
            if neighbor not in self.nodes and neighbor not in self.explored:
                self.nodes.append(neighbor)
                #print(f"down and ---CURRENT---> {self.current}")
        if y + 1 < len(self.labirent_vec) and self.labirent_vec[y + 1][x] != "#":
            neighbor = (x, y + 1)
            if neighbor not in self.nodes and neighbor not in self.explored:
                self.nodes.append(neighbor)
                #print(f"up and ---CURRENT---> {self.current}")


    def Move(self):
        while not self.mazedone:
            self.CheckSurround()
            if self.current[0] == self.end[0] and self.current[1] == self.end[1]:
                print("Done.")
                break
            print(self.current)
            print(self.explored)
            self.explored.append(self.current)
            try:
                self.nodes.remove(self.current)
            except:
                pass
            if not self.nodes:  # Eğer düğüm kalmazsa çözüm yok demektir.
                print("Çözüm bulunamadı.")
                break
            self.current = self.nodes.pop()  # Bir sonraki düğümü al

Solver = maze_solver()
Solver.StartEndFind()
Solver.Move()

