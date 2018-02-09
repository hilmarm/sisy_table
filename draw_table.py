import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


class DrawTable(object):

    def __init__(self, parsed_program, variables):
        self.A = [a.time for a in parsed_program.artists]
        self.pp = parsed_program
        self.vars = variables
        self.min = 1000
        self.max = 0
        for a in self.A:
            self.min = min(a) if min(a) < self.min else self.min
            self.max = max(a) if max(a) > self.max else self.max
        print(self.min)
        print(self.max)

    def draw_table(self):
        # Fixing random state for reproducibility

        
        # plt.axis([0,4, 0,10])
        # ax = plt.gca()
        # ax.set_autoscale_on(False)
        fig = plt.figure(figsize=(25,5))
        ax = fig.add_subplot(111)
        pts = []
        for i in range(len(self.A)):
            dj = self.pp.artists[i].name_utf
            time = self.pp.artists[i].sisy_time
            # Set DJ time slot boxes
            x = self.A[i][0]
            y = self.vars[i]
            w = self.A[i][1]-self.A[i][0]
            h = 1
            # Generate random color
            r = lambda: random.randint(0,255)
            color = '#%02X%02X%02X' % (r(),r(),r())

            pts.append(
                patches.Rectangle(
                    (x,y),
                    w,
                    h,
                    fill=True,
                    facecolor=color,
                    edgecolor='blue',
                    alpha=0.3
                )
            )
            centerx = x + w/6.0
            centery = y + 2.0/3.0 # obviously use a different formula for different shapes
            plt.text(centerx, centery, dj, fontsize=7)
            plt.text(centerx, centery - 0.5, time, fontsize=7)
            print("A = ({},{})".format(self.A[i][0], self.A[i][1]))
            print("self.vars[i] = {}".format(self.vars[i]))
            # patches.Rectangle(
            #     (0.26, 0.1), 0.2, 0.6,
            #     facecolor="none"     # No background
            # ),
            # patches.Rectangle(
            #     (0.49, 0.1), 0.2, 0.6,
            #     facecolor="red"
            # ),
            # patches.Rectangle(
            #     (0.72, 0.1), 0.2, 0.6,
            #     facecolor="#00ffff"
            # )
        for p in pts:
            print(p)
            ax.add_patch(p)
        plt.axis([self.min, self.max, 0,6])
        ax.set_autoscale_on(False)
        plt.tight_layout(True)
        #plt.savefig('exported/foo.png', bbox_inches='tight')
        plt.title('Sisyphos timetable', bbox={'facecolor': '0.8', 'pad': 5})
        plt.show()
        pass

        def name_in_table(self):
            pass
