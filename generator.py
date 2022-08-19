import random
from random import sample

# A random satisfiable k-sat instance generator based on lovasz local lemma.
# Noticed that the constrian is different with the original version and based on Theorem 1.3 in paper
# "DISPROOF OF THE NEIGHBORHOOD CONJECTURE WITH IMPLICATIONS TO SAT*"


def lll_sat_generator(n, k):
    if n < k:
        print("n must be greater or equal to k for k-sat problem")
        return []

    d = int(2 ** k / (2.71829 * k))
    clause_list = []
    vars_quota = [d] * n

    valid_vars = [i for i in range(n) if vars_quota[i] > 0]
    while len(valid_vars) >= k:
        _clause = sample(valid_vars, k)
        for x in _clause:
            vars_quota[x] -= 1
        valid_vars = [i for i in range(n) if vars_quota[i] > 0]
        _clause = [x+1 for x in _clause]
        _clause = [x if random.random() > 0.5 else -x for x in _clause]

        clause_list.append(_clause)

    return clause_list
