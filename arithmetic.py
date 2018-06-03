import sys

# Recursively search for answer. Sets a boolean flag if it is found.
def solve(depth, total, output):
    global found
    global operands
    global target
    if found or total > target or (total != target and depth >= len(operands) -1):
        return
    if total == target and depth >= len(operands) -1:
        found = True
        print(f"L {target} {output}")
    else:
        depth = depth + 1
        addout = output + ' + ' + str(operands[depth])
        multiout = output + ' * ' + str(operands[depth])
        solve(depth, int(operands[depth]) + total, addout)
        solve(depth, int(operands[depth]) * total, multiout)

# Read lines from stdin
def read_lines():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    return lines

# Main function. Split input lines, assign variables
# and call recursive function for each input
def main():
    global operands, target, found
    lines = read_lines()
    for i in range(0, len(lines), 2):
        found = False
        operands = lines[i].split(" ")
        output = str(operands[0])
        line_2 = lines[i+1].split(" ")
        target = int(line_2[0])
        solve(0, int(operands[0]) , output)
        if not found:
            print(f"L {target} impossible")

# Global variables
operands = []
found = False
target = 6

# Run the program
main()

