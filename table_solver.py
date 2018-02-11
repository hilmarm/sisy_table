from __future__ import print_function
from ortools.linear_solver import pywraplp

class TableSolver(object):

    def __init__(self, segments, M):
        self.A = segments
        self.vars = []
        self.M = M
        self.solver = pywraplp.Solver('SolveIntegerProblem',
                                      pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    def SolveMIP(self):
        N = len(self.A)
        inter = [[0 for i in range(N)] for j in range(N)]
        intersecs = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if self.intersect(self.A[i], self.A[j]):
                    inter[i][j] = 1
                    inter[j][i] = 1
                    intersecs += 1

        print(intersecs)
        self.vars = self.produce_vars(self.A, intersecs, self.solver)
        print('Total of {} segments given as input'.format(self.A))
        constr_count = 0
        for i in range(N-1):
            for j in range(i+1, N):
                if inter[i][j]==1:
                    self.add_constraint(self.vars[j], self.vars[i], self.vars[N+constr_count-1], self.solver)
                    constr_count += 1

        objective = self.solver.Objective()
        for i in range(N):
            objective.SetCoefficient(self.vars[i], self.A[i][1]-self.A[i][0])
        objective.SetMinimization()

        """Solve the problem and print the solution."""
        result_status = self.solver.Solve()
        # The problem has an optimal solution.
        print(result_status)
        assert result_status == pywraplp.Solver.OPTIMAL

        # The solution looks legit (when using solvers other than
        # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
        #
        assert self.solver.VerifySolution(1e-9, True)
        print('Number of variables =', self.solver.NumVariables())
        print('Number of constraints =', self.solver.NumConstraints())

        # The value of each variable in the solution.
        for variable in self.vars:
          print('%s = %d' % (variable.name(), variable.solution_value()))
        print('Objective value is {}'.format(self.solver.Objective().Value()))


    def intersect(self, a, b):
        if a[0] < b[1] and a[1] > b[0]:
            return True
        else: return False


    def add_constraint(self, a, b, z, solver):
        my = []
        my.append(solver.Constraint(1, solver.infinity()))
        my[0].SetCoefficient(a, 1)
        my[0].SetCoefficient(b, -1)
        my[0].SetCoefficient(z, self.M)

        # f2nd ineq
        my.append(solver.Constraint(1-self.M, solver.infinity()))
        my[1].SetCoefficient(a, -1)
        my[1].SetCoefficient(b, 1)
        my[1].SetCoefficient(z, -self.M)

    def produce_vars(self, segments, n_inter, solver):
        var_list = []
        i = 0
        for segment in segments:
            var_list.append(solver.IntVar(0.0, 6.0, 'x'+str(i)))
            i+=1
        i=0
        for k in range(n_inter):
            var_list.append(solver.IntVar(0, 1, 'z'+str(i)))
            i+=1

        return var_list
