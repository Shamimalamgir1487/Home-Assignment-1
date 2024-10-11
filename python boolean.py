# Task 1: Check if the 2-CNF formula is satisfiable
def is_satisfiable(formula: str) -> bool:
    # Convert formula to a more usable structure (e.g., list of clauses)
    clauses = parse_formula(formula)
    
    # Apply the 2-SAT algorithm (e.g., Tarjan's SCC algorithm or brute force)
    if two_sat(clauses):
        return True
    else:
        return False

# Task 2: Find a satisfying assignment
def sat_assignment(formula: str) -> dict:
    # Convert formula to a more usable structure (e.g., list of clauses)
    clauses = parse_formula(formula)
    
    # Apply the 2-SAT algorithm to find a satisfying assignment
    assignment = find_satisfying_assignment(clauses)
    
    return assignment

# Helper function to parse the 2-CNF formula into clauses
def parse_formula(formula: str):
    # Parsing logic goes here
    # Convert the formula string to a list of clauses, such as:
    # [(p, q), (~r, s), ...]
    pass

# Helper function for solving 2-SAT using a graph-based approach
def two_sat(clauses):
    # Implement 2-SAT satisfiability check (e.g., SCC)
    pass

# Helper function to find a satisfying assignment if satisfiable
def find_satisfying_assignment(clauses):
    # Return a dictionary of variable assignments
    pass
