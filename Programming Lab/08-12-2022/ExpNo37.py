class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def __add__(self, other):
        hour = self.hour + other.hour
        minute = self.minute + other.minute
        second = self.second + other.second

        if second >= 60:
            second -= 60
            minute += 1

        if minute >= 60:
            minute -= 60
            hour += 1

        return Time(hour, minute, second)


time1 = Time(1, 20, 30)
time2 = Time(2, 45, 15)

print(time1 + time2)