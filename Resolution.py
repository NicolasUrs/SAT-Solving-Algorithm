"""
Resolution-based SAT Solver
Reads a DIMACS CNF file and determines satisfiability using resolution.
Run the code in terminal as: python Resolution.py sat.cnf for sat
Run the code in terminal as: python Resolution.py unsat.cnf for unsat
"""
import sys
import time


def resolution_sat(clauses):

    clauses_set = set(frozenset(cl) for cl in clauses if cl)
    clauses = {cl for cl in clauses_set if not any(-lit in cl for lit in cl)}

    while True:
        new_clauses = set()
        clause_list = list(clauses)
        n = len(clause_list)

        for i in range(n):
            for j in range(i + 1, n):
                ci, cj = clause_list[i], clause_list[j]

                for lit in ci:
                    if -lit in cj:
                        resolvent = set(ci) - {lit}
                        resolvent |= (cj - {-lit})

                        if any(-l in resolvent for l in resolvent):
                            continue

                        resolvent = frozenset(resolvent)
                        if len(resolvent) == 0:
                            return False

                        new_clauses.add(resolvent)

        if new_clauses.issubset(clauses):
            break

        clauses |= new_clauses

    return True


def parse_dimacs(file_path):

    clauses = []
    num_variables = 0
    num_clauses = 0

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith('c'):
                continue

            if line.startswith('p'):
                parts = line.split()
                if len(parts) >= 4 and parts[1] == 'cnf':
                    num_variables = int(parts[2])
                    num_clauses = int(parts[3])
                continue

            literals = list(map(int, line.split()))
            if literals[-1] == 0:
                literals.pop()

            if literals:
                clauses.append(literals)

    return num_variables, clauses


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dimacs_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        print(f"Reading DIMACS file: {file_path}")
        num_variables, clauses = parse_dimacs(file_path)
        print(f"Problem has {num_variables} variables and {len(clauses)} clauses")

        start_time = time.time()
        result = resolution_sat(clauses)
        end_time = time.time()

        print(f"Time taken: {end_time - start_time:.4f} seconds")

        if result:
            print("SATISFIABLE")
        else:
            print("UNSATISFIABLE")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
