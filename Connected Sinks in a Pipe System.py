"""
Implemented with DFS method.
It's also a classical dynamic programming problem since it has clear state transitioning,
but since it's hard to read and I have to go for a networking event, I just paused here.
"""


def connected_sinks(input_path):
    """ the main function to find the connected sinks in a pipe system """
    file_data = parse_input_file(input_path)
    pipe_map = dict(pipe2coordination(file_data))
    coord_map = dict(coordination2pip(pipe_map))

    pip_conf = get_pip_configuration()

    starter = coord_map['*']
    visited = []
    res = []

    def dfs(x, y, direction):
        if (x, y) in visited or (x, y) not in pipe_map:
            return
        cur_pipe = pipe_map[(x, y)]
        if cur_pipe not in pip_conf:
            if cur_pipe not in res and cur_pipe != "*":
                res.append(cur_pipe)
            return
        else:
            # if not connected, then exit
            if pip_conf[cur_pipe][(direction + 2) % 4] != 1:
                return

        visited.append((x, y))

        cur_pip_conf = pip_conf[cur_pipe]
        if cur_pip_conf[0] == 1:  # go up
            dfs(x, y + 1, 0)
        if cur_pip_conf[1] == 1:  # go left
            dfs(x - 1, y, 1)
        if cur_pip_conf[2] == 1:  # go down
            dfs(x, y - 1, 2)
        if cur_pip_conf[3] == 1:  # go right
            dfs(x + 1, y, 3)

    dfs(starter[0], starter[1] + 1, 0)  # go up
    dfs(starter[0] - 1, starter[1], 1)  # go left
    dfs(starter[0], starter[1] - 1, 2)  # go down
    dfs(starter[0] + 1, starter[1], 3)  # go right

    return "".join(sorted(res))


def parse_input_file(path):
    """ read file and get the content as a list """
    try:
        with open(path) as f:
            return list(f)
    except FileNotFoundError:
        raise Exception("Input file not found: ", path)


def pipe2coordination(f):
    """ create a dictionary contains coordination as key, and char as value """
    for line in f:
        ls = line.split()
        yield (int(ls[1]), int(ls[2])), ls[0]


def coordination2pip(pipe_data):
    """ reverse the map of coordination-char, so that we can get the coordination by the char """
    for ele in pipe_data:
        yield pipe_data[ele], ele


def get_pip_configuration():
    """ the list in each element is to flag the open port of a pipe: [top, left, bottom, right] """
    return {
        '═': [0, 1, 0, 1],
        '║': [1, 0, 1, 0],
        '╔': [0, 0, 1, 1],
        '╗': [0, 1, 1, 0],
        '╚': [1, 0, 0, 1],
        '╝': [1, 1, 0, 0],
        '╠': [1, 0, 1, 1],
        '╣': [1, 1, 1, 0],
        '╦': [0, 1, 1, 1],
        '╩': [1, 1, 0, 1]
    }


if __name__ == "__main__":
    INPUT_PATH = "/Users/wxf/Downloads/DataAnnotation/Assessment/coding_qual_input.txt"
    res = connected_sinks(INPUT_PATH)
    print(res)
