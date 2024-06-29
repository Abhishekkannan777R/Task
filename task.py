def print_pattern(rows, cols):
    for c in range(cols+1):        
        for r in range(rows):
            if c == 0:
                print("  __      ", end="")
            if r == rows-1 :
                print() 
        for k in range(rows):
            if c%2==0:
                if(k == rows-1 ):
                    print("/    \ ",end="")
                else:
                    print("/    \ __ " ,end="")
            else:
                print("\ __ /    ",end="")

        


print_pattern(3, 5)
print()
print()
print()
print_pattern(4, 7)
