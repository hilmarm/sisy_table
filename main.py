from table_solver import TableSolver
from draw_table import DrawTable

def main():
    A = [[0,2], [1,3], [2,6], [9,10], [4,8], [6,10]]
    solver = TableSolver(A, 10)
    solver.SolveMIP()

    drawer = DrawTable(A, [x.solution_value() for x in solver.vars])
    drawer.draw_table()


if __name__ == '__main__':
  main()
