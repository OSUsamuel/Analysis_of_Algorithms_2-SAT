
from assignment4 import can_turn_off_lights

def main():
    """ Main program """

    for i in range(1,4):
        can_turn_off_lights(f"testfiles\\samples_subset\\test_{i}.txt", f"testfiles\\answers\\test_{i}.txt")

        correct_answers = open(f"testfiles\\samples_subset\\test_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_{i}.txt", "r")
        print(f"test_{i}")
        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")
        

    for i in range(3):
        can_turn_off_lights(f"testfiles\\samples_subset\\test_small_{i}.txt", f"testfiles\\answers\\test_small_{i}.txt")

        correct_answers = open(f"testfiles\\samples_subset\\test_small_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_small_{i}.txt", "r")
        print(f"test_small_{i}")
        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")


    for i in range(2):
        can_turn_off_lights(f"testfiles\\samples_subset\\test_medium_{i}.txt", f"testfiles\\answers\\test_medium_{i}.txt")

        correct_answers = open(f"testfiles\\samples_subset\\test_medium_answer_{i}.txt", "r")
        answers = open(f"testfiles\\answers\\test_medium_{i}.txt", "r")
        print(f"test_medium_{i}")
        for i in range(2):
            print("output line matches exactly: ", correct_answers.readline() == answers.readline())
        print("")

 
    return 0






if __name__ == "__main__":
    main()