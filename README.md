# A naive implementation of [Algorithmic Lovász local lemma](https://en.wikipedia.org/wiki/Algorithmic_Lov%C3%A1sz_local_lemma)

- The `generator.py` implements a function to generate SAT instance which are satisfied for Lovasz local lemma constrain.
- The `solver.py` provides a solver which is based on the naive algorithmic lovasz local lemma.
- The `main.py` provides a demo for the implementation, as for comparison I add a pysat solver so to run it you need to install PySAT by `pip install python-sat` (or you can just comment the PySAT part in code).