from pwn import *

m = []
a = []

def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:
                if i > 0 and m[i - 1][j] == 0 and a[i - 1][j] == 0:
                    m[i - 1][j] = k + 1
                if j > 0 and m[i][j - 1] == 0 and a[i][j - 1] == 0:
                    m[i][j - 1] = k + 1
                if i < len(m) - 1 and m[i + 1][j] == 0 and a[i + 1][j] == 0:
                    m[i + 1][j] = k + 1
                if j < len(m[i]) - 1 and m[i][j + 1] == 0 and a[i][j + 1] == 0:
                    m[i][j + 1] = k + 1

def main():
    p = remote('nc.ctf.unitedctf.ca', 5002)
    _m = p.recv().strip().split(b'\n')
    start = 0, 0
    end = 0, 0
    y = 0
    for s in _m:
        x = 0
        new_m = list(s)
        y_maze = []
        for w in new_m:
            if w == 69:
                end = y, x
            if w == 83:
                start = y, x
            if w == 69 or w == 83 or w == 32:
                y_maze.append(0)
            elif w == 35:
                y_maze.append(1)
            else:
                raise RuntimeError('wtf happened')
            x += 1
        a.append(y_maze)
        y += 1
    info(f'the maze starts at {start} and ends at {end}')
    pprint(a)
    info('starting algo')

    for i in range(len(a)):
        m.append([])
        for j in range(len(a[i])):
            m[-1].append(0)
    i, j = start
    m[i][j] = 1

    k = 0
    while m[end[0]][end[1]] == 0:
        k += 1
        make_step(k)

    i, j = end
    k = m[i][j]
    the_path = [(i, j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            the_path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            the_path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            the_path.append((i, j))
            k -= 1

    the_path.reverse()

    the_path = the_path[1:-1]

    for (x, y) in the_path:
        print(f'{y} {x}')
        p.sendline(f'{x} {y}')
    p.sendline('.')

    r = p.recv()
    pprint(r)
    p.interactive()

main()