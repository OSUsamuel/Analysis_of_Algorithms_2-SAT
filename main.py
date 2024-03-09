
from assignment4 import can_turn_off_lights

def main():
    """ Main program """

    # test medium
    for i in range(2):
        curr = f"test_medium_{i}.txt"
        print(curr)
        print("actual:")
        can_turn_off_lights(f"testfiles/samples_subset/test_medium_{i}.txt", "some")

        expectedoutputfile = f"testfiles/samples_subset/test_medium_answer_{i}.txt"
        with open(expectedoutputfile, 'r') as file:
            expectedoutput1 = file.readline()
            expectedoutput2 = file.readline()
        print("")
        print("expected output:")
        print(expectedoutput1)
        print(expectedoutput2)

    # test small
    for i in range(3):
        curr = f"test_small_{i}.txt"
        print(curr)
        print("actual:")
        can_turn_off_lights(f"testfiles/samples_subset/test_small_{i}.txt", "some")

        expectedoutputfile = f"testfiles/samples_subset/test_small_answer_{i}.txt"
        with open(expectedoutputfile, 'r') as file:
            expectedoutput1 = file.readline()
            expectedoutput2 = file.readline()
        print("")
        print("expected output:")
        print(expectedoutput1)
        print(expectedoutput2)




    return 0

if __name__ == "__main__":
    main()