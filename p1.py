class PQueue(): 
    def __init__(self):
        self.dict = {} 
        self.keys = [] 
        self.sorted = False 
    def push(self, k, v): 
        self.dict[k] = v 
        self.sorted = False 
    def _sort(self): 
        self.keys = sorted(self.dict, key=self.dict.get,reverse=True) 
        self.sorted = True 
    def pop(self): 
        try: 
            if not self.sorted: 
                self._sort() 
            key = self.keys.pop() 
            value = self.dict[key] 
            self.dict.pop(key) 
            return key, value 
        except: 
            return None

def heuristics(path): 
    h = {} 
    with open(path, 'r') as file: 
        for line in file: 
            k, v = line.split(", ") 
            h[k] = int(v)
    return h

def path_costs(path): 
    c = {} 
    with open(path, 'r') as file: 
        for line in file: 
            line = line.split(", ") 
            v = int(line.pop()) 
            e1 = line.pop() 
            e2 = line.pop() 
            if e1 not in c: 
                c[e1] = {} 
            if e2 not in c: 
                c[e2] = {} 
            c[e1][e2] = c[e2][e1] = v 
    return c

def a_star(start, goal, h, g): 
    frontier = PQueue()
    frontier.push(start, h[start]) 
    while True: 
        
            path, cost = frontier.pop() 
            print(path+ " " +str(cost)) 
        
            end = path.split("->")[-1]  
         
            cost -= h[end] 
            if goal == end: 
                break 
            for node, weight in g[end].items(): 
         
                new_cost = cost + weight + h[node] 
                new_path = path + "->" + node 
        
                frontier.push(new_path, new_cost)

a_star('Arad', 'Bucharest', heuristics('./Heuristics.txt'),path_costs("./Paths.txt"))