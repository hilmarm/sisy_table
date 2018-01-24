import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class DrawTable(object):

    def __init__(self, A, variables):
        self.A = A
        self.vars = variables

    def draw_table(self):
        # Fixing random state for reproducibility

        
        # plt.axis([0,4, 0,10])
        # ax = plt.gca()
        # ax.set_autoscale_on(False)
        fig6 = plt.figure()
        ax6 = fig6.add_subplot(111, aspect='equal')
        pts = []
        for i in range(len(self.A)):
            pts.append(
                patches.Rectangle(
                    (0.1*self.A[i][0], 0.1*self.vars[i]), 0.1*(self.A[i][1]-self.A[i][0]), 0.1*(1), fill=True, facecolor='red' ,edgecolor='blue'
                )
            )
            print("A = ({},{})".format(0.1*self.A[i][0], 0.1*self.A[i][1]))
            print("self.vars[i] = {}".format(0.1*self.vars[i]))
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
            ax6.add_patch(p)
        plt.show()
        pass
