

class Graph:
    def __init__(self):
        self.vertices = {}  #dictionary not a set
    
    def add_vert(self,vert):
        # if type(vert) == tuple:
        parent,child = vert
        if child not in self.vertices:
            self.vertices[child] = {parent}
        else:
            self.vertices[child].add(parent)

    def parents(self,child):

        parents = []
        if child in self.vertices:
            for p in self.vertices[child]:
                parents.append(p)
            
        return parents
    
    def bft(self,start_vert):
        q = Queue()
        parents = self.vertices[start_vert]

        for p in parents:
            q.enque(p)
        print(q)
        visited = [start_vert]

        while q.size():
            vert = q.deque()
            if vert not in visited:
                visited.append(vert)
                parents = self.parents(vert)
                for p in parents:
                    q.enque(p)
        
        return visited


    
    def dft(self,start_vert):
        s = Stack()
        parents = self.parents(start_vert)
        
        for p in parents:
            s.push(p)
        
        visited = [start_vert]
        
        while s.size():
            v = s.pop()
            if v not in visited:
                visited.append(v)
                parents = self.parents(v)
                for p in parents:
                    s.push(p)
        return visited

    def dfs(self,start_vert,dest_vert):
        '''
        return a path from start to destination
        1. create a stack
        2. push a path list with starting vert to the stack
        3. initialize a visited set
        4. while the stack size > 0
            5. pop the path off the stack
            6. grab the last vert fro the latest path
            7. check to see if the vert has not been visited yet
                8.if its not, then check to see if the last vert == the destination vert
                    9. if it is, return the latest path that was popped from the stack
                10. if the last vert is not the destination vert, add the vert to visited
                11. grab the parents of the latest vert,
                    12. for each parent, create a new copy of the current path
                    13. add the new parent to the new copy of the path.
                    14. push the new path to the stack.  
        '''
        stack = Stack()
        stack.push([start_vert])  #push a path array into the stack
        visited = set()

        while stack.size() > 0:
            path = stack.pop() #get latest path
            vert = path[-1] #last vert in path.

            if vert not in visited:
                if vert == dest_vert:
                    return path
                visited.add(vert)

                for next_vert in self.parents(vert):
                    new_path = list(path)
                    # new_path = path
                    new_path.append(next_vert)
                    stack.push(new_path)

    def bfs(self,start_vert,dest_vert):
        queue = Queue()
        queue.enque([start_vert])
        visited = set()

        while queue.size() > 0:
            path = queue.deque()
            vert = path[-1]
            if vert not in visited:
                if vert == dest_vert:
                    return path
                visited.add(vert)

                parents = self.parents(vert)
                for p in parents:
                    new_path = list(path)
                    new_path.append(p)
                    queue.enque(new_path)


    def __repr__(self):
        return str(self.vertices)


class Stack():
     #using list underlying storage structure. append() / pop() = O(1) insert() = O(n)
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def clear(self):
        self.stack = []
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return str(self.stack)

class Queue:
    def __init__(self):
        self.queue = []
    def enque(self,val):
        self.queue.append(val)
        return self.queue[-1]
    def deque(self):
        removed = self.queue[0]
        self.queue = self.queue[1:]
        return removed
    def size(self):
        return len(self.queue)
    def __repr__(self):
        return str(self.queue)