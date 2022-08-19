# A solver based on Algorithmic Lovász local lemma: https://en.wikipedia.org/wiki/Algorithmic_Lov%C3%A1sz_local_lemma
import random


def is_satisfied(clause, assignment):
    for literal in clause:
        if literal * assignment[abs(literal) - 1] > 0:
            return True
    return False

# http://tcs.nju.edu.cn/slides/random2015/LLL.pdf


def lll_solver(n, instance):
    assignment = [1 if random.random() > 0.5 else -1 for x in range(1, n+1)]
    iterations = 0
    solved = False

    while not solved:
        iterations += 1
        solved = True
        for clause in instance:
            if is_satisfied(clause, assignment):
                pass
            else:
                solved = False
                literal = random.choice(clause)
                assignment[abs(literal) - 1] = -assignment[abs(literal) - 1]
                break

    return assignment, iterations
