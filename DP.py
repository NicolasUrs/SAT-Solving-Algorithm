"""
Davis-Putnam Resolution SAT Solver
Reads a DIMACS CNF file and determines satisfiability using the Davis-Putnam algorithm.
Run the code in terminal as: python DP.py sat.cnf for sat
Run the code in terminal as: python DP.py unsat.cnf for unsat
"""
import sys
import time


def dp_resolution(clauses, vars=None):

    if vars is None:
        vars = set(abs(lit) for cl in clauses for lit in cl)

    clauses = [cl for cl in clauses if not any(-lit in cl for lit in cl)]

    if any(len(cl) == 0 for cl in clauses):
        return False, {}

    if not clauses:
        return True, {}

    p = min(vars)
    vars = vars - {p}

    pos = [cl for cl in clauses if p in cl]
    neg = [cl for cl in clauses if -p in cl]
    rest = [cl[:] for cl in clauses if p not in cl and -p not in cl]

    resolvents = []
    for cl_pos in pos:
        for cl_neg in neg:
            newcl = [l for l in cl_pos if l != p] + [l for l in cl_neg if l != -p]
            if any(-l in newcl for l in newcl):
                continue
            resolvents.append(newcl)

    new_formula = rest + resolvents
    sat, assignment = dp_resolution(new_formula, vars)

    if not sat:
        return False, {}

    assignment[p] = False

    def satisfies_all(clauses, assign):
        for cl in clauses:
            if not any((lit > 0 and assign.get(abs(lit), None) == True) or
                       (lit < 0 and assign.get(abs(lit), None) == False)
                       for lit in cl):
                return False
        return True

    if not satisfies_all(clauses, assignment):
        assignment[p] = True

    return True, assignment


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
        satisfiable, assignment = dp_resolution(clauses)
        end_time = time.time()

        print(f"Time taken: {end_time - start_time:.4f} seconds")

        if satisfiable:
            print("SATISFIABLE")
            sorted_assignment = sorted(assignment.items())
            print("Assignment:")
            for var, val in sorted_assignment:
                print(f"{var if val else -var}", end=" ")
            print("0")
        else:
            print("UNSATISFIABLE")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
