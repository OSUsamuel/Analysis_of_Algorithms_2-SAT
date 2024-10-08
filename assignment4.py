
from collections import defaultdict

neg = '~'


'''
Steps of Code:
1) Read data and store in circuit Class
        ex.
           Switches    | ['0', '1', '2', '3']
           Lights      | [[], [], [], [], [], []]
           state       | ['1', '0', '1', '1', '1', '0']
           Connections |[[1, 2, 3], [1, 4, 6], [3, 5, 6], [2, 4, 5]]

2) Create Clauses
        2a) First determine if each element in the Lights Array is on or off
            If off fill said element with [["P","Q"], ["~P","~Q"]]   This is NXOR
            else   fill said element with [["~P","Q"], ["P","~Q"]]   This is XOR
        2b) Loop through Connections and replace the corresponding P and Qs with the corresponding 
            switch 
                i.e. [["P","Q"], ["~P","~Q"]] -> [["0","Q"], ["~0","~Q"]]

3) Add these clauses to a forumla object

4) Run SAT solver 

'''
def can_turn_off_lights(input_file_path, output_file_path):
    

    Circuits = get_circuits(input_file_path)

   


    Circuits[0].create_clauses()
    Circuits[1].create_clauses()

    



    formula1 = two_cnf()
    formula2 = two_cnf()

    for l in Circuits[0].get_lights():
        formula1.add_clause(l[0])
        formula1.add_clause(l[1])
            
    f1_answer = two_sat_solver(formula1)

    for l in Circuits[1].get_lights():
        formula2.add_clause(l[0])
        formula2.add_clause(l[1])

    f2_answer = two_sat_solver(formula2)

    output = open(output_file_path, "w")
    output.write(f1_answer + "\n" + f2_answer + "\n")
    output.close()

 







'''
------------------------------------------------------------------------------------------------------------------------
End of algorithm
------------------------------------------------------------------------------------------------------------------------
'''


'''
------------------------------------------------------------------------------------------------------------------------
Helper Methods
------------------------------------------------------------------------------------------------------------------------
'''

'''
Description: Function reads input converts it to integer and create class representation
Parameters: File to parse
Return:  Returns array of circuit classses
'''
def get_circuits(input_file_path):
    """
    CIRCUIT 0
    """

    # INPUT
    input_file = open(input_file_path, "r")
    connections = []
    
    # First line
    input_file.readline()
    temp = input_file.readline().rstrip('\n').split(',')
    switches = int(temp[0]) 
    lights = int(temp[1])

    # Second Line
    state = input_file.readline().rstrip('\n').split(',')

    # Third Line
    for i in range(switches):

        connection = input_file.readline().rstrip('\n').split(',')
        for j in range(len(connection)):
            connection[j] = int(connection[j])
        connections.append(connection)
    
    # Create Circuit from inputs
    Circuit1 = circuit(switches, lights, state, connections)




    """
    CIRCUIT 1
    """

    #INPUT 
    connections = []

    # First Line
    input_file.readline()
    temp = input_file.readline().rstrip('\n').split(',')
    switches = int(temp[0])
    lights = int(temp[1])

    # Second Line
    state = input_file.readline().rstrip('\n').split(',')

    # Third Line
    for i in range(switches):
        connection = input_file.readline().rstrip('\n').split(',')
        for j in range(len(connection)):
            connection[j] = int(connection[j])
        connections.append(connection)
    Circuit2 = circuit(switches, lights, state, connections)

    input_file.close()
    return Circuit1, Circuit2



'''
------------------------------------------------------------------------------------------------------------------------
Classes
------------------------------------------------------------------------------------------------------------------------
'''

'''
Class used to represent data 
'''
class circuit():
    def __init__(self, switches, lights, state, connections):
        self.switches = list(str(i) for i in range(switches))
        self.lights = list([] for _ in range(lights))
        self.state = state
        self.connections = connections



    """
    Getter methods for corresponding variables
    """
    def get_lights(self):
        return self.lights
    
    def get_state(self):
        return self.state
    
    def get_switches(self):
        return self.switches
    
    def get_connections(self):
        return self.connections
    


    """
    Fills lights with empty clauses
    Returns: NULL
    """
    def fill_lights(self):
        for i in range(len(self.state)):
            if(self.state[i] == ('1')):
                self.lights[i] = [["P","Q"], ["~P","~Q"]]
            else:
                self.lights[i] = [["~P","Q"], ["P","~Q"]]
    

    """
    Replaces clauses with corresponding switch
    Returns: NULL
    """
    def create_clauses(self):
        self.fill_lights()
        for i in range(len(self.connections)):
            for j in range(len(self.connections[i])):
                light = self.lights[self.connections[i][j]-1]

                if light[0][0] == "P" or light[0][0] == "~P":   
                    light[0][0] = light[0][0].replace('P', self.switches[i])
                    light[1][0] = light[1][0].replace('P', self.switches[i])
                    
                else:
                    light[0][1] = light[0][1].replace('Q', self.switches[i])
                    light[1][1] = light[1][1].replace('Q', self.switches[i])

    """
    Displays circuit data
    """  
    def __str__(self):
        return f"Switches    | {self.switches}\nLights      | {self.lights}\nstate       | {self.state}\nConnections |{self.connections}"





'''
------------------------------------------------------------------------------------------------------------------------
SAT SOLVER
------------------------------------------------------------------------------------------------------------------------
'''
            



# directed graph class
#  adapted from:
#  src: https://www.geeksforgeeks.org/generate-graph-using-dictionary-python/
class dir_graph:
    def __init__(self):
        # create an empty directed graph, represented by a dictionary
        #  The dictionary consists of keys and corresponding lists
        #  Key = node u , List = nodes, v, such that (u,v) is an edge
        self.graph = defaultdict(set)
        self.nodes = set()

    # Function that adds an edge (u,v) to the graph
    #  It finds the dictionary entry for node u and appends node v to its list
    # performance: O(1)
    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.nodes.add(u)
        self.nodes.add(v)

    # Function that outputs the edges of all nodes in the graph
    #  prints all (u,v) in the set of edges of the graoh
    # performance: O(m+n) m = #edges , n = #nodes
    def print(self):
        edges = []
        # for each node in graph
        for node in self.graph:
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                # if edge exists then append
                edges.append((node, neighbour))
        return edges


# 2-CNF class
#  Class storing a boolean formula in Conjunctive Normal Form of literals
#  where the size of clauses is at most 2
#  -NOTATION-
#    The CNF is represented as a list of lists
#    e.g [[x, y], [k, z]] == (x or y) and (k or z)
#    i.e Conjunction of inner lists , where the inner lists are disjunctions
#    of literals
#    Negation is represented with ~ .  ~x == negation of literal x
# class two_cnf:
class two_cnf:
    def __init__(self):
        self.con = []

    # adds a clause to the CNF
    # performance O(1)
    def add_clause(self, clause):
        if len(clause) <= 2:
            self.con.append(clause)
        else:
            print("error: clause contains > 2 literals")

    # returns a set of all the variables in the CNF formula
    def get_variables(self):
        vars = set()
        for clause in self.con:
            for literal in clause:
                vars.add(literal)
        return vars
    
    def print(self):
        print(self.con)

    def __str__(self):
        return f"{self.con}"


# helper function that applies the double negation rule to a formula
#   the function removes all occurrences ~~ from the formula
def double_neg(formula):
    return formula.replace((neg+neg), '')


# Function that performs Depth First Search on a directed graph
# O(|V|+|E|)
def DFS(dir_graph, visited, stack, scc):
    for node in dir_graph.nodes:
        if node not in visited:
            explore(dir_graph, visited, node, stack, scc)


# DFS helper function that 'explores' as far as possible from a node
def explore(dir_graph, visited, node, stack, scc):
    if node not in visited:
        visited.append(node)
        for neighbour in dir_graph.graph[node]:
            explore(dir_graph, visited, neighbour, stack, scc)
        stack.append(node)
        scc.append(node)
    return visited


# Function that generates the transpose of a given directed graph
# Performance O(|V|+|E|)
def transpose_graph(d_graph):
    t_graph = dir_graph()
    # for each node in graph
    for node in d_graph.graph:
        # for each neighbour node of a single node
        for neighbour in d_graph.graph[node]:
            t_graph.addEdge(neighbour, node)
    return t_graph


# Function that finds all the strongly connected components in a given graph
# Implementation of Kosaraju’s algorithm
# Performance O(|V|+|E|) for a directed graph G=(V,E)
# IN : directed graph, G
# OUT: list of lists containing the strongly connected components of G
def strongly_connected_components(dir_graph):
    stack = []
    sccs = []
    DFS(dir_graph, [], stack, [])
    t_g = transpose_graph(dir_graph)
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            scc = []
            scc.append(node)
            explore(t_g, visited, node, [], scc)
            sccs.append(scc)
    return sccs


# Function that finds a contradiction in a list of strong connected components
# if [a , b , ~a,  c, a] is a connected component then the function returns T
# since a -> ~a -> a exists
# sccs = Strongly Connected Components
#   It is a list of lists representing the connected components
def find_contradiction(sccs):
    for component in sccs:
        for literal in component:
            for other_literal in component[component.index(literal):]:
                if other_literal == double_neg(neg + literal):
                    return True
    return False


# Function that determines if a given 2-CNF is Satisfiable or not
def two_sat_solver(two_cnf_formula):
    #print("Checking if the following 2-CNF is Satisfiable in linear time ")
    #two_cnf_formula.print()
    # setup the edges of the graph
    # G = (V,E) , V = L U ~L where L = set of variables in 2-CNF
    # E =
    # {(~u,v),(~v,u) | for all clauses [u,v] } U {(~u,u) | for all clauses [u]}
    graph = dir_graph()
    for clause in two_cnf_formula.con:
        if len(clause) == 2:
            u = clause[0]
            v = clause[1]
            graph.addEdge(double_neg(neg+u), v)
            graph.addEdge(double_neg(neg+v), u)
        else:
            graph.addEdge(double_neg(neg+clause[0]), clause[0])
    if not find_contradiction(strongly_connected_components(graph)):
        return("yes")
    else:
        return("no")



    