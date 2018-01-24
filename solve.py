from __future__ import print_function
from ortools.linear_solver import pywraplp

def main():
  M = 10
  # Instantiate a mixed-integer solver, naming it SolveIntegerProblem.
  solver = pywraplp.Solver('SolveIntegerProblem',
                           pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

  # x and y are integer non-negative variables.
  x1 = solver.IntVar(0.0, 5.0, 'x1') #solver.infinity()
  x2 = solver.IntVar(0.0, 5.0, 'x2')
  x3 = solver.IntVar(0.0, 5.0, 'x3')
  z1 = solver.IntVar(0.0, 1.0, 'z1')
  z2 = solver.IntVar(0.0, 1.0, 'z2')

  # x + 7 * y <= 17.5
  # constraint1 = solver.Constraint(-solver.infinity(), 17.5)
  # constraint1.SetCoefficient(x, 1)
  # constraint1.SetCoefficient(y, 7)

  # first ineq
  constraint1 = solver.Constraint(1, solver.infinity())
  constraint1.SetCoefficient(x1, -1)
  constraint1.SetCoefficient(x2, 1)
  #constraint1.SetCoefficient(x3, 0)
  constraint1.SetCoefficient(z1, M)
  #constraint1.SetCoefficient(z2, 0)

  # f2nd ineq
  constraint2 = solver.Constraint(1-M, solver.infinity())
  constraint2.SetCoefficient(x1, 1)
  constraint2.SetCoefficient(x2, -1)
  #constraint2.SetCoefficient(x3, 0)
  constraint2.SetCoefficient(z1, -M)
  #constraint2.SetCoefficient(z2, 0)

  # 3rd ineq
  constraint3 = solver.Constraint(1, solver.infinity())
  #constraint3.SetCoefficient(x1, 0)
  constraint3.SetCoefficient(x2, -1)
  constraint3.SetCoefficient(x3, 1)
  #constraint3.SetCoefficient(z1, 0)
  constraint3.SetCoefficient(z2, M)

  # 4th ineq
  constraint4 = solver.Constraint(1-M, solver.infinity())
  #constraint4.SetCoefficient(x1, 0)
  constraint4.SetCoefficient(x2, 1)
  constraint4.SetCoefficient(x3, -1)
  #constraint4.SetCoefficient(z1, 0)
  constraint4.SetCoefficient(z2, -M)

  # Maximize x + 10 * y.
  objective = solver.Objective()
  objective.SetCoefficient(x1, -1)
  objective.SetCoefficient(x2, -1)
  objective.SetCoefficient(x3, -1)
  objective.SetMaximization()

  """Solve the problem and print the solution."""
  result_status = solver.Solve()
  # The problem has an optimal solution.
  print(result_status)
  assert result_status == pywraplp.Solver.OPTIMAL

  # The solution looks legit (when using solvers other than
  # GLOP_LINEAR_PROGRAMMING, verifying the solution is highly recommended!).
  #
  assert solver.VerifySolution(1e-7, True)
  print('Number of variables =', solver.NumVariables())
  print('Number of constraints =', solver.NumConstraints())

  # The objective value of the solution.
  #print('Optimal objective value = %d' % solver.Objective().Value())
  print()
  # The value of each variable in the solution.
  variable_list = [x1, x2, x3, z1, z2]

  for variable in variable_list:
    print('%s = %d' % (variable.name(), variable.solution_value()))

if __name__ == '__main__':
  main()
