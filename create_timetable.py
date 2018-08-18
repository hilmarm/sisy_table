import shutil


day_time = {'DO':0, 'FR':24, 'SA':48, 'SO':72, 'MO':96, 'DI':120, 'MI':144}
day_t = [[0,24], [24,48], [48,72], [72,96], [96,120], [120,144], [144,168]]
days = ['thursday', 'friday', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday']
stages = ['Wintergarten', 'Hammerhalle', 'Dampfer', 'Draussen', 'backup']
stage_classes = ['meltstage', 'meltselektor', 'bigwheel', 'superdrysounds', 'foreststage']
stage_colors = ['e8412c', '2a3286', '0bbcd', '000000', '002244']
stage_images = ['Melt_Stage.png', 'Meltselektor_C.png', 'Big_Wheel_C.png', 'Superdrysounds_C.png', 'House_of_presents_C.png']
stage_info = [{'name': stages[i], 'css_class': stage_classes[i], 'color': stage_colors[i], 'image': stage_images[i]} for i in range(len(stages))]

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
        day_code = ''

        
        for stage_n in [0,1,2]:
            a = ''
            stage = stages[stage_n]
            for i in range(len(self.A)):
                # "floor{};".format(stages[stage_n])
                times = self.plays_today(day, self.A[i])
                # If today and plays on right stage
                if times and int(self.vars[i])==stage_n:
                    dj = self.pp.artists[i].name_utf
                    time = self.pp.artists[i].sisy_time
                    y = int(self.vars[i])
                    start = times[0]
                    end = times[1]

                    
                    pts = []
                    b = [day, dj, stage, start, end, stage, stage_n]
                    #print(b)
                    #print(self.create_dj_string(dj, start, end))
                    a += self.create_dj_string(dj, start, end)

            if a != '':
                # print('There are djs playing on stage {} on day {}'.format(stage, day))
                pre_floor_string = self.pre_floor_string(stage_info[stage_n]['css_class'], stage_info[stage_n]['name'], stage_info[stage_n]['color'], stage_info[stage_n]['image'])
                post_floor_string = self.post_floor_string()
                b = pre_floor_string + '\n' + a + '\n' + post_floor_string
                day_code += b

        self.export_day_html(day, day_code)

    def plays_today(self, day, time_slot):
        # Check if time slot is within given day, if yes return playing times
        if time_slot[1] > day_t[day][0] and time_slot[0] < day_t[day][1]:
            end = min(time_slot[1], day_t[day][1])%24
            start = max(time_slot[0], day_t[day][0])%24

            # Corner case if show ends at 0 or 24. 
            return [start, end if end!=0 else 24]
        else:
            return False

    def add_newline(self, string):
        string += '\n'
        return string

    def create_dj_string(self, dj, start, end, bg_color='f49855', addon=''):
        print(start)
        print(end)
        print(dj)
        [start, end] = self.time_to_pixels(start, end)
        template = '<li style="top: {start}px; height: {end}px;"> <a class="runningorder-event" style="background-color:#{bg_color};"> <h3>{dj}</h3> <div class="title-addon">{addon}</div> </a></li>'.format(start=start, end=end, bg_color=bg_color, dj=dj, addon=addon)
        return template
    
    def time_to_pixels(self, start, end):
        return [start*80, (end-start)*80 + 4]

    def pre_floor_string(self, stage_class, floor, floor_color, floor_image='image.png'):
        return '<div class="runningorder-column runningorder-column-{}"> <header class="runningorder-column-header"> <img src="./files/{}" alt="" class="column-icon"> <h2 class="column-name" style="background-color: #{};"> <span>{}</span> </h2> </header> <section class="runningorder-column-events"> <ul>'.format(stage_class, floor_image, floor_color, floor)

    def post_floor_string(self):
        return '</ul></section></div>'


    def post_day_string(self):
        bottom_msg = 'To see how this timetable was generated please visit <a href="https://www.github.com/hilmarm/sisy_table">github.com/hilmarm/sisy_table</a>. The layout was taken from the running order of <a href="https://meltfestival.de/en/runningorder/">Melt Festival</a> which is powered by <a href="http://piklist.com/">Piklist</a>.'
        return '</article> </div> {} </body> </html>'.format(bottom_msg)


    def export_day_html(self, day, day_code):
        print('on day {}'.format(days[day]))
        # (day_code)

        outfilename = 'webpage/{}.html'.format(days[day])
        with open(outfilename, 'wb') as outfile:

            template_file = 'web_page_template/{}pre'.format(day)

            with open(template_file, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)
        
            outfile.write(day_code)
            outfile.write(self.post_day_string())

    def hey(self, template_file):
        
            for filename in glob.glob('*.txt'):
                if filename == outfilename:
                    # don't want to copy the output into the output
                    continue
                with open(filename, 'rb') as readfile:
                    shutil.copyfileobj(readfile, outfile)