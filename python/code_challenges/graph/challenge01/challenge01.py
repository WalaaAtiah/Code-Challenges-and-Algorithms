# Write here the code challenge solution
class Node:
    '''
    this class to create a node(vertex) take value as argument
    '''
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    '''
    this class create the edge  that connects between two vertex ,takes vertex ,weight as arguments
    '''

    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Grahp:
    '''
    this class create the graph represent as Adjacency List  have :
    1 attribute adj_list
    3 methode  add_node(),add_edge(),__str__()
    '''
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        """
        this methode to add a node to the graph return this node
        """

        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        """
        this method to create a new edge between  two vertex by takes node1 , node2 and weight  as parameter and append it in adj_list
        """
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output

    def GraphBreadthFirst(self,root):
        """
        method that take a value as a parameter, then traverse through the graph using Breadth First way starting from the inputted value, and appending all the visited nodes values in a returned array
        
        input: root(node)
        output: list
        """
        queue=[]
        visited=[]
        queue.append(root)
        
        while queue :
            for child in self.adj_list[queue[0]]:
                if child.vertex not in queue and child.vertex not in visited:
                    queue.append(child.vertex)
            visited.append(queue.pop(0))
        
        return [x.value for x in visited]
                
           
 

if __name__ == "__main__":
    graph1 = Grahp()
    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")
    e = graph1.add_node("E")

    graph1.add_edge(a,b)
    graph1.add_edge(a,e)
    graph1.add_edge(b,c)
    graph1.add_edge(b,e)
    graph1.add_edge(e,d)
    graph1.add_edge(d,c)

    print ("\n*********************************   Example 1   **********************************\n") 

    print ("Graph Representation as Adjacency List ")
    print(graph1)
    print ("Breadth First traverse if the root is A")
    print("Output ",graph1.GraphBreadthFirst(a))


    graph2 = Grahp()

    a = graph2.add_node("A")
    b = graph2.add_node("B")
    c = graph2.add_node("C")
    e = graph2.add_node("E")
    d = graph2.add_node("D")
    f = graph2.add_node("F")
    g = graph2.add_node("G")
    h = graph2.add_node("H")
    i = graph2.add_node("I")
    k = graph2.add_node("K")

    graph2.add_edge(a,c)
    graph2.add_edge(a,e)
    graph2.add_edge(a,b)

    graph2.add_edge(b,d)
    graph2.add_edge(e,g)
    graph2.add_edge(c,f)
    graph2.add_edge(e,f)

    graph2.add_edge(d,e)
    graph2.add_edge(g,h)
    graph2.add_edge(f,i)
    graph2.add_edge(f,h)

    graph2.add_edge(h,k)
    graph2.add_edge(i,k)

    print ("\n*********************************   Example 2   **********************************\n") 

    print ("Graph Representation as Adjacency List ")
    print(graph2)
    print ("Breadth First traverse if the root is A")
    print("Output ",graph2.GraphBreadthFirst(a))
