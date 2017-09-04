#!/usr/bin/env python3

week = ('M', 'T', 'W', 'Th', 'F', 'Sa', 'Su')

class Calculator(object):
    def __init__(self, start, end):
        self.sundays_on_first = 0
        self.start = start
        self.end = end

    def calc(self):
        i = 0
        for year in range(self.start[2], self.end[2] + 1):
            for month in range(1, 13):
                days = 31
                if month in [4, 6, 9, 11]:
                    days = 30
                elif month == 2:
                    if year % 4 == 0:
                        days = 29
                    else:
                        days = 28
                for day in range(1, days + 1):
                    dow = week[(i + 1) % 7]
                    if day == 1 and dow == 'Su':
                        self.sundays_on_first += 1
                        print('sof:', self.sundays_on_first)
                    print('{}/{}/{} was a {}'.format(
                        day, month, year, dow))
                    i += 1

        print('total days:', i)
        return self.sundays_on_first

if __name__ == '__main__':
    c = Calculator([1, 1, 1901], [31, 12, 2000])
    print('Sundays on first of month:', c.calc())
