#Handles displaying cell generations.

def display_generation(cells):
    
    #Prints the generation using '.' for 0 and 'x' for 1.
    
    print(''.join('x' if cell else '.' for cell in cells))