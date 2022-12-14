import utils

lines = utils.get_file_lines("../inputs/input_day7.txt")
lines = utils.get_file_lines("../inputs/test_1_day7.txt")

#print(lines)

class MyTree:
    def __init__(self, tag, data):
        self.nodes = []
        self.tag = tag
        self.data = data

    def has_node(self, in_node):
        for node in self.nodes:
            if node.tag == in_node.tag and node.data == in_node.data:
                return True
        return False
        
    def print(self, indent = 0):
        print("{indent}{data} ({tag})".format(
            indent='  ' * indent,
            tag=self.tag,
            data=self.data,
            nodes=[(n.tag, n.data, len(n.nodes)) for n in self.nodes]))

        for node in self.nodes:
            node.print(indent+1)


class MyFileSystem:
    def __init__(self):
        self.tree = None

    def get_node_by_path(self, path):
        cur_node = self.tree
        for path_node in path:
            for tree_node in cur_node.nodes:
                if tree_node.tag == 'dir' and tree_node.data == path_node:
                    cur_node = tree_node
                    break
        return cur_node

    def add_node(self, path, node):
        if self.tree is None:
            self.tree = node
        else:
            cur_node = self.get_node_by_path(path)
            
            if not cur_node.has_node(node):
                cur_node.nodes.append(node)
    
    def add_dir(self, path, dir_name):
        #print("  add dir: path '{}' dir '{}'".format(path, dir_name))

        self.add_node(path, MyTree('dir', dir_name))
    
    def add_file(self, path, file_name, size):
        #print("  add file: path '{}' name '{}' size '{}'".format(path, file_name, size))

        self.add_node(path, MyTree('file', (file_name, size)))

    def get_dir_sizes(self):
        dir_sizes = []
        if not self.tree:
            return dir_sizes

        #todo: impl this
        
        return dir_sizes


    def print_tree(self):
        if self.tree is None:
            print("Tree is empty")
            return
        
        print("Tree:")
        self.tree.print()

        
def parse_commands(lines):
    commands = []
    cur_command_id = None
    cur_command_nodes = None
    cur_command_output = []
    for line in lines:
        nodes = line.split(' ')
        if cur_command_id == None:
            cur_command_id = nodes[1]
            cur_command_nodes = nodes
            continue
            
        if nodes[0] == '$':
            commands.append((cur_command_id, cur_command_nodes, cur_command_output))
            cur_command_id = nodes[1]
            cur_command_nodes = nodes
            cur_command_output = []
        else:
            cur_command_output.append(nodes)
    
    commands.append((cur_command_id, cur_command_nodes, cur_command_output))
    cur_command_id = nodes[1]
    cur_command_nodes = nodes
    cur_command_output = []
    return commands


def parse_filesystem(commands):
    fs = MyFileSystem()

    path = []
    for command in commands:
        c_id, c_nodes, c_output = command
        #print(command)
        if c_id == 'cd':
            dir_name = c_nodes[2]
            if dir_name == '..':
                path.pop()
            else:
                fs.add_dir(path, c_nodes[2])
                path.append(c_nodes[2])

            #print(" path:", path)
        elif c_id == 'ls':
            for output_nodes in c_output:
                a, b = output_nodes
                if a == 'dir':
                    fs.add_dir(path, b)
                else:
                    fs.add_file(path, b, a)
    return fs

def part_one(lines):
    commands = parse_commands(lines)

    fs = parse_filesystem(commands)

    fs.print_tree()

    return 0
    
	
def part_two(lines):
	return 0
    

result_part_one = part_one(lines)
result_part_two = part_two(lines)

print("Part 1 result:", result_part_one)
print("Part 2 result:", result_part_two)