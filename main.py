
from assignment4 import can_turn_off_lights
from time import *


def main():
    """ Main program """

    for i in range(1,4):
        curr = f"test{i}.txt"
        print(curr)
        start_time = time()
        can_turn_off_lights(f"testfiles/test{i}.txt", f"testfiles/test{i}_actual_output.txt")
        print("")
        print("Ran in " + str(time() - start_time))
        actualoutputfile = f"testfiles/test{i}_actual_output.txt"
        with open(actualoutputfile, 'r') as file:
            actualoutput1 = file.readline()
            actualoutput2 = file.readline()
        print("actual output:")
        print(actualoutput1.strip())
        print(actualoutput2.strip())     
        expectedoutputfile = f"testfiles/test{i}_result.txt"
        with open(expectedoutputfile, 'r') as file:
            expectedoutput1 = file.readline()
            expectedoutput2 = file.readline()
        print("expected output:")
        print(expectedoutput1.strip())
        print(expectedoutput2.strip())
        print("")


    # test medium
    for i in range(2):
        curr = f"test_medium_{i}.txt"
        print(curr)
        start_time = time()
        can_turn_off_lights(f"testfiles/samples_subset/test_medium_{i}.txt", f"testfiles/samples_subset/test_medium_{i}_actual_output.txt")
        print("")
        print("Ran in " + str(time() - start_time))
        actualoutputfile = f"testfiles/samples_subset/test_medium_{i}_actual_output.txt"
        with open(actualoutputfile, 'r') as file:
            actualoutput1 = file.readline()
            actualoutput2 = file.readline()
        print("actual output:")
        print(actualoutput1.strip())
        print(actualoutput2.strip())     
        expectedoutputfile = f"testfiles/samples_subset/test_medium_answer_{i}.txt"
        with open(expectedoutputfile, 'r') as file:
            expectedoutput1 = file.readline()
            expectedoutput2 = file.readline()
        print("expected output:")
        print(expectedoutput1.strip())
        print(expectedoutput2.strip())
        print("")


    # test small
    for i in range(3):
        curr = f"test_small_{i}.txt"
        print(curr)
        start_time = time()
        can_turn_off_lights(f"testfiles/samples_subset/test_small_{i}.txt", f"testfiles/samples_subset/test_small_{i}_actual_output.txt")
        print("")
        print("Ran in " + str(time() - start_time))
        actualoutputfile = f"testfiles/samples_subset/test_small_{i}_actual_output.txt"
        with open(actualoutputfile, 'r') as file:
            actualoutput1 = file.readline()
            actualoutput2 = file.readline()
        print("actual output:")
        print(actualoutput1.strip())
        print(actualoutput2.strip())
        expectedoutputfile = f"testfiles/samples_subset/test_small_answer_{i}.txt"
        with open(expectedoutputfile, 'r') as file:
            expectedoutput1 = file.readline()
            expectedoutput2 = file.readline()
        print("expected output:")
        print(expectedoutput1.strip())
        print(expectedoutput2.strip())
        print("")


    return 0

if __name__ == "__main__":
    main()