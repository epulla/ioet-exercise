# Exercise IOET
# By Erick Pulla
# Made using python3

import sys

def main(argv):
    """Main function of the program
    """
    
    if len(argv) != 2:
        print("Usage:\n(Windows) python main.py <inputfile>\n(Linux/Mac) python3 main.py <inputfile>")
        sys.exit()
    
    from util import Schedule, get_unique_pairs

    schedules = []
    with open(argv[1], "r") as f:
        for line in f:
            name, data = line.strip().split("=")
            schedules.append(Schedule(name, data))

    unique_pairs = get_unique_pairs(schedules)

    for schedule1, schedule2 in unique_pairs:
        coincidences = schedule1.compare(schedule2)
        if coincidences > 0:
            print("%s-%s: %d"%(schedule1.owner, schedule2.owner, coincidences))

if __name__ == "__main__":
    main(sys.argv)