#Entry point for the program

from rule import get_rule_dict
from automaton import next_generation
from display import display_generation

def main():
    # Print author declaration and academic integrity statement
    print("Author: Harmon Vears")
    print("Student ID: 110352759")
    print("Email ID: Veahb001")
    print("This is my own work as defined by the University's Academic Misconduct Policy.")
    
    try:
        # Prompt user to enter the rule number (between 0 and 255)
        rule_num = int(input("Enter rule number (0–255): "))
        if not (0 <= rule_num <= 255):
            raise ValueError("Rule number must be between 0 and 255.")

        # Prompt user to enter the number of generations
        generations = int(input("Enter number of generations: "))
        if generations <= 0:
            raise ValueError("Number of generations must be positive.")

        # Prompt user for input type (custom or standard)
        input_type = input("Custom input (c) or standard input (s)? ").lower()

        if input_type == 'c':
            # Prompt user for custom input of 0s and 1s
            input_str = input("Enter custom input (0s and 1s only): ")
            if not all(ch in '01' for ch in input_str):
                raise ValueError("Input must contain only 0s and 1s.")
            cells = [int(ch) for ch in input_str]

        elif input_type == 's':
            # Standard input: ask for number of cells and initialize with one cell set to 1
            cell_count = int(input("Enter number of cells: "))
            if cell_count <= 0:
                raise ValueError("Number of cells must be positive.")
            cells = [0] * cell_count
            cells[cell_count // 2] = 1
        else:
            raise ValueError("Invalid input type. Must be 'c' or 's'.")

        # Generate the rule dictionary based on the rule number
        rule_dict = get_rule_dict(rule_num)

        # Display the initial generation
        for _ in range(generations + 1):
            display_generation(cells)
            cells = next_generation(cells, rule_dict)

    except Exception as e:
        # Catch and print any errors encountered during input or processing
        print(f"Error: {e}")

if __name__ == "__main__":
    main()