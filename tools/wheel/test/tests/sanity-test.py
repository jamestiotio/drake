#!/usr/bin/env python

import numpy
import pydrake.all

# Basic sanity checks.
print(pydrake.getDrakePath())
print(pydrake.all.PackageMap().GetPath('drake'))

# Check for presence of optional solvers.
assert pydrake.all.MosekSolver().available(), 'Missing MOSEK'
assert pydrake.all.SnoptSolver().available(), 'Missing SNOPT'

# Once we drop Focal and its nerfs, we won't need this sanity-check anymore
# (because we won't be at risk of accidentally turning off Clarabel).
assert pydrake.all.ClarabelSolver().available(), 'Missing Clarabel'

# Check that IPOPT is working.
prog = pydrake.all.MathematicalProgram()
x = prog.NewContinuousVariables(2, 'x')
prog.AddLinearConstraint(x[0] >= 1)
prog.AddLinearConstraint(x[1] >= 1)
prog.AddQuadraticCost(numpy.eye(2), numpy.zeros(2), x)
solver = pydrake.all.IpoptSolver()
assert solver.Solve(prog, None, None).is_success(), 'IPOPT is not usable'
