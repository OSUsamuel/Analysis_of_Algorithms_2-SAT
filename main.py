
from assignment4 import can_turn_off_lights

def main():
    """ Main program """

    for i in range(2):
        can_turn_off_lights(f"GA4\\testfiles\\samples_subset\\test_medium_{i}.txt", "some")
    return 0

if __name__ == "__main__":
    main()