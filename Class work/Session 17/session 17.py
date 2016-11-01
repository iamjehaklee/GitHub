class Time:
    """
    Represents the time of day

    attributes: hour, minute, second 
    """
    def print_time(self):
        print('%.2d:%.2d:%.2d' %(self.hour, self.minute, self.second))


start = Time()
start.hour = 9
start.minute = 45
start.second = 0
start.print_time()