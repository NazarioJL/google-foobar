

def generate_modified_mazes(maze):
    """ generates original maze and subsequently mazes with one (1) wall removed """
    # yield copy of same maze
    yield [x[:] for x in maze]

    width = len(maze[0])
    height = len(maze)

    for j in xrange(height):
        for i in xrange(width):
            if maze[j][i] == 1:
                # if wall is blocked in at least 3 sides no need to remove this wall
                blocked_sides = 0
                if j == 0 or maze[j - 1][i] == 1:
                    blocked_sides += 1
                if j == height - 1 or maze[j + 1][i] == 1:
                    blocked_sides += 1
                if i == 0 or maze[j][i - 1] == 1:
                    blocked_sides += 1
                if i == width - 1 or maze[j][i + 1] == 1:
                    blocked_sides += 1
                if blocked_sides < 3:
                    new_maze = [x[:] for x in maze]
                    new_maze[j][i] = 0
                    yield new_maze

def find_path(maze, current_best):
    """ Uses a problem optmized A* pathfinding algorithm to search for the shortest path """
    width = len(maze[0])
    height = len(maze)

    # end and start nodes are always the same let functions close over them
    start = (0, 0)
    end = (width - 1, height - 1)

    def heuristic(node):
        x1, y1 = node
        x2, y2 = end
        return (x2 - x1) + (y2 - y1)

    def compute_path(path):
        result = [end]
        current = end
        while current != start:
            current = path[current]
            result.append(current)

        return result

    def neighbours(node):
        x, y = node
        for i, j in [(0, -1), (0, +1), (-1, 0), (+1, 0)]:
            x1 = x + i
            y1 = y + j
            if x1 >= 0 and y1 >= 0 and x1 < width and y1 < height:
                if maze[y1][x1] == 0:
                    yield (x1, y1)

    closed_set = set([])
    open_set = set([start])
    visited_nodes = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = heuristic(start)

    while len(open_set) > 0:
        current = min(f_score, key=f_score.get)
        # if the current smallest f_score is worst than previous found, stop calculating
        current_f = f_score[current]
        if current_f > current_best:
            break

        if current == end:
            return compute_path(visited_nodes)

        open_set.discard(current)
        del f_score[current]
        closed_set.add(current)

        for neighbor in neighbours(current):
            if neighbor in closed_set:
                continue
            tmp_g_score = g_score[current] + 1

            if (neighbor not in open_set) or (tmp_g_score < g_score[neighbor]):
                visited_nodes[neighbor] = current
                g_score[neighbor] = tmp_g_score
                f_score[neighbor] = tmp_g_score + heuristic(neighbor)
                open_set.add(neighbor)
    return None

def find_best_path(maze):
    """ finds the shortest solution path to maze my removing at most one wall """
    width = len(maze[0])
    height = len(maze)

    # calculate initial assumptions
    best_solution = width + height - 1
    worst_solution = width * height
    result = worst_solution

    for modified_maze in generate_modified_mazes(maze):
        tmp = find_path(modified_maze, width * height)
        if tmp is None:
            continue
        tmp_length = len(tmp)
        if tmp_length < result:
            result = tmp_length
        if result == best_solution:
            break

    return result

def answer(maze):
    solution = find_best_path(maze)
    return solution
