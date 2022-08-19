import time

from pysat.formula import CNF
from pysat.solvers import Solver

from generator import lll_sat_generator
from solver import lll_solver


def main():
    n = 1000
    k = 10
    sat_instance = lll_sat_generator(n, k)
    print(f"clauses number: {len(sat_instance)}")
    print(f"clauses density: {len(sat_instance)/n}")

    print('<<<<<<<<LLL solver>>>>>>>>')
    start_time = time.time()
    assignment, iterations = lll_solver(n, sat_instance)
    print(f"solver iterations: {iterations}")
    print(f"solver time: {time.time() - start_time:.4f}")

    print('<<<<<<<<pysat>>>>>>>>')
    cnf = CNF(from_clauses=sat_instance)
    start_time = time.time()
    with Solver(bootstrap_with=cnf) as solver:
        solver.solve()
    print(f"solver time: {time.time() - start_time:.4f}")


if __name__ == "__main__":
    main()
