# File for utils (functions or classes) to solve the exercise
# Made by Erick Pulla

# Use of built-in library (not external)
from datetime import datetime as dt

DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]

class DateRange:
    def __init__(self, start_time: str, end_time: str):
        self.start_time = dt.strptime(start_time.strip(), "%H:%M")
        self.end_time = dt.strptime(end_time.strip(), "%H:%M")

    def is_overlapped_with(self, other: 'DateRange') -> bool:
        return self.start_time <= other.end_time and self.end_time >= other.start_time

    def __repr__(self) -> str:
        return 'DateRange(start_time=%s, end_time=%s)'%(dt.strftime(self.start_time, "%H:%M"), dt.strftime(self.end_time, "%H:%M"))

class Schedule:
    def __init__(self, owner: str, data_days: str):
        self.owner = owner
        self.schedule = self.format_days_to_dict(data_days)

    def format_days_to_dict(self, data_days: str) -> dict:
        dicc = {}
        for day in data_days.split(","):
            start_time, end_time = day[2:].split("-")
            dicc[day[:2]] = DateRange(start_time, end_time)
        return dicc

    def compare(self, other: 'Schedule') -> int:
        coincidences = 0
        for day in DAYS:
            try:
                if self.schedule[day].is_overlapped_with(other.schedule[day]):
                    coincidences += 1
            except KeyError:
                pass
        return coincidences

    def __repr__(self) -> str:
        return "Schedule(owner=%s)"%(self.owner)

def get_unique_pairs(elements: list) -> list:
    l = []
    for i, elem1 in enumerate(elements):
        for elem2 in elements[i + 1:]:
            l.append((elem1, elem2))
    return l
