#!/usr/bin/env python

from table_solver import TableSolver
from draw_table import DrawTable
from parse_programm import ParseProgramm as PP
import random

def main():
    A = [[0,2], [1,3], [9,10], [4,8], [6,10], [2,6]]
    #A = [[4,9], [3,9], [1,4], [4,6], [4,7], [3,6]]
    #B = [[4,9], [3,6], [3,9], [1,4], [4,6], [4,7]]

    A = []

    N = 10
    for i in range(N):
    	mid = random.randint(1,20-2)
    	A.append([mid, mid+random.randint(1,6)])

    # solver = TableSolver(A, 10)
    # solver.SolveMIP()
    
    # drawer = DrawTable(A, [x.solution_value() for x in solver.vars])
    # drawer.draw_table()

    pp = PP()
    pp.read_table('input/programm_example')
    pp.print_table()
    pp.parse_timetable()
    pp.print_table()

if __name__ == '__main__':
  main()
