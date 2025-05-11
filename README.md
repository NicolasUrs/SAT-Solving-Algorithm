# SAT-Solving-Algorithm by [Urs Nicolas Robert] 🚀

Welcome to my SAT solver collection! 🎉 I’m [Your Name], a passionate computer science enthusiast exploring the world of SAT solvers. This repository contains a series of SAT solvers built to tackle the Boolean Satisfiability Problem (SAT) using different approaches. 🧠✨

## 🚀 Algorithms Included

| Algorithm | File | Description |
|-----------|------|-------------|
| Pure Resolution | `pure_resolution.py` | A classic approach that resolves clauses until a contradiction or a fixed point is reached. |
| Davis-Putnam | `davis_putnam.py` | A variable elimination technique that simplifies the formula using resolution. |
| DPLL | `dpll.py` | A backtracking algorithm with unit propagation and pure literal elimination. |
| PySAT Benchmark | `pysat_benchmark.py` | Benchmarking tool to test modern SAT solvers (e.g., Glucose3, Glucose4). |

## 🛠️ How to Run the SAT Solvers

To run one of the solvers, follow these easy steps:

1. Clone or download this repo.
2. Navigate to the directory.
3. Run one of the solvers with a CNF file:

```bash
python dpll.py --input example.cnf
