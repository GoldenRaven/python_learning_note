class maze:
    def __init__(self, m, n, mat):
        self.row = m
        self.column = n
        self.matrix = mat
    def branch(self, pos):
        count = 0
        candidates = []
        x = pos[0]
        y = pos[1]
        if (0 <= y+1 < self.column) and self.matrix[pos[0]][pos[1] + 1] == 0:
            count += 1
            candidates.append([x, y+1])
        if (0 <= x-1 < self.row) and self.matrix[pos[0] - 1][pos[1]] == 0:
            count += 1
            candidates.append([x-1, y])
        if (0 <= y-1 < self.column) and self.matrix[pos[0]][pos[1] - 1] == 0:
            count += 1
            candidates.append([x, y-1])
        if (0 <= x+1 < self.row) and (self.matrix[x + 1][y] == 0):
            count += 1
            candidates.append([x+1, y])
        return candidates
    def flip(self, pos):
        x = pos[0]
        y = pos[1]
        if self.matrix[x][y] == 0:
            self.matrix[x][y] = 1
    def mark(self, pos):
        x = pos[0]
        y = pos[1]
        self.matrix[x][y] = 'x'

def wander(mz, x, y, br, path):
    path.append([x, y])
    if (x, y) == (m-1, n-1):
        raise AssertionError
    mz.flip([x, y])
    bond = len(mz.branch([x, y]))
    if bond > 1: br.append([x, y])
    if bond == 0:
        del(path[path.index(br[-1]):len(br)])
        [x, y] = br[-1]
    for [i, j] in maze1.branch([x, y]):
        [x, y] = [i, j]
        # print(x,y)
        wander(mz, x, y, br, path)
while True:
    try:
        [m, n] = list(map(int, input().split()))
        mat = []
        mat2 = []
        for i in range(m):
            mat.append(list(map(int, input().split())))
        maze1 = maze(m, n, mat)
        br = []
        path = []
        wander(maze1, 0, 0, br, path)
    except AssertionError:
        for i in range(len(path)):
            print('(',path[i][0], ',', path[i][1], ')', sep='')
        # print(path)
        # mat2 = mat
        # maze2 = maze(m, n, mat2)
        # for i in path:
        #     maze2.mark(i)
        # print()
        # for i in range(m):
        #     print(' '.join(map(str, maze2.matrix[i])))
        # break
    except:
        break
