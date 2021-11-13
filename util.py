# File for utils (functions or classes) to solve the exercise
# Made by Erick Pulla

# Use of built-in library (not external)
from datetime import datetime as dt

class DateRange:
    """
    A class used to represent a range between dates

    Attributes
    ----------
    start_time : str
        The start date of the range
    end_time : str
        The end date of the range
    date_format : str, optional
        The datetime format to convert string to datetime (default is '%H:%M')

    Methods
    ----------
    is_overlapped_with(other: DateRange) -> bool
        Returns boolean if this start_time and end_time are overlapped with other's
    """

    def __init__(self, start_time: str, end_time: str, date_format: str="%H:%M"):
        """
        Parameters
        ----------
        start_time : str
            The start date of the range
        end_time : str
            The end date of the range
        date_format : str
            The datetime format to convert string to datetime (default is '%H:%M')
        """

        self.start_time = dt.strptime(start_time.strip(), date_format)
        self.end_time = dt.strptime(end_time.strip(), date_format)

    def is_overlapped_with(self, other: 'DateRange') -> bool:
        """Returns boolean if this start_time and end_time are overlapped with other's
        
        Parameters
        ----------
        other : DateRange
            A DateRange object to compare with its start time and end time   
        
        Returns
        -------
        bool
            A boolean value checking if this start_time and end_time are overlapped with other's
        """
        return other is not None and self.start_time <= other.end_time and self.end_time >= other.start_time

    def __repr__(self) -> str:
        """
        Returns
        -------
        str
            A string representation of this object and its attributes
        """
        return 'DateRange(start_time=%s, end_time=%s)'%(dt.strftime(self.start_time, "%H:%M"), dt.strftime(self.end_time, "%H:%M"))

class Schedule:
    """
    A class used to represent a week schedule of a person

    Attributes
    ----------
    owner : str
        The name of the schedule owner
    schedule : dict
        A dictionary of the days (string name as keys) with its date range (DateRange as values)
    
    Methods
    -------
    format_days_to_dict(data_days: str) -> dict
        Creates a dictionary from a string, using the day code (MO, TU, WE, etc) as keys, and a DateRange object as values
    compare(other: Schedule) -> int
        Compare the days of this dictionary with the other's
    """

    def __init__(self, owner: str, data_days: str):
        """
        Parameters
        ----------
        owner : str
            The name of the schedule owner
        schedule : dict
            A dictionary of the days (string name as keys) with its date range (DateRange as values)
        """
        
        self.owner = owner
        self.schedule = self.format_days_to_dict(data_days)

    def format_days_to_dict(self, data_days: str) -> dict:
        """Creates a dictionary from a string, using the day code (MO, TU, WE, etc) as keys, and a DateRange object as values
        
        Parameters
        ----------
        data_days : str
            A formatted string of the schedule of a person ([day_code][start_time]:[end_time], e.g. MO10:00-12:00)
        
        Returns
        -------
        dict
            A dictionary using the day code (MO, TU, WE, etc) as keys, and a DateRange object as values
        """
        
        dicc = {}
        for day in data_days.split(","):
            start_time, end_time = day[2:].split("-")
            dicc[day[:2]] = DateRange(start_time, end_time)
        return dicc

    def compare(self, other: 'Schedule') -> int:
        """Compare the days of this dictionary with the other's
        
        Parameters
        ----------
        other : Schedule
            A Schedule object to compare with its schedule
        
        Returns
        -------
        dict
            The number of coincidences between this object's schedule and other's
        
        Raises
        ------
        TypeError
            If the other Schedule to compare with is None
        """
        if other is None:
            raise TypeError("Param 'other' can't be None type")
        coincidences = 0
        for day in list(self.schedule.keys()):
            try:
                if self.schedule[day].is_overlapped_with(other.schedule[day]):
                    coincidences += 1
            except KeyError:
                pass
        return coincidences

    def __repr__(self) -> str:
        """
        Returns
        -------
        str
            A string representation of this object and its owner
        """
        return "Schedule(owner=%s)"%(self.owner)

def get_unique_pairs(elements: list) -> list:
    """Generates a list of combinations of pairs (without repeated and inverted pairs) of a list of unique elements
    
    Parameters
    ----------
    elements : list
        List of unique elements of any type or class

    Returns
    -------
    list
        A list of combinations of unique pairs
    """
    
    l = []
    for i, elem1 in enumerate(elements):
        for elem2 in elements[i + 1:]:
            l.append((elem1, elem2))
    return l
