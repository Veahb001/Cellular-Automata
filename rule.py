#Logic fo r rule number to binary and rule dictionary

def get_rule_dict(rule_num):
    
    #Conveerts a rule number (0-255) to a dictionary mapping binary patterns to their corresponding output.
    binary = f"{rule_num:08b}"
    patterns = [f"{i:03b}" for i in range(7, -1,-1)]
    return {pattern: int(bit) for pattern, bit in zip(patterns, binary)}