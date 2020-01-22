

class Graph:
    def __init__(self):
        self.vertices = {}  #dictionary not a set
    
    def add_vert(self,vert):

        parent,child = vert
        if parent not in self.vertices:
            self.vertices[parent] = {child}
        else:
            self.vertices[parent].add(child)


        # if type(vert) == tuple:
            
            # print('parent,child', parent,child)
            # self.vertices[parent] = {child}
            # self.vertices[child] = set()
            # self.vertices[parent]

        #     if parent in self.vertices and child in self.vertices:
        #         self.vertices[parent].add(child)
        #         return
        #     elif parent in self.vertices and child not in self.vertices:
        #         self.vertices[child] = set()
        #         self.vertices[parent].add(child)
        #         return
        #     else:  #parent and child not in self.vertices
        #         self.vertices[parent] = set()
        #         self.vertices[child] = set()
        #         self.vertices[parent].add(child)
        #         print(self.vertices[parent],self.vertices[child])
        # elif type(vert) == list:
        #     pass
        # else: #vert is an int, str, etc.
        #     self.vertices[parent] = set()

    def __repr__(self):
        return str(self.vertices)

