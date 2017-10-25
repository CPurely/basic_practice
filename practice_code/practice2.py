import datetime
import operator

class Time():
    '''time object attribute: hour, minute, second
       time method : time_to_int'''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    #def __radd__(self, other):
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def int_to_time(self,seconds):
        self=Time()
        minute, self.second = divmod(seconds, 60)
        self.hour, self.minute = divmod(minute, 60)
        return self
def int_to_time(seconds):
    self=Time()
    minute, self.second = divmod(seconds, 60)
    self.hour, self.minute = divmod(minute, 60)
    return self


start = Time(9, 45)
duration=Time(10,20)
operator.__lt__(start,duration)






