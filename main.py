
from assignment4 import can_turn_off_lights
from time import *

def main():
    """ Main program """

    for i in range(1,4):
        print(f"test_{i}")
        start_time = time()
        can_turn_off_lights(f"testfiles\\samples_subset\\test_{i}.txt", f"testfiles\\answers\\test_{i}.txt")
        print("Ran in " + str(time() - start_time))
        correct_answers = open(f"testfiles\\samples_subset\\test_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_{i}.txt", "r")

        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")
        

    for i in range(3):
        print(f"test_small_{i}")
        start_time = time()
        can_turn_off_lights(f"testfiles\\samples_subset\\test_small_{i}.txt", f"testfiles\\answers\\test_small_{i}.txt")
        print("Ran in " + str(time() - start_time))
        correct_answers = open(f"testfiles\\samples_subset\\test_small_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_small_{i}.txt", "r")

        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")


    for i in range(2):
        print(f"test_medium_{i}")
        start_time = time()
        can_turn_off_lights(f"testfiles\\samples_subset\\test_medium_{i}.txt", f"testfiles\\answers\\test_medium_{i}.txt")
        print("Ran in " + str(time() - start_time))
        correct_answers = open(f"testfiles\\samples_subset\\test_medium_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_medium_{i}.txt", "r")
        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")

    print(f"test_bigger")
    start_time = time()
    can_turn_off_lights(f"testfiles\\samples_subset\\test_bigger.txt", f"testfiles\\answers\\test_medium_{i}.txt")
    print("Ran in " + str(time() - start_time))
    print("")

 
    return 0






if __name__ == "__main__":
    main()