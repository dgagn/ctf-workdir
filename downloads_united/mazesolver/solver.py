from pwn import *
import queue


def valid(the_maze, moves):
    start = 0
    for x, pos in enumerate(the_maze[0]):
        if pos == 'S':
            start = x
    
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        
        elif move == "R":
            i += 1
        
        elif move == "U":
            j -= 1
        
        elif move == "D":
            j += 1
        
        if not (0 <= i < len(the_maze[0]) and 0 <= j < len(the_maze)):
            return False
        elif the_maze[j][i] == "#":
            return False
    
    return True


def find_end(the_maze, moves):
    start = 0
    for x, pos in enumerate(the_maze[0]):
        if pos == "S":
            start = x
    
    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1
        
        elif move == "R":
            i += 1
        
        elif move == "U":
            j -= 1
        
        elif move == "D":
            j += 1
    
    if the_maze[j][i] == "E":
        print("Found: " + moves)
        pprint(the_maze, moves)
        return True
    
    return False


p = remote('nc.ctf.unitedctf.ca', 5001)

maze = p.recv().strip().split(b'\n')

x_length = len(maze[0])
y_length = len(maze)

new_maze = []
for maze_line in maze:
    new_maze.append(list(maze_line.decode('ascii')))

info(f'the maze is {x_length}x{y_length} in size')

nums = queue.Queue()
nums.put("")
add = ""

pprint(maze)

while not find_end(new_maze, add):
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(new_maze, put):
            nums.put(put)

p.interactive()
