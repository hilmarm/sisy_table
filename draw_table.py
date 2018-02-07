import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random


class DrawTable(object):

    def __init__(self, A, variables):
        self.A = A
        self.vars = variables

    def draw_table(self):
        # Fixing random state for reproducibility

        
        # plt.axis([0,4, 0,10])
        # ax = plt.gca()
        # ax.set_autoscale_on(False)
        fig = plt.figure(figsize=(8,3))
        ax = fig.add_subplot(111, aspect='equal')
        pts = []
        for i in range(len(self.A)):
            dj = 'dj'
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
                    alpha=0.2
                )
            )
            centerx = x + w/2.0
            centery = y + 1.0/3.0 # obviously use a different formula for different shapes
            plt.text(centerx, centery, dj)
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
        plt.axis([0,25, 0,6])
        ax.set_autoscale_on(True)
        plt.show()
        pass
