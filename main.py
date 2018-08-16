#!/usr/bin/env python

from table_solver import TableSolver
from draw_table import DrawTable
from create_timetable import CreateTimetable
from parse_programm import ParseProgramm as PP
import random

def main():
    # A = [[0,2], [1,3], [9,10], [4,8], [6,10], [2,6]]

    my_input = 'input/program2018'

    pp = PP(my_input)
    pp.run()

    A = []
    for artist in pp.artists:
    	A.append(artist.time)

    solver = TableSolver(A, 10)
    solver.SolveMIP()
    
    # drawer = DrawTable(pp, [x.solution_value() for x in solver.vars])
    # drawer.draw_table()

    drawer = CreateTimetable(pp, [x.solution_value() for x in solver.vars])
    for day in [0,1,2,3,4,5,6]:
        drawer.draw_day(day)

if __name__ == '__main__':
  main()
