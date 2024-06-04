class Timer:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            
            if self.__minutes == 59:
                self.__minutes = 0
                
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1

    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59

            if self.__minutes == 0:
                self.__minutes = 59
                
                if self.__hours == 0:
                    self.__hours = 23
                else:
                    self.__hours -= 1
            else:
                self.__minutes -= 1
        else:
            self.__seconds -= 1


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
