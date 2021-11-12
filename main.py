# Exercise IOET
# By Erick Pulla
# Made using python3

from util import Schedule, get_unique_pairs

schedules = []
with open("data.txt", "r") as f:
    for line in f:
        name, data = line.strip().split("=")
        schedules.append(Schedule(name, data))

unique_pairs = get_unique_pairs(schedules)

for schedule1, schedule2 in unique_pairs:
    coincidences = schedule1.compare(schedule2)
    if coincidences > 0:
        print("%s-%s: %d"%(schedule1.owner, schedule2.owner, coincidences))
        
