import numpy as np

day_time = {'DO':0, 'FR':24, 'SA':48, 'SO':72, 'MO':96, 'DI':120, 'MI':144}
day_t = [[0,24], [24,48], [48,72], [72,96], [96,120], [120,144], [144,168]]

class CreateTimetable(object):

    def __init__(self, parsed_program, variables):
        self.A = [a.time for a in parsed_program.artists]
        self.pp = parsed_program
        self.vars = variables
        self.min = 1000
        self.max = 0
        for a in self.A:
            self.min = min(a) if min(a) < self.min else self.min
            self.max = max(a) if max(a) > self.max else self.max
        self.days = []

        print(self.min)
        print(self.max)

    
    def draw_week(self):
        for day in [0,1,2,3,4,5,6]:
            self.draw_day(day)

    def draw_day(self, day):

        a = "var timetable{} = new Timetable();".format(day)
        a = self.add_newline(a)
        a += "timetable{}.setScope(0,23)".format(day)
        a = self.add_newline(a)
        a += "timetable{}.addLocations(['Wintergarten', 'Hammerhalle', 'Dampfer']);".format(day)
        a = self.add_newline(a)

        for i in range(len(self.A)):
            times = self.plays_today(day, self.A[i])
            if times:
                dj = self.pp.artists[i].name_utf
                time = self.pp.artists[i].sisy_time
                y = int(self.vars[i])
                start = times[0]
                end = times[1]
    
                if y == 0:
                    stage = 'Wintergarten'
                elif y == 1:
                    stage = 'Hammerhalle'
                elif y == 2:
                    stage = 'Dampfer'
                else:
                    print('y = {}'.format(y))
                    print('error')
                    
                pts = []
                a += "timetable{}.addEvent('{}', '{}', new Date(2015,7,17,{},00), new Date(2015,7,17,{},00), {{ url: '#' }});".format(day, dj, stage, int(end), int(start))
                a = self.add_newline(a)
        a += "var renderer{} = new Timetable.Renderer(timetable{});".format(day, day)
        a = self.add_newline(a)
        a += "renderer{}.draw('.timetable');".format(day)
        a = self.add_newline(a)

        path = 'js_webpage/timetables/timetable_{}.js'.format(day)
        file = open(path, 'w')
        file.write(a)

    def plays_today(self, day, time_slot):
        # Check if time slot is within given day, if yes return playing times
        if time_slot[1] > day_t[day][0] and time_slot[0] < day_t[day][1]:
            return [max(time_slot[1], day_t[day][0])%24, min(time_slot[0], day_t[day][1])%24]
        else:
            return False

    def add_newline(self, string):
        string += '\n'
        return string
