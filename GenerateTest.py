import math
import re
import sys
import random
"""
Use from terminal with following command:
    python3 GenerateTest.py n_number_of_switches m_number_of_lights
"""

def make_bigger_input_file(number_of_lights, number_of_switches):
    output_file_path = "testfiles\\samples_subset\\test_bigger.txt"
    int_lights = int(number_of_lights)
    int_switches = int(number_of_switches)

    lineasterix = "***"

    line1txt = ""
    line1txt = line1txt+number_of_switches+","+number_of_lights
    # print(line1txt)

    line2list = [-1]*int_lights
    for i in range(int_lights):
        line2list[i] = random.randint(0, 1)
    line2txt = ""
    for i in range(int_lights-1):
        line2txt = line2txt+str(line2list[i])+","
    line2txt = line2txt+str(line2list[int_lights-1])
    # print(line2txt)

    line3array = [-1]*int_switches
    switches_without_lights = [i for i in range(int_switches)]
    unassigned_light_index_values = [i for i in range(1, int_lights+1)]
    # print(switches_without_lights)
    # print(unassigned_light_index_values)

    for i in range(int_lights):
        random_light_index = unassigned_light_index_values[random.randint(0, len(unassigned_light_index_values)-1)]
        unassigned_light_index_values.remove(random_light_index)
        # print(random_light_index)

        if len(switches_without_lights)>0:
            random_switch_index1 = switches_without_lights[random.randint(0, len(switches_without_lights)-1)]
            switches_without_lights.remove(random_switch_index1)

        else:
            random_switch_index1 = random.randint(0, int_switches-1)

        if line3array[random_switch_index1] == -1:
            line3array[random_switch_index1]= [random_light_index]
        else:
            line3array[random_switch_index1].insert(len(line3array[random_switch_index1]),random_light_index)
        
        random_switch_index2 = random_switch_index1
        while (random_switch_index2 == random_switch_index1):
            random_switch_index2 = random.randint(0, int_switches-1)

        if line3array[random_switch_index2] == -1:
            line3array[random_switch_index2]= [random_light_index]
            # print("FIRST: ",line3array)
        else:
            # print("len: ", len(line3array[random_switch_index2]))
            # print("idx2 in list: ", line3array[random_switch_index2])
            line3array[random_switch_index2].insert(len(line3array[random_switch_index2]),random_light_index)
            # print(line3array)

        # print("light ", random_light_index)
        # print("   idx1: ", random_switch_index1)
        # print("   idx2: ", random_switch_index2)
            

                
                



    with open(output_file_path, 'w') as output_file:
        output_file.write(f"{lineasterix}\n")
        output_file.write(f"{line1txt}\n")
        output_file.write(f"{line2txt}\n")
        print(line3array)
        for i in range(int_switches):
            line3_list = line3array[i]
            line3txt = str(line3_list[0])
            if isinstance(line3_list, int):
                line3array[i] = line3txt
            else:
                for j in range(1, len(line3_list)):
                    line3txt = line3txt + ","+ str(line3_list[j])
            line3array[i] = line3txt
        print(line3array)
        for i in range(int_switches):
            output_file.write(f"{line3array[i]}\n")
        output_file.write(f"{lineasterix}\n")
        output_file.write(f"{line1txt}\n")
        output_file.write(f"{line2txt}\n")
        for i in range(int_switches):
            output_file.write(f"{line3array[i]}\n")
    
    return

if len(sys.argv) != 4:
    print("Usage: python script.py n_number_of_switches m_number_of_lights)")
else:
    output_file_path = sys.argv[1]
    n_number_of_switches = sys.argv[2]
    m_number_of_lights = sys.argv[3]
    if int(n_number_of_switches)>int(m_number_of_lights):
        print("Usage: number_of_switches must be less than or equal to number_of_lights)")
    else:
        make_bigger_input_file(m_number_of_lights, n_number_of_switches)