def print_pattern(rows, cols):
    for c in range(cols+1):
        # Print the top part of the hexagons
        for r in range(rows):
            if c == 0:
                print("  __      ", end="")
            if r == rows-1 :
                print()  # New line after top part of the hexagons
        for k in range(rows):
            if c%2==0:
                if(k == rows-1 ):
                    print("/    \ ",end="")
                else:
                    print("/    \ __ " ,end="")
            else:
                print("\ __ /    ",end="")

        # Print the middle part of the hexagons
        
        # New line after the bottom part of the hexagons

# Example usage
print_pattern(3, 5)
print()
print()
print()
print_pattern(4, 7)