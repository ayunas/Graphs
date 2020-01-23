

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



        # visited = [start_vert]
        # s = Stack()
        # parents = self.parents(start_vert)
        # for p in parents:
        #     s.push(p)
        # while s.size() > 0:
        #     # print('s.size()', s.size())
        #     vert = s.pop()
        #     # print(s.pop())
        #     if vert not in visited:
        #         visited.append(vert)
        #         parents = self.parents(vert)
        #         for p in parents:
        #             s.push(p)
        # return visited

        
    def ancestor(self,child):

        parents = self.dft(child)
        print('parents', parents)

        # print('child in ancestor', child)

        # if child not in self.vertices:
        #     return -1

        # parents = self.vertices[child]

        # self.dfs(6)
       
        # for p in parents:
        #     print('p', p)
        #     self.ancestor(p)

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
    def size(self):
        return len(self.stack)
    
    def __repr__(self):
        return str(self.stack)