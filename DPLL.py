"""
DPLL (Davis-Putnam-Logemann-Loveland) SAT Solver
Reads a DIMACS CNF file and determines satisfiability using the DPLL algorithm.
Run the code in terminal as python DPLL.py sat.cnf for sat
Run the code in terminal as python DPLL.py unsat.cnf for unsat
"""
import sys
import time


def dpll(clauses, assignment=None):
    if assignment is None:
        assignment = {}

    new_clauses = []
    for cl in clauses:
        if any((lit > 0 and assignment.get(abs(lit), None) == True) or
               (lit < 0 and assignment.get(abs(lit), None) == False)
               for lit in cl):
            continue

        filtered = [lit for lit in cl if not ((lit > 0 and assignment.get(abs(lit), None) == False) or
                                              (lit < 0 and assignment.get(abs(lit), None) == True))]
        if not filtered:
            return False, {}

        new_clauses.append(filtered)

    if not new_clauses:
        return True, assignment.copy()

    for cl in new_clauses:
        if len(cl) == 1:
            lit = cl[0]
            val = (lit > 0)
            var = abs(lit)
            if var not in assignment:
                assignment[var] = val
                return dpll(clauses, assignment)

    pos = set(abs(lit) for cl in new_clauses for lit in cl if lit > 0)
    neg = set(abs(lit) for cl in new_clauses for lit in cl if lit < 0)

    for var in pos:
        if var not in neg:
            assignment[var] = True
            return dpll(clauses, assignment)

    for var in neg:
        if var not in pos:
            assignment[var] = False
            return dpll(clauses, assignment)

    lit = new_clauses[0][0]
    var = abs(lit)

    assignment_copy = assignment.copy()
    assignment_copy[var] = True
    sat, res = dpll(clauses, assignment_copy)
    if sat:
        return True, res

    assignment_copy = assignment.copy()
    assignment_copy[var] = False
    return dpll(clauses, assignment_copy)


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
        satisfiable, assignment = dpll(clauses)
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