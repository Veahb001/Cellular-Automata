#Contains the  generation simulation logic for the automaton.

def next_generation(cells, rule_dict):
    
    #Computes the next generation using wrap-around neighbors.
    
    length = len(cells)
    new_cells = []
    for i in range(length):
        # Use modulo arithmetic to wrap around the ends (circular boundary conditions)
        left = cells[(i - 1) % length]
        center = cells[i]
        right = cells[(i + 1) % length]
       
        # Form the 3-bit pattern string, e.g., "110", "001", etc.
        pattern = f"{left}{center}{right}"

        # Look up the outcome for this pattern in the rule dictionary
        # If pattern not found (shouldn’t happen), default to 0
        new_cells.append(rule_dict.get(pattern, 0))
    return new_cells