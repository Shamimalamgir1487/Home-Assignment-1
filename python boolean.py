# Task 1: Check if the 2-CNF formula is satisfiable
def is_satisfiable(formula: str) -> bool:
    # Convert formula to a more usable structure (e.g., list of clauses)
    clauses = parse_formula(formula)
    
    # Apply the 2-SAT algorithm (e.g., brute force or graph-based solution)
    assignment = two_sat(clauses)
    
    # Return whether the formula is satisfiable or not
    return assignment is not None

# Task 2: Find a satisfying assignment
def sat_assignment(formula: str) -> dict:
    # Convert formula to a more usable structure (e.g., list of clauses)
    clauses = parse_formula(formula)
    
    # Apply the 2-SAT algorithm to find a satisfying assignment
    assignment = two_sat(clauses)
    
    # Return the assignment if satisfiable, otherwise return None
    return assignment if assignment else None

# Helper function to parse the 2-CNF formula into clauses
def parse_formula(formula: str):
    # Example parsing function to split clauses and literals from the formula
    # Here we assume the formula is already in a cleaned 2-CNF string form.
    # You can extend this to handle more complex input strings.
    
    clauses = []
    formula = formula.replace(' ', '')  # Remove spaces
    split_formula = formula.split('/\\')  # Split clauses on conjunctions
    
    for clause in split_formula:
        if '->' in clause:
            literals = clause.split('->')
            clauses.append(('~' + literals[0], literals[1]))  # Implication
        elif '\\/' in clause:
            literals = clause.split('\\/')
            clauses.append((literals[0], literals[1]))  # Disjunction
        else:
            literals = clause  # Single literal clause
            clauses.append((literals,))
    
    return clauses

# Helper function for solving 2-SAT using a graph-based approach
def two_sat(clauses):
    # We'll use a simple truth assignment mechanism for each variable
    # Variables will be assigned based on a basic check of the clauses
    
    assignment = {}
    
    for clause in clauses:
        if len(clause) == 1:
            # If it's a single literal clause, assign it directly
            literal = clause[0]
            variable = literal.replace('~', '')  # Remove negation to get the variable
            value = False if literal.startswith('~') else True
            if variable in assignment and assignment[variable] != value:
                return None  # Conflict in assignments
            assignment[variable] = value
        else:
            # Handle (L1 \/ L2) or (L1 -> L2)
            literal1, literal2 = clause
            var1 = literal1.replace('~', '')
            var2 = literal2.replace('~', '')
            val1 = False if literal1.startswith('~') else True
            val2 = False if literal2.startswith('~') else True
            
            # Try assigning the values for both literals
            if var1 not in assignment and var2 not in assignment:
                assignment[var1] = not val1
                assignment[var2] = not val2
            elif var1 in assignment and assignment[var1] == val1:
                assignment[var2] = val2
            elif var2 in assignment and assignment[var2] == val2:
                assignment[var1] = val1
            else:
                return None  # Conflict in assignments
    
    return assignment


# Example usage of the code:
if name == 'main':
    formula = 'p /\\ (p -> q) /\\ (p -> ~r) /\\ (~r \\/ ~s) /\\ (s \\/ ~q)'
    
    # Task 1: Check if the formula is satisfiable
    is_sat = is_satisfiable(formula)
    print(f"Is the formula satisfiable? {is_sat}")
    
    # Task 2: Find a satisfying assignment if it exists
    assignment = sat_assignment(formula)
    if assignment:
        print("Satisfying assignment found:", assignment)
    else:
        print("No satisfying assignment exists.")
