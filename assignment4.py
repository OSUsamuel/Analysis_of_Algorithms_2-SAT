
'''
This file contains the template for Assignment1. For testing it, I will place
it
in a different directory, call the function <number_of_allowable_intervals>,
and check
its output. So, you can add/remove whatever you want to/from this file. But,
don't
change the name of the file or the name/signature of the following function.
Also, I will use <python3> to run this code.
'''
def can_turn_off_lights(input_file_path, output_file_path):
    

    Circuits = get_circuits(input_file_path)





    







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
    input_file = open(input_file_path, "r")
    connections = []
    input_file.readline()
    temp = input_file.readline()
    switches = int(temp[0])
    lights = int(temp[2])
    state = input_file.readline()
    for i in range(switches):

        connection = input_file.readline().rstrip('\n').split(',')
        for j in range(len(connection)):
            connection[j] = int(connection[j])
        connections.append(connection)
    Circuit1 = circuit(switches, lights, state, connections)

    connections = []
    input_file.readline()
    temp = input_file.readline()
    switches = int(temp[0])
    lights = int(temp[2])
    state = input_file.readline()
    for i in range(switches):

        connection = input_file.readline().rstrip('\n').split(',')
        for j in range(len(connection)):
            connection[j] = int(connection[j])
        connections.append(connection)
    Circuit2 = circuit(switches, lights, state, connections)

    return Circuit1, Circuit2



'''
------------------------------------------------------------------------------------------------------------------------
Classes
------------------------------------------------------------------------------------------------------------------------
'''
class circuit():
    def __init__(self, switches, lights, state, connections):
        self.switches = switches
        self.lights = lights
        self.state = state
        self.connections = connections
        
    def __str__(self):
        return f"Switches    | {self.switches}\nLights      | {self.lights}\nstate       | {self.state}Connections |{self.connections}"

        
    
            


    

