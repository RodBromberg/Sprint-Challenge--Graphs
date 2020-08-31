from room import Room
from player import Player
from world import World
from queue import Queue

import random
from ast import literal_eval

traversal_path = []

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def bfs(player):
    diff_directions = ['n', 's', 'e', 'w']
    rev_dict = {
        'n': 's',
        's': 'n',
        'w': 'e',
        'e': 'w'
    }
    visited_vertices = {}
    arr = []

    # create queue
    # grab start id
    # check if traversal is complete
    # check dequeued element add dictionary and use helper function to get exits
    # if array is truthy set prev path to indx and if ? set to prev
    # loop through vertices and if we have a direction add to avail directions
    # grab a random direction to continue traversal
    # push idx and direction to arr of dicts
    # push path and then check if we have no exits to pop off arr go back to prev room
    # travel to next room and then push path

    queue = Queue()
    queue.enqueue(player.current_room.id)
    while queue:

        pos_exits = []
        if len(visited_vertices) == 500:
            return visited_vertices

        current_path = queue.dequeue()

        while current_path not in visited_vertices:
            visited_vertices[current_path] = {}
            for path in player.current_room.get_exits():
                visited_vertices[current_path][path] = '?'
            if path == '?':
                current_path = 's'

        if arr:
            prev_path = arr[-1]['idx']
            prev_room = rev_dict[arr[-1]['path']]
            if visited_vertices[current_path][prev_room] == '?':
                visited_vertices[current_path][prev_room] = prev_path

        for path in visited_vertices[current_path]:
            if 'n' in visited_vertices[current_path] and visited_vertices[current_path][path] == '?':
                pos_exits.append(path)
            if 's' in visited_vertices[current_path] and visited_vertices[current_path][path] == '?':
                pos_exits.append(path)
            if 'e' in visited_vertices[current_path] and visited_vertices[current_path][path] == '?':
                pos_exits.append(path)
            if 'w' in visited_vertices[current_path] and visited_vertices[current_path][path] == '?':
                pos_exits.append(path)

        if pos_exits:
            path = random.choice(pos_exits)
            player.travel(path)

            visited_vertices[current_path][path] = player.current_room.id
            arr.append({
                'idx': current_path,
                'path': path
            })
            traversal_path.append(path)

        if len(pos_exits) == 0:
            arr.pop()
            path = prev_room
            player.travel(path)
            traversal_path.append(path)

        queue.enqueue(player.current_room.id)


bfs(player)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def dfs(player):
    diff_directions = ['n', 's', 'e', 'w']
    rev_dict = {
        'n': 's',
        's': 'n',
        'w': 'e',
        'e': 'w'
    }
    visited_vertices = Queue()
    arr = []

    stack = Stack()
    visited_vertices = {}

    while stack:
        pos_exits = Stack()
        if len(visited_vertices) == 500:
            return visited_vertices

        current_path = stack.pop()

        while current_path not in visited_vertices:
            visited_vertices[current_path] = {}
            for path in player.current_room.get_exits():
                visited_vertices[current_path][path] = '?'
                current_path = rev_dict[path]

        # if possible_exits:
        #     path = random.choice(possible_exits)
        #     player.travel(path)

        #     visited_vertices[current_path][path] = player.current_room.id
        #     arr.append({
        #         'idx': current_path,
        #         'path': path
        #     })
        #     traversal_path.append(path)


# # Fill this out with directions to walk
# # traversal_path = ['n', 'n']
#
# # TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
