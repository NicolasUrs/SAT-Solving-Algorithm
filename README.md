# SAT-Solving-Algorithm by Urs Nicolas Robert 🚀

Welcome to my SAT solver collection! 🎉 I’m **Urs Nicolas Robert**, This repository contains a series of SAT solvers built to tackle the Boolean Satisfiability Problem (SAT) using different approaches. 🧠✨

## 🚀 Algorithms Included

| Algorithm        | File                | Description                                                        |
|------------------|---------------------|--------------------------------------------------------------------|
| **Pure Resolution** | `pure_resolution.py` | A classic approach that resolves clauses until a contradiction or a fixed point is reached. |
| **Davis-Putnam**   | `davis_putnam.py`   | A variable elimination technique that simplifies the formula using resolution. |
| **DPLL**           | `dpll.py`           | A backtracking algorithm with unit propagation and pure literal elimination. |

## 🔍 Algorithm Comparison

| Algorithm          | Time Complexity | Space Complexity | Strengths                                  | Weaknesses                              |
|--------------------|-----------------|------------------|--------------------------------------------|-----------------------------------------|
| **Pure Resolution** | Exponential     | Exponential      | Complete, theoretically elegant            | Inefficient for large formulas          |
| **Davis-Putnam**    | Exponential     | Exponential      | Improved variable elimination              | Still impractical for large inputs      |
| **DPLL**            | Exponential     | Linear           | Practical for moderately sized problems    | Still exponential in worst case         |
| **Modern SAT Solvers** | Exponential  | Linear           | Highly optimized for real-world problems   | Complex implementations                 |

## 🛠️ How to Run the SAT Solvers???

To run one of the solvers, follow these easy steps:

### 1. Clone or Download the Repository

Clone the repository to your local machine:
```bash
git clone https://github.com/NicolasUrs/SAT-Solving-Algorithm 
```
if u don't have the git on yout local machine , use the folllowing command:

On windows:

```bash
winget install --id Git.Git -e --source winget
```

On linux:
```bash
sudo apt update
sudo apt install git
```

or you can just download it :)

### 2. Navigate to the file:
Use the command (if you want this way): 
```bash
cd path/to/your/dir
```
### 3. Run the solvers via CNF File:
```bash
python dpll.py [input_example].cnf
python pure_resolution.py [input_example].cnf
python davis_putnam.py [input_example].cnf
```
