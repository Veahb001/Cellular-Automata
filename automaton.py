#Contains the  generation simulation logic for the automaton.

def next_generation(cells, rule_dict):
    
    #Computes the next generation using wrap-around neighbors.
    
    length = len(cells)
    new_cells = []
    for i in range(length):
        left = cells[(i - 1) % length]
        center = cells[i]
        right = cells[(i + 1) % length]
        pattern = f"{left}{center}{right}"
        new_cells.append(rule_dict.get(pattern, 0))
    return new_cells